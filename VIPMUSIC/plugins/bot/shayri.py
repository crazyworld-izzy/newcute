
from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VIPMUSIC import app
from time import time
import asyncio
from VIPMUSIC.utils.extraction import extract_user

# Define a dictionary to track the last message timestamp for each user
user_last_message_time = {}
user_command_count = {}
# Define the threshold for command spamming (e.g., 20 commands within 60 seconds)
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

SHAYRI = [ " **𝑷𝒆𝒏𝒏𝒆𝒚 𝑵𝒆 𝑷𝒂𝒌𝒌𝒂 𝑷𝒂𝒓𝒐𝒕𝒕𝒂 😋✨ 𝑼𝒏 𝑽𝒆𝒆𝒕𝒖𝒌𝒌𝒖 𝑴𝒂𝒑𝒊𝒍𝒂𝒊 𝒂𝒉 𝑵𝒂𝒂𝒏 𝑽𝒂𝒓𝒂𝒕𝒕𝒂🙈✨** ",
           " **𝑵𝒆𝒆 𝑻𝒉𝒂𝒏 𝑬𝒏 𝑲𝒂𝒏𝒂𝒗𝒖 𝑲𝒂𝒏𝒏𝒊 🙈✨ 𝑬𝒏 𝑻𝒉𝒂𝒎𝒃𝒉𝒊𝒌𝒌𝒖 𝑵𝒆 𝑻𝒉𝒂𝒏 𝒅𝒊 𝑨𝒏𝒏𝒊 🤤✨** ",
           " **𝑵𝒆𝒆 𝑲𝒖𝒑𝒕𝒂 𝑵𝒆𝒗𝒆𝒓 𝑳𝒂𝒕𝒆 - 𝒖𝒉 🤭✨ 𝑽𝒂𝒏𝒅𝒉𝒐𝒏𝒆𝒚 𝑻𝒉𝒐𝒓𝒂 𝑮𝒂𝒕𝒆 - 𝒖𝒉 😚✨ 𝑵𝒆𝒆𝒕𝒉𝒂𝒏 𝑬𝒏𝒂𝒌𝒌𝒖 𝑭𝒂𝒕𝒆 - 𝒖𝒉 😋✨ 𝑬𝒏 𝑲𝒐𝒅𝒂 𝑽𝒂𝒛𝒉𝒌𝒂𝒊 𝑶𝒐𝒕𝒕𝒖 💙✨** ",
           " **𝑷𝒂𝒍𝒍𝒖 𝑽𝒆𝒍𝒂𝒌𝒌𝒂 𝑻𝒉𝒆𝒗𝒂 𝑩𝒓𝒖𝒔𝒉 - 𝒖𝒉 😬✨ 𝑵𝒆 𝑻𝒉𝒂𝒏 𝑬𝒏𝒂𝒌𝒌𝒖 𝑪𝒓𝒖𝒔𝒉 - 𝒖𝒉 😘✨ 𝑵𝒂𝒎𝒂𝒌𝒖𝒍𝒍𝒂 𝑬𝒅𝒉𝒖𝒌𝒖 𝑹𝒖𝒔𝒉 - 𝒖𝒉 🥵✨ 𝒀𝒐𝒖 𝒂𝒓𝒆 𝑶𝒏𝒍𝒚 𝑴𝒚 𝑾𝒊𝒔𝒉 - 𝒖𝒉 😇✨** ",
           " **𝑼𝒌𝒌𝒂𝒓𝒂 𝒕𝒉𝒆𝒗𝒂 𝑪𝒉𝒂𝒊𝒓 - 𝒖𝒉 🪑✨ 𝑵𝒆𝒆 𝑲𝒂𝒂𝒕𝒖 𝑬𝒏 𝑴𝒆𝒍𝒂 𝑪𝒂𝒓𝒆 - 𝒖𝒉 🤗✨ 𝑼𝒏 𝑲𝒂𝒊𝒚𝒂𝒂𝒍𝒂 𝑷𝒐𝒅𝒖 𝑺𝒐𝒐𝒓𝒖 🍚✨ 𝑨𝒅𝒉𝒖𝒏𝒂𝒂𝒍𝒂 𝑽𝒊𝒕𝒖𝒓𝒖𝒗𝒆𝒏 𝑩𝒆𝒆𝒓 - 𝒖𝒉 🍻✨** ",
           " **𝑴𝒂𝒛𝒉𝒂𝒊𝒚𝒊𝒍𝒂 𝑨𝒂𝒅𝒖𝒎 𝑴𝒂𝒚𝒊𝒍 -𝒖𝒉 🦚✨ 𝑬𝒏 𝑰𝒓𝒖𝒕𝒕𝒖𝒍𝒂 𝑵𝒆𝒆𝒕𝒉𝒂𝒏 𝑽𝒆𝒚𝒊𝒍 - 𝒖𝒉 🌅✨ 𝑴𝒖𝒌𝒌𝒊 𝑷𝒂𝒅𝒊𝒄𝒉𝒖𝒎 𝑨𝒂𝒏𝒆𝒏 𝑭𝒂𝒊𝒍 - 𝒖𝒉 🙇‍♂️✨ 𝑵𝒆 𝒊𝒍𝒍𝒂𝒅𝒉𝒂 𝑽𝒂𝒛𝒉𝒌𝒂𝒊 𝑱𝒂𝒊𝒍 - 𝒖𝒉 🏤✨** ",
           " **𝑶𝒓𝒖 𝑻𝒉𝒂𝒓𝒂 𝑽𝒂𝒓𝒂𝒊𝒌𝒌𝒖𝒎 𝑷𝒆𝒔𝒖 🥲✨ 𝑼𝒏 𝑴𝒐𝒐𝒄𝒉𝒊 𝑲𝒂𝒂𝒕𝒉𝒖 𝑽𝒆𝒆𝒔𝒖 🌬️✨ 𝑬𝒏𝒂𝒌𝒌𝒂 𝑷𝒂𝒅𝒂𝒄𝒉𝒂𝒏 𝒀𝒆𝒔𝒖 ⛪✨ 𝑵𝒂𝒂𝒏 𝑨𝒂𝒈𝒊 𝑵𝒊𝒌𝒌𝒖𝒓𝒆𝒏 𝑳𝒐𝒐𝒔𝒖 🤪** ",
           " **𝑷𝒂𝒕𝒕𝒂𝒔𝒖 𝑲𝒐𝒍𝒖𝒕𝒉𝒖𝒏𝒂 𝑽𝒆𝒅𝒊𝒌𝒌𝒖𝒎 🎆✨ 𝑵𝒆𝒆 𝑰𝒍𝒍𝒂𝒏𝒂 𝒆𝒏 𝑯𝒆𝒂𝒓𝒕 𝑻𝒉𝒖𝒅𝒊𝒌𝒌𝒖𝒎 💓** ",
           " **𝑪𝒚𝒄𝒍𝒆 𝑶𝒐𝒅𝒂 𝑻𝒉𝒆𝒗𝒂 𝑾𝒉𝒆𝒆𝒍 - 𝒖𝒉 🚲✨ 𝑵𝒆 𝑷𝒆𝒔𝒂𝒍𝒂𝒏𝒂 𝑨𝒂𝒈𝒖𝒅𝒉𝒖 𝑭𝒆𝒆𝒍 - 𝒖𝒉 🥺✨** ",
           " **𝑶𝒐𝒓𝒖𝒌𝒌𝒖 𝑷𝒐𝒗𝒂𝒏𝒈𝒂 𝒃𝒖𝒔𝒖𝒍𝒂 🚌✨ 𝑵𝒆𝒆 𝑰𝒓𝒖𝒌𝒌𝒂 𝑬𝒏 𝑴𝒂𝒏𝒂𝒔𝒖𝒍𝒂 💝✨** ",
           " **𝑽𝒄 𝒍𝒂 𝒑𝒐𝒅𝒂𝒍𝒂𝒎 𝑴𝒖𝒕𝒆 - 𝒖𝒉 🤐✨ 𝑺𝒉𝒐𝒓𝒕 𝑮𝒊𝒓𝒍𝒔 𝑨𝒓𝒆 𝑪𝒖𝒕𝒆 - 𝒖𝒉 😍✨** ",
           " **𝑷𝒂𝒂𝒕𝒊 𝑺𝒆𝒊𝒚𝒖𝒎 𝑽𝒂𝒊𝒕𝒉𝒊𝒚𝒂𝒎 👵✨ 𝑰𝒅𝒉𝒂 𝑹𝒆𝒂𝒅 𝑷𝒂𝒏𝒅𝒓𝒂 𝑵𝒆𝒆 𝑷𝒂𝒊𝒕𝒉𝒊𝒚𝒂𝒎 🤪✨** ",
           " **𝑻𝒉𝒊𝒓𝒖𝒑𝒂𝒕𝒉𝒊 𝒍𝒂 𝑨𝒅𝒊𝒑𝒑𝒂𝒏𝒈𝒂 𝑴𝒐𝒕𝒕𝒂 👨‍🦲✨ 𝑵𝒆𝒆 𝑻𝒉𝒂𝒏 𝑰𝒏𝒅𝒉𝒂 𝑮𝒓𝒐𝒖𝒑 𝒍𝒂𝒚𝒆 𝑲𝒖𝒕𝒕𝒂 🤣✨** ",
           " **𝑲𝒂𝒂𝒊 𝑲𝒂𝒓𝒊 𝑽𝒆𝒕𝒕𝒂 𝑻𝒉𝒆𝒗𝒂 𝑲𝒏𝒊𝒇𝒆 - 𝒖𝒉 🔪✨ 𝑵𝒆𝒆𝒏𝒈𝒂 𝑻𝒉𝒂𝒏 𝑬𝒏 𝑾𝒊𝒇𝒆 - 𝒖𝒉 👰✨** ",
           " **𝒌𝒂𝒅𝒂𝒊 𝒍𝒂 𝑰𝒓𝒖𝒌𝒌𝒖𝒎 𝑺𝒆𝒎𝒊𝒚𝒂🍜✨ 𝑼𝒏𝒈𝒂 𝑨𝒎𝒎𝒂 𝑻𝒉𝒂𝒏 𝑬𝒏𝒂𝒌𝒌𝒖 𝑴𝒂𝒎𝒊𝒚𝒂 🙈✨** ",
           " **𝑪𝒓𝒊𝒄𝒌𝒆𝒕 𝑷𝒍𝒂𝒚 𝑷𝒂𝒏𝒏𝒂 𝑻𝒉𝒆𝒗𝒂 𝑩𝒂𝒍𝒍 - 𝒖𝒉 🏏✨ 𝑰𝒅𝒉𝒂 𝑹𝒆𝒂𝒅 𝑷𝒂𝒏𝒅𝒓𝒂 𝑵𝒆 𝑻𝒉𝒂𝒏 𝑬𝒏 𝑨𝒂𝒍𝒖 🙈✨**",
           " **𝑬𝒏 𝑫𝒐𝒈 𝑵𝒂𝒎𝒆 𝑩𝒐𝒃𝒃𝒚 🐩✨ 𝑼𝒏𝒂𝒌𝒌𝒖 𝑴𝒆𝒔𝒔𝒂𝒈𝒆 𝑷𝒂𝒏𝒅𝒓𝒂𝒅𝒉𝒖 𝒕𝒉𝒂𝒏 𝒆𝒏 𝑯𝒐𝒃𝒃𝒚 🙈✨** ",
           " **𝑲𝒐𝒓𝒂𝒏𝒈𝒖 𝒌𝒌𝒖 𝒊𝒓𝒖𝒌𝒌𝒖𝒎 𝑽𝒂𝒂𝒍𝒖 🐒✨ 𝑵𝒆𝒆 𝒕𝒉𝒂𝒏 𝑬𝒏 𝑨𝒂𝒍𝒖 💌🙀✨** ",
           " 🌺**खुद नहीं जानती वो कितनी प्यारी हैं , जान है हमारी पर जान से प्यारी हैं, दूरियों के होने से कोई फर्क नहीं पड़ता वो कल भी हमारी थी और आज भी हमारी है.**🌺 \n\n**🥀khud nahi janti vo kitni pyari hai jan hai hamari par jan se jyda payari hai duriya ke hone se frak nahi pdta vo kal bhe hamari the or aaj bhe hamari hai.🥀** ",
           " 🌺**चुपके से आकर इस दिल में उतर जाते हो, सांसों में मेरी खुशबु बनके बिखर जाते हो, कुछ यूँ चला है तेरे इश्क का जादू, सोते-जागते तुम ही तुम नज़र आते हो।**🌺 \n\n**🥀Chupke Se Aakar Iss Dil Mein Utar Jate Ho, Saanso Mein Meri Khushbu BanKe Bikhar Jate Ho,Kuchh Yun Chala Hai Tere Ishq Ka Jadoo, Sote-Jagte Tum Hi Tum Najar Aate Ho..🥀** ",
           " 🌺**प्यार करना सिखा है नफरतो का कोई ठौर नही, बस तु ही तु है इस दिल मे दूसरा कोई और नही.**🌺 \n\n**🥀Pyar karna sikha hai naftaro ka koi thor nahi bas tu hi tu hai is dil me dusra koi aur nahi hai.🥀** ",
           " 🌺**रब से आपकी खुशीयां मांगते है, दुआओं में आपकी हंसी मांगते है, सोचते है आपसे क्या मांगे,चलो आपसे उम्र भर की मोहब्बत मांगते है।**🌺\n\n**🥀Rab se apki khushiyan mangte hai duao me apki hansi mangte hai sochte hai apse kya mange chalo apse umar bhar ki mohabbat mangte hai..🥀** ",
           " 🌺**काश मेरे होंठ तेरे होंठों को छू जाए देखूं जहा बस तेरा ही चेहरा नज़र आए हो जाए हमारा रिश्ता कुछ ऐसा होंठों के साथ हमारे दिल भी जुड़ जाए.**🌺\n\n**🥀kash mere hoth tere hontho ko chu jayen dekhun jaha bas teri hi chehra nazar aaye ho jayen humara rishta kuch easa hothon ke sath humare dil bhi jud jaye.🥀** ",
           " 🌺**आज मुझे ये बताने की इजाज़त दे दो, आज मुझे ये शाम सजाने की इजाज़त दे दो, अपने इश्क़ मे मुझे क़ैद कर लो,आज जान तुम पर लूटाने की इजाज़त दे दो.**🌺\n\n**🥀Aaj mujhe ye batane ki izazat de do, aaj mujhe ye sham sajane ki izazat de do, apne ishq me mujhe ked kr lo aaj jaan tum par lutane ki izazat de do..🥀** ",
           " 🌺**जाने लोग मोहब्बत को क्या क्या नाम देते है, हम तो तेरे नाम को ही मोहब्बत कहते है.**🌺\n\n**🥀Jane log mohabbat ko kya kya naam dete hai hum to tere naam ko hi mohabbat kehte hai..🥀** ",
           " 🌺**देख के हमें वो सिर झुकाते हैं। बुला के महफिल में नजर चुराते हैं। नफरत हैं हमसे तो भी कोई बात नहीं। पर गैरो से मिल के दिल क्यों जलाते हो।**🌺\n\n**🥀Dekh Ke Hame Wo Sir Jhukate Hai Bula Ke Mahfhil Me Najar Churate Hai Nafrat Hai Hamse To Bhi Koei Bat Nhi Par Gairo Se Mil Ke Dil Kyo Jalate Ho.🥀** ",
           " 🌺**तेरे बिना टूट कर बिखर जायेंगे,तुम मिल गए तो गुलशन की तरह खिल जायेंगे, तुम ना मिले तो जीते जी ही मर जायेंगे, तुम्हें जो पा लिया तो मर कर भी जी जायेंगे।**🌺\n\n**🥀Tere bina tut kar bikhar jeynge tum mil gaye to gulshan ki tarha khil jayenge tum na mile to jite ji hi mar jayenge tumhe jo pa liya to mar kar bhi ji jayenge..🥀** ",
           " 🌺**सनम तेरी कसम जेसे मै जरूरी हूँ तेरी ख़ुशी के लिये, तू जरूरी है मेरी जिंदगी के लिये.**🌺\n\n**🥀Sanam teri kasam jese me zaruri hun teri khushi ke liye tu zaruri hai meri zindagi ke liye.🥀** ",
           " 🌺**तुम्हारे गुस्से पर मुझे बड़ा प्यार आया हैं इस बेदर्द दुनिया में कोई तो हैं जिसने मुझे पुरे हक्क से धमकाया हैं.**🌺\n\n**🥀Tumharfe gusse par mujhe pyar aaya hai is bedard duniya me koi to hai jisne mujhe pure hakk se dhamkaya hai.🥀** ",
           " 🌺**पलको से आँखो की हिफाजत होती है धडकन दिल की अमानत होती है ये रिश्ता भी बडा प्यारा होता है कभी चाहत तो कभी शिकायत होती है.**🌺\n\n**🥀Palkon se Aankho ki hifajat hoti hai dhakad dil ki Aamanat hoti hai, ye rishta bhi bada pyara hota hai, kabhi chahat to kabhi shikayat hoti hai.🥀** ",
           " 🌺**मुहब्बत को जब लोग खुदा मानते हैं प्यार करने वाले को क्यों बुरा मानते हैं। जब जमाना ही पत्थर दिल हैं। फिर पत्थर से लोग क्यों दुआ मांगते है।**🌺\n\n**🥀Muhabbt Ko Hab Log Khuda Mante Hai, Payar Karne Walo Ko Kyu Bura Mante Hai,Jab Jamana Hi Patthr Dil Hai,Fhir Patthr Se Log Kyu Duaa Magte Hai.🥀** ",
           " 🌺**हुआ जब इश्क़ का एहसास उन्हें आकर वो पास हमारे सारा दिन रोते रहे हम भी निकले खुदगर्ज़ इतने यारो कि ओढ़ कर कफ़न, आँखें बंद करके सोते रहे।**🌺\n\n**🥀Hua jab ishq ka ehsaas unhe akar wo pass humare sara din rate rahe, hum bhi nikale khudgarj itne yaro ki ood kar kafan ankhe band krke sote rhe.🥀** ",
           " 🌺**दिल के कोने से एक आवाज़ आती हैं। हमें हर पल उनकी याद आती हैं। दिल पुछता हैं बार -बार हमसे के जितना हम याद करते हैं उन्हें क्या उन्हें भी हमारी याद आती हैं।**🌺\n\n**🥀Dil Ke Kone Se Ek Aawaj Aati Hai, Hame Har Pal Uaski Yad Aati Hai, Dil Puchhta Hai Bar Bar Hamse Ke, Jitna Ham Yad Karte Hai Uanhe, Kya Uanhe Bhi Hamari Yad Aati Hai,🥀** ",
           " 🌺**कभी लफ्ज़ भूल जाऊं कभी बात भूल जाऊं, तूझे इस कदर चाहूँ कि अपनी जात भूल जाऊं, कभी उठ के तेरे पास से जो मैं चल दूँ, जाते हुए खुद को तेरे पास भूल जाऊं।**🌺\n\n**🥀Kabhi Lafz Bhool Jaaun Kabhi Baat Bhool Jaaun, Tujhe Iss Kadar Chahun Ki Apni Jaat Bhool Jaaun, Kabhi Uthh Ke Tere Paas Se Jo Main Chal Dun, Jaate Huye Khud Ko Tere Paas Bhool Jaaun..🥀** ",
           " 🌺**आईना देखोगे तो मेरी याद आएगी साथ गुज़री वो मुलाकात याद आएगी पल भर क लिए वक़्त ठहर जाएगा, जब आपको मेरी कोई बात याद आएगी.**🌺\n\n**🥀Aaina dekhoge to meri yad ayegi sath guzari wo mulakat yad ayegi pal bhar ke waqt thahar jayega jab apko meri koi bat yad ayegi.🥀** ",
           " 🌺**प्यार किया तो उनकी मोहब्बत नज़र आई दर्द हुआ तो पलके उनकी भर आई दो दिलों की धड़कन में एक बात नज़र आई दिल तो उनका धड़का पर आवाज़ इस दिल की आई.**🌺\n\n**🥀Pyar kiya to unki mohabbat nazar aai dard hua to palke unki bhar aai do dilon ki dhadkan me ek baat nazar aai dil to unka dhadka par awaz dil ki aai.🥀** ",
           " 🌺**कई चेहरे लेकर लोग यहाँ जिया करते हैं हम तो बस एक ही चेहरे से प्यार करते हैं ना छुपाया करो तुम इस चेहरे को,क्योंकि हम इसे देख के ही जिया करते हैं.**🌺\n\n**🥀Kai chehre lekar log yahn jiya karte hai hum to bas ek hi chehre se pyar karte hai na chupaya karo tum is chehre ko kyuki hum ise dekh ke hi jiya karte hai.🥀** ",
           " 🌺**सबके bf को अपनी gf से बात करके नींद आजाती है और मेरे वाले को मुझसे लड़े बिना नींद नहीं आती।**🌺\n\n**🥀Sabke bf ko apni gf se baat karke nind aajati hai aur mere wale ko mujhse lade bina nind nhi aati.🥀** ",
           " 🌺**सच्चा प्यार कहा किसी के नसीब में होता है. एसा प्यार कहा इस दुनिया में किसी को नसीब होता है.**🌺\n\n**🥀Sacha pyar kaha kisi ke nasib me hota hai esa pyar kahan is duniya me kisi ko nasib hota hai.🥀** " ]

# Command
SHAYRI_COMMAND = ["gf", "bf", "shayri", "sari", "shari", "love"]

@app.on_message(
    filters.command(SHAYRI_COMMAND)
    & filters.group
    )
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(SHAYRI),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍷 𝐍𖽞𖾓𖾟𖽙𖾖ᴋ 😻", url=f"https://t.me/Team_Hypers_Networks"),
                    InlineKeyboardButton(
                        "🍷 𝐎𖾟𖽡𖽞𖾖 😻", url=f"https://t.me/King_0f_izzy")
                    
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(SHAYRI_COMMAND)
    & filters.private
    )
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(SHAYRI),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         "🍷 𝐍𖽞𖾓𖾟𖽙𖾖ᴋ 😻", url=f"https://t.me/Team_Hypers_Networks"),
                    InlineKeyboardButton(
                        "🍷 𝐎𖾟𖽡𖽞𖾖 😻", url=f"https://t.me/King_0f_izzy")
                    
                ]
            ]
        ),
    )
