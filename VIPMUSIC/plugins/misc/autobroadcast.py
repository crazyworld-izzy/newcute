import asyncio
import datetime
from VIPMUSIC import app
from pyrogram import Client
from VIPMUSIC.utils.database import get_served_chats
from config import START_IMG_URL, AUTO_GCAST_MSG, AUTO_GCAST, LOGGER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

AUTO_GCASTS = f"{AUTO_GCAST}" if AUTO_GCAST else False

START_IMG_URLS = "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"

MESSAGES = f"""  **𝐶𝑢𝑡𝑒 𝐺𝑖𝑟𝑙𝑠 🖤✨ 𝐼𝑠 𝐴𝑑𝑣𝑎𝑛𝑐𝑒 𝑀𝑢𝑠𝑖𝑐 𝐵𝑜𝑡  😎🙂‍↔✨

𝑁𝑒𝑤 𝐹𝑒𝑎𝑡𝑢𝑟𝑒 📩✨

𝑃𝑖𝑐𝑘𝑢𝑝 𝑙𝑖𝑛𝑒 💙✨, 𝐿𝑒𝑓𝑡 𝑁𝑜𝑡𝑖𝑐𝑒 😑✨ , 𝑇𝑎𝑔𝑎𝑙𝑙 🥳✨, 𝑉𝑐𝑇𝑎𝑔 🎥✨, 𝑉𝑖𝑑𝑒𝑜 𝐷𝑜𝑤𝑛𝑙𝑜𝑎𝑑 🔽✨, 𝐵𝑎𝑛 🚫✨, 𝑊𝑒𝑙𝑐𝑜𝑚𝑒 𝑁𝑜𝑡𝑖𝑐𝑒 😇✨

𝐶𝑢𝑡𝑒 𝐺𝑖𝑟𝑙 🖤✨ 𝑆𝑝𝑙 𝐹𝑒𝑎𝑡𝑢𝑟𝑒 😻✨

𝑃𝑖𝑐𝑘 𝑈𝑝 𝐿𝑖𝑛𝑒 🔐✨

𝐶𝑚𝑑 📲✨

/uruttu 

/pickup 

/love

𝑃𝑜𝑤𝑒𝑟 𝐵𝑦 - 𝐻𝑦𝑝𝑒𝑟 𝑁𝑒𝑡𝑤𝑜𝑟𝑘 😎✨

𝑂𝑤𝑛𝑒𝑟 - [𝐼𝑧𝑧𝑦𝑦𝑖𝑟](https://t.me/King_0f_izzy) ❤🖤✨ 

𝑁𝑒𝑡𝑤𝑜𝑟𝑘 - [𝐻𝑦𝑝𝑒𝑟 𝑁𝑒𝑡𝑤𝑜𝑟𝑘](https://t.me/Team_Hypers_Networks) 😎✨**"""


BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🦋‌𝆺𝅥𓆩〭〬𝐂𖽪֟፝‌𖾓𖾝 ԍ𖽹𖾜֟፝𖾘 ‌𝆺𝅥😻⤍🖤", url=f"https://t.me/Rose_milk_chat_bot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

MESSAGE = f"""**𝐶𝑢𝑡𝑒 𝐺𝑖𝑟𝑙𝑠 🖤✨ 𝐼𝑠 𝐴𝑑𝑣𝑎𝑛𝑐𝑒 𝑀𝑢𝑠𝑖𝑐 𝐵𝑜𝑡  😎🙂‍↔✨

𝑁𝑒𝑤 𝐹𝑒𝑎𝑡𝑢𝑟𝑒 📩✨

𝑃𝑖𝑐𝑘𝑢𝑝 𝑙𝑖𝑛𝑒 💙✨, 𝐿𝑒𝑓𝑡 𝑁𝑜𝑡𝑖𝑐𝑒 😑✨ , 𝑇𝑎𝑔𝑎𝑙𝑙 🥳✨, 𝑉𝑐𝑇𝑎𝑔 🎥✨, 𝑉𝑖𝑑𝑒𝑜 𝐷𝑜𝑤𝑛𝑙𝑜𝑎𝑑 🔽✨, 𝐵𝑎𝑛 🚫✨, 𝑊𝑒𝑙𝑐𝑜𝑚𝑒 𝑁𝑜𝑡𝑖𝑐𝑒 😇✨

𝐶𝑢𝑡𝑒 𝐺𝑖𝑟𝑙 🖤✨ 𝑆𝑝𝑙 𝐹𝑒𝑎𝑡𝑢𝑟𝑒 😻✨

𝑃𝑖𝑐𝑘 𝑈𝑝 𝐿𝑖𝑛𝑒 🔐✨

𝐶𝑚𝑑 📲✨

/uruttu 

/pickup 

/love

𝑃𝑜𝑤𝑒𝑟 𝐵𝑦 - 𝐻𝑦𝑝𝑒𝑟 𝑁𝑒𝑡𝑤𝑜𝑟𝑘 😎✨

𝑂𝑤𝑛𝑒𝑟 - [𝐼𝑧𝑧𝑦𝑦𝑖𝑟](https://t.me/King_0f_izzy) ❤🖤✨ 

𝑁𝑒𝑡𝑤𝑜𝑟𝑘 - [𝐻𝑦𝑝𝑒𝑟 𝑁𝑒𝑡𝑤𝑜𝑟𝑘](https://t.me/Team_Hypers_Networks) 😎✨

🔐ᴜꜱᴇ » [/start](https://t.me/{app.username}?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

➲ ʙᴏᴛ :** @{app.username}"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🍷 𝐊𖽹𖽴𖽡𖽖𖽳 𝐌𖽞 😻", url=f"https://t.me/Rose_milk_chat_bot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGES

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ. **\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (ᴋᴇᴇᴘ ʙʟᴀɴᴋ & ᴅᴏɴᴛ ᴡʀɪᴛᴇ ᴀɴʏᴛʜɪɴɢ)]**"""

async def send_text_once():
    try:
        await app.send_message(LOGGER_ID, TEXT)
    except Exception as e:
        pass

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URLS, caption=caption, reply_markup=BUTTONS)
                    await asyncio.sleep(20)  # Sleep for 100 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats

async def continuous_broadcast():
    await send_text_once()  # Send TEXT once when bot starts

    while True:
        if AUTO_GCAST:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass

        # Wait for 100000 seconds before next broadcast
        await asyncio.sleep(100000)

# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:  
    asyncio.create_task(continuous_broadcast())
