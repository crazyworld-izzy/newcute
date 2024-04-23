from VIPMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ "**🐾 𝐵𝑎𝑏𝑒 𝑐𝑜𝑚𝑒 𝑓𝑎𝑠𝑡 𝑖𝑚 𝑤𝑎𝑖𝑡𝑖𝑛𝑔 𝑓𝑜𝑟 𝑦𝑜𝑢😍**",
           "**🌱 𝑂𝑛𝑙𝑖𝑛𝑒 𝑙𝑎 𝑖𝑟𝑢𝑘𝑎 𝑏𝑢𝑡 𝑚𝑒𝑠𝑠𝑎𝑔𝑒 𝑚𝑎𝑡𝑡𝑢𝑚 𝑝𝑎𝑛𝑛𝑎𝑣𝑒 𝑚𝑎𝑎𝑡𝑟𝑎😭**",
           "**🍂 𝑉𝐶 𝑣𝑎 𝑓𝑢𝑛 𝑝𝑎𝑛𝑛𝑎𝑙𝑎𝑚 😂**",
           "**🍁 𝐶ℎ𝑖𝑡ℎ𝑎𝑝𝑝𝑢𝑢 𝑛𝑒𝑒𝑛𝑔𝑎 𝑦𝑒𝑝𝑑𝑖 𝑖𝑛𝑔𝑎 🤔**",
           "**☘️ 𝑟𝑜𝑚𝑏𝑎 𝑏𝑜𝑟𝑒 𝑎ℎ 𝑖𝑟𝑢𝑘𝑢, 𝑦𝑒𝑛𝑜𝑜𝑑𝑎 𝑘𝑜𝑛𝑗𝑎 𝑛𝑒𝑟𝑎𝑚 𝑝𝑒𝑠𝑢 😢**",
           "**🌷 𝑉𝑒𝑒𝑡𝑙𝑎 𝑣𝑒𝑒𝑡𝑖𝑦𝑎 𝑡ℎ𝑎𝑛𝑎 𝑖𝑟𝑢𝑘𝑎 𝑜𝑛𝑙𝑖𝑛𝑒 𝑣𝑎**",
           "**🌹 𝐻𝑒𝑙𝑙𝑜 𝑑𝑒𝑎𝑟 🥰**",
           "**🌺 𝐴𝑛𝑔𝑎 𝑦𝑒𝑛𝑛𝑎 𝑠𝑎𝑝𝑎𝑑𝑢, 𝑦𝑒𝑡ℎ𝑢𝑣𝑎 𝑖𝑟𝑢𝑛𝑡ℎ𝑎𝑙𝑢 𝑦𝑒𝑛𝑛𝑎𝑘𝑢 𝑘𝑜𝑛𝑗𝑎𝑚 𝑝𝑎𝑟𝑐𝑒𝑙 𝑝𝑎𝑛𝑛𝑢 😁**",
           "**✨ 𝐾𝑎𝑙𝑎𝑦𝑖𝑙𝑎 𝑒𝑙𝑢𝑛𝑡ℎ𝑢𝑟𝑢𝑐ℎ𝑢 𝑘𝑢𝑙𝑖𝑐ℎ𝑢 𝑚𝑢𝑑𝑖𝑐ℎ𝑢𝑣𝑖𝑡𝑡𝑢 𝑘𝑜𝑣𝑖𝑙 𝑘𝑢 𝑝𝑜𝑔𝑎 𝑝𝑜𝑟𝑒𝑛 𝑘𝑎𝑑𝑎𝑣𝑢𝑙𝑒𝑒 😆**",
           "**🌱 𝑂𝑖𝑖 𝑙𝑜𝑜𝑠𝑢 𝑚𝑖𝑠𝑠 𝑦𝑜𝑢 🥹**",
           "**🪴 𝑁𝑎𝑎𝑛 𝑦𝑎𝑎𝑟𝑒𝑛𝑑𝑟𝑢 𝑡ℎ𝑒𝑟𝑖𝑔𝑖𝑟𝑎𝑡ℎ𝑎𝑎 😚**",
           "**🧸 𝐼𝑛𝑡ℎ𝑎 𝑔𝑟𝑜𝑢𝑝'𝑙𝑎 𝑢𝑛𝑛𝑎 𝑝𝑎𝑘𝑘𝑎𝑣𝑒 𝑚𝑢𝑑𝑖𝑙𝑎𝑦𝑒 𝑑ℎ𝑒𝑖𝑣𝑎𝑚𝑒**",
           "**🎊 𝐾𝑢𝑚𝑎𝑟𝑢𝑢, 𝑦𝑎𝑟𝑢 𝑖𝑣𝑎𝑛🫣**",
           "**🎉 𝐼𝑣𝑎𝑟𝑎 𝑡ℎ𝑒𝑡𝑖𝑦𝑎𝑡ℎ𝑎 𝑖𝑣𝑎𝑟𝑢𝑡ℎ𝑎𝑛 𝑏𝑟𝑖𝑡𝑖𝑠ℎ 𝑖𝑙𝑎𝑣𝑎𝑟𝑎𝑠𝑎𝑟 𝑐ℎ𝑎𝑟𝑙𝑒𝑠 𝑢ℎℎ 😤**",
           "**🤍 𝑁𝑒𝑒 𝑦𝑎𝑟𝑢𝑛𝑢 𝑦𝑒𝑛𝑛𝑎𝑘𝑢 𝑡ℎ𝑒𝑟𝑖𝑦𝑢𝑚, 𝑛𝑎𝑎 𝑦𝑎𝑟𝑢𝑛𝑢 𝑢𝑛𝑛𝑎𝑘𝑢 𝑡ℎ𝑒𝑟𝑖𝑦𝑢𝑚, 𝑛𝑎𝑚𝑚𝑎 𝑟𝑒𝑛𝑑𝑢 𝑝𝑒𝑟𝑢 𝑦𝑎𝑎𝑟𝑢𝑛𝑢 𝑖𝑛𝑡ℎ𝑎 𝑔𝑟𝑜𝑢𝑝 𝑘𝑒ℎ 𝑡ℎ𝑒𝑟𝑖𝑦𝑢𝑚 🙃**",
           "**🩷 𝑈𝑛𝑛𝑎𝑙𝑎 𝑖𝑝𝑝𝑎 𝑜𝑛𝑙𝑖𝑛𝑒 𝑣𝑎𝑟𝑎 𝑚𝑢𝑑𝑖𝑦𝑢𝑚𝑎 𝑖𝑙𝑙𝑎 𝑚𝑢𝑑𝑖𝑦𝑎𝑡ℎ𝑎 😡**",
           "**❤️‍🩹 𝐼 𝑙𝑜𝑣𝑒 𝑦𝑜𝑢 😍**",
           "**🌹 𝑈𝑛𝑜𝑜𝑑𝑎 𝑝𝑒𝑠𝑎𝑚𝑎 𝑦𝑒𝑛𝑛𝑎𝑘𝑢 𝑡ℎ𝑜𝑜𝑘𝑎𝑚𝑒 𝑣𝑎𝑟𝑙𝑎 🥲**",
           "**🌺 𝑈𝑛𝑜𝑜𝑑𝑎 𝑝ℎ𝑜𝑡𝑜 𝑎𝑛𝑢𝑝𝑢, 𝑛𝑎 𝑢𝑛𝑛𝑎 𝑝𝑎𝑡ℎ𝑎𝑡ℎ𝑒 𝑖𝑙𝑙𝑎 😌**",
           "**✨ 𝑊ℎ𝑎𝑡𝑠𝑎𝑝𝑝 𝑛𝑢𝑚𝑏𝑒𝑟 𝑣𝑒𝑛𝑢𝑚𝑎 𝑢𝑛𝑛𝑎𝑛𝑘𝑢 😳**",
           "**☘️ 𝑁𝑎𝑙𝑙𝑎 𝑘𝑒𝑙𝑎𝑝𝑎𝑟𝑎𝑖𝑛𝑔𝑎𝑦𝑎 𝑏𝑒𝑒𝑡ℎ𝑖𝑦𝑎 🙄**",
           "**🍁 𝑌𝑒𝑛𝑛𝑎 𝑝𝑎𝑛𝑟𝑎 𝑑𝑎𝑟𝑙𝑖𝑛𝑔 ❤️**",
           "**🍂 𝑆𝑖𝑛𝑔𝑙𝑒 𝑎ℎ 𝑖𝑟𝑢𝑘𝑎𝑟𝑎𝑡ℎ𝑢 𝑒𝑣𝑙𝑜 𝑘𝑎𝑠𝑡𝑎𝑚 𝑡ℎ𝑒𝑟𝑖𝑦𝑢𝑚𝑎 𝑣𝑐 𝑣𝑎 𝑠𝑜𝑙𝑟𝑒𝑛**",
           "**🐾 𝐻𝑖𝑖☺️**",
           "**🌱 𝑉𝑎𝑛𝑔𝑎 𝑚𝑎𝑐ℎ𝑎 𝑣𝑎𝑛𝑔𝑎 𝑣𝑎𝑛𝑡ℎ𝑎 𝑣𝑎𝑙𝑖𝑦𝑎 𝑝𝑎𝑎𝑡ℎ𝑢 𝑝𝑜𝑜𝑛𝑔𝑎 😅**",
           "**🎊 𝑉𝑐 𝑣𝑎𝑦𝑒𝑛 𝑔𝑎𝑚𝑒 𝑝𝑙𝑎𝑦 𝑝𝑎𝑛𝑛𝑎𝑙𝑎𝑚 🎮**",
           "**🎉 𝑆𝑎𝑡ℎ𝑖𝑦𝑎𝑚𝑎 𝑠𝑜𝑙𝑟𝑒𝑛𝑑𝑎 𝑛𝑒𝑒 𝑢𝑟𝑢𝑝𝑎𝑑𝑎𝑣𝑒 𝑚𝑎𝑡𝑎 😏**",
           "**🌷 𝑈𝑛𝑛𝑎𝑘𝑢 𝑡ℎ𝑒𝑟𝑖𝑛𝑗𝑎 𝑚𝑒𝑚𝑏𝑒𝑟𝑠 𝑖𝑟𝑢𝑛𝑡ℎ𝑎 𝑘𝑢𝑝𝑡𝑢𝑡𝑢 𝑣𝑎 😌**",
           "**🍁 𝑈𝑛𝑛𝑎 𝑟𝑜𝑚𝑏𝑎 𝑝𝑢𝑑𝑖𝑘𝑢𝑚 😍**",
           "**𝐇𝐞𝐥𝐥𝐨🙊**",
           "**🧸 𝐹𝑜𝑛𝑡 𝑒ℎ 𝑖𝑣𝑙𝑜 𝑎𝑙𝑎𝑔𝑎 𝑖𝑟𝑢𝑘𝑢, 𝑎𝑝𝑜 𝑝𝑜𝑛𝑛𝑢 𝑒𝑣𝑙𝑜 𝑎𝑙𝑎𝑔𝑎𝑎 𝑖𝑟𝑢𝑝𝑎 🙈**",
           "**4 𝑝𝑒𝑟𝑢 4 𝑣𝑖𝑡ℎ𝑎𝑚𝑎 𝑠𝑜𝑙𝑙𝑢𝑣𝑎𝑛𝑔𝑎𝑙𝑎 𝑎𝑛𝑡ℎ𝑎 4 𝑝𝑒𝑟𝑢 𝑙𝑎 𝑜𝑟𝑢𝑡ℎ𝑎𝑛 𝑡ℎ𝑎𝑛 𝑖𝑛𝑡ℎ𝑎 𝑔𝑟𝑜𝑢𝑝 𝑜𝑤𝑛𝑒𝑟 😝**",
           "**🩷 𝑆𝑖𝑛𝑔𝑎𝑝𝑝𝑒𝑛𝑒 😍**",
           "**🌺 𝑃𝑀 𝑝𝑎𝑛𝑛𝑎𝑡ℎ𝑎 𝑑𝑎 𝑣𝑒𝑛𝑛𝑎𝑖 😤**",
           "**🐾 𝑆𝑜𝑛𝑔 𝑘𝑒𝑘𝑎𝑙𝑎𝑚𝑎**",
           "**🌱 𝑉𝑎𝑑𝑎 𝑦𝑒𝑛 𝑚𝑎𝑐ℎ𝑖 𝑣𝑎𝑙𝑎𝑘𝑘𝑎 𝑏𝑎𝑗𝑗𝑖 😆**",
           "**🐾𝐈 𝐋𝐨𝐯𝐞 𝐘𝐨𝐮🙈🙈🙈**",
           "**🎊𝐃𝐨 𝐘𝐨𝐮 𝐋𝐨𝐯𝐞 𝐌𝐞..?👀**",
           "**🎊 𝑁𝑒𝑒 𝑖𝑝𝑝𝑎𝑣𝑎𝑒 𝑣𝑎𝑟𝑎𝑛𝑢𝑚 𝑜𝑛𝑙𝑖𝑛𝑒 𝑢ℎℎ, 𝑦𝑒𝑛𝑛𝑎𝑘𝑢𝑚 𝑝𝑜𝑔𝑎𝑡ℎ𝑒𝑟𝑖𝑦𝑢𝑚 𝑜𝑓𝑓𝑙𝑖𝑛𝑒 𝑢ℎℎ
𝑁𝑒𝑒𝑡ℎ𝑎 𝑦𝑒𝑛𝑜𝑜𝑑𝑎 𝑙𝑖𝑓𝑒𝑙𝑖𝑛𝑒 𝑢ℎℎ 𝑌𝑒𝑛𝑜𝑜𝑑𝑎𝑣𝑒 𝑖𝑟𝑢𝑛𝑡ℎ𝑎 𝑢𝑛 𝑙𝑖𝑓𝑒 𝑓𝑖𝑛𝑒 𝑢ℎℎ**",
           "**✨ 𝐼𝑚 𝑓𝑖𝑛𝑒 🥰 𝑤𝑖𝑙𝑙 𝑦𝑜𝑢 𝑏𝑒 𝑚𝑖𝑛𝑒 😚**",
           "**🌱 𝑇𝑟𝑢𝑡ℎ 𝑜𝑟 𝑑𝑎𝑟𝑒 𝑝𝑙𝑎𝑦 𝑝𝑎𝑛𝑛𝑎𝑙𝑎𝑚 😆**",
           "**🧸 𝐾𝑜𝑛𝑑𝑟𝑢𝑣𝑎 𝑑𝑎 𝑢𝑛𝑛𝑎 🥹**",
           "**✨𝑂𝑟𝑎𝑒 𝑐ℎ𝑎𝑡𝑡𝑖𝑛𝑔 𝑎ℎ 𝑝𝑎𝑛𝑛𝑖𝑡𝑢 𝑖𝑟𝑢𝑘𝑎 𝑏𝑢𝑡 𝑦𝑒𝑛𝑛𝑎𝑘𝑢 𝑜𝑟𝑢 𝑡𝑎𝑔 𝑝𝑜𝑑𝑎 𝑚𝑎𝑡𝑟𝑎 😡**",
           "**🐾 𝑂𝑖𝑖𝑖 𝑣𝑒𝑛𝑛𝑎𝑚𝑎𝑣𝑎𝑙𝑒 😀**",
           "**🧸 𝑈𝑛𝑑𝑎𝑎𝑛𝑎 𝑘𝑎𝑎𝑦𝑎𝑚 𝑦𝑎𝑎𝑣𝑢𝑚 𝑡ℎ𝑎𝑙𝑙𝑎𝑒 𝑚𝑎𝑎𝑟𝑖𝑝𝑜𝑔𝑢𝑚 😝**",
           "**𝐴𝑙𝑜𝑛𝑒 𝑎ℎ 𝑓𝑒𝑒𝑙 𝑝𝑎𝑛𝑟𝑎𝑦𝑎 𝑐ℎ𝑒𝑙𝑙𝑎𝑚 😞**",
           "**𝐻𝑒𝑦 𝑐𝑢𝑡𝑖𝑒 💋**",
           "**𝑀𝑎𝑐ℎ𝑖 𝑜𝑟𝑢 𝑞𝑢𝑎𝑡𝑒𝑟 𝑠𝑜𝑙𝑙𝑢 😜**",
           "**𝑆𝑐ℎ𝑜𝑜𝑙 𝑝𝑜𝑟𝑎𝑦𝑎 𝑖𝑙𝑙𝑎 𝑐𝑜𝑙𝑙𝑒𝑔𝑒 𝑎ℎ?**",
           "**𝑁𝑎𝑛𝑏𝑒𝑛𝑑𝑎 ☺️**",
           "**𝐾𝑎𝑑ℎ𝑎𝑙 𝑝𝑎𝑛𝑟𝑎𝑦𝑎 𝑚𝑎𝑐ℎ𝑖 😳**",
           "**𝑌𝑒𝑛𝑛𝑎 𝑟𝑜𝑚𝑏𝑎 𝑛𝑒𝑟𝑎𝑚 𝑤𝑎𝑖𝑡 𝑝𝑎𝑛𝑛𝑎 𝑣𝑒𝑘𝑘𝑎𝑟𝑎 𝑛𝑒𝑒 😭**",
           "**𝑁𝑒𝑒 𝑠𝑎𝑝𝑡𝑎𝑦𝑎 😋**",
           "**𝑌𝑒𝑛𝑛𝑎𝑘𝑢 𝑠𝑎𝑝𝑎𝑑𝑢 𝑜𝑜𝑡𝑖 𝑣𝑖𝑑𝑢 🙈**",
           "**𝐿𝑒𝑡𝑠 𝑣𝑖𝑏𝑒 𝑑𝑎𝑟𝑙𝑖𝑛𝑔😘**",
           "**𝑦𝑒𝑛𝑛𝑎𝑘𝑢 𝑠𝑡𝑖𝑐𝑘𝑒𝑟𝑠 𝑣𝑒𝑛𝑛𝑢𝑚 𝑝𝑙𝑒𝑎𝑠𝑒 😔**"
           "**𝐇𝐢𝐢👀**",
           "**𝑦𝑒𝑛𝑛𝑎 𝑣𝑎𝑧ℎ𝑘𝑎𝑖 𝑑𝑎 𝑖𝑡ℎ𝑢 😭**",
           "**𝑜𝑢𝑡𝑖𝑛𝑔 𝑝𝑜𝑙𝑎𝑚𝑎 😁**",
           "**𝑦𝑒𝑛𝑡ℎ𝑎 𝑝𝑜𝑛𝑛𝑢𝑚 𝑝𝑒𝑠𝑎𝑚𝑎𝑡𝑟𝑎𝑛𝑔𝑎 𝑡ℎ𝑒𝑟𝑖𝑦𝑢𝑚𝑎 😔**",
           "**𝑁𝑒𝑒 𝑠𝑡𝑒𝑎𝑑𝑦 𝑎ℎ 𝑖𝑙𝑙𝑎 𝑢𝑛 𝑘𝑎𝑎𝑙 𝑡ℎ𝑎𝑟𝑎𝑖𝑙𝑎 𝑝𝑎𝑑𝑎𝑙𝑎 😊 1𝑠𝑡 𝑛𝑖𝑙𝑙𝑢 𝑎𝑝𝑟𝑚 𝑣𝑎𝑛𝑡ℎ𝑢 𝑠𝑜𝑙𝑙𝑢**",
           "**𝐾𝑎𝑑ℎ𝑎𝑙 𝑎𝑎𝑠𝑎𝑖 𝑦𝑎𝑟𝑎𝑖 𝑣𝑖𝑡𝑡𝑎𝑡ℎ𝑜 😊**",
           "**𝑉𝑒𝑟𝑖 𝑎𝑔𝑢𝑡ℎ𝑢 𝑑𝑢𝑑𝑒**",
           "**𝐼𝑛𝑠𝑡𝑎 𝑖𝑑 𝑠𝑜𝑙𝑙𝑢𝑛𝑔𝑎 𝑝𝑙𝑒𝑎𝑠𝑒**",
           "**𝑁𝑒𝑒 𝑖𝑙𝑙𝑎𝑖𝑛𝑎 𝑛𝑎 𝑠𝑒𝑡ℎ𝑢𝑟𝑢𝑣𝑎**",
           "**𝑆𝑎𝑛𝑑𝑎 𝑝𝑜𝑑𝑎𝑙𝑎𝑚𝑎 😂**",
           "**𝑈𝑛𝑜𝑜𝑑𝑎 𝑣𝑜𝑖𝑐𝑒 𝑟𝑜𝑚𝑏𝑎 𝑠𝑤𝑒𝑒𝑡 𝑎ℎ 𝑖𝑟𝑢𝑘𝑢**",
           "**𝑌𝑒𝑛𝑛𝑎 𝑑𝑎 𝑖𝑝𝑑𝑖 𝑝𝑎𝑛𝑟𝑎**",
           "**𝑈𝑛𝑛𝑎𝑘𝑢 𝑝𝑎𝑎𝑠𝑎𝑚𝑒 𝑖𝑙𝑙𝑎**",
           "**𝐴𝑣𝑎𝑛𝑘𝑢𝑑𝑎 𝑝𝑒𝑠𝑎𝑡ℎ𝑎 𝑦𝑒𝑛𝑛𝑎𝑘𝑢 𝑝𝑜𝑠𝑠𝑒𝑠𝑠𝑖𝑣𝑒 𝑎𝑔𝑢𝑡ℎ𝑢**",
           "**𝑈𝑛𝑎𝑘𝑎𝑔𝑎 𝑣𝑎𝑎𝑧ℎ𝑎 𝑛𝑒𝑛𝑎𝑖𝑘𝑢𝑟𝑒𝑛**",
           "**𝐶ℎ𝑒𝑙𝑙𝑎 𝑘𝑢𝑡𝑡𝑢**",
           "**𝐷𝑒𝑦 𝑔𝑢𝑛𝑑𝑎**",
           "**𝑁𝑎 𝑖𝑟𝑢𝑘𝑎 𝑑 𝑢𝑛𝑎𝑘𝑎𝑔𝑎**",
           "**𝑆𝑜𝑙𝑙𝑢𝑛𝑔𝑎 𝑀𝑎𝑚𝑎 𝑘𝑢𝑡𝑡𝑦**",
           "**𝑂𝑣𝑣𝑜𝑟𝑢 𝑝𝑜𝑛𝑛𝑢𝑘𝑢 𝑜𝑣𝑣𝑜𝑟𝑢 𝑓𝑒𝑒𝑙𝑖𝑛𝑔𝑠 𝑚𝑎𝑐ℎ𝑖**",
           "**𝑀𝑎𝑐ℎ𝑖 𝑛𝑎𝑚𝑚𝑎 𝑎𝑠𝑖𝑛𝑔𝑎 𝑝𝑎𝑡𝑡𝑎𝑡ℎ𝑎 𝑦𝑎𝑟𝑢𝑚 𝑝𝑎𝑘𝑎𝑙𝑎𝑖𝑙𝑎**",
           "**𝑀𝑎𝑐ℎ𝑖 𝑛𝑎𝑚𝑚𝑎 𝑎𝑠𝑖𝑛𝑔𝑎 𝑝𝑎𝑡𝑡𝑎𝑡ℎ𝑎 𝑦𝑎𝑟𝑢𝑚 𝑝𝑎𝑘𝑎𝑙𝑎𝑖𝑙𝑎**",
           "**𝑌𝑎𝑟𝑢 𝑛𝑒𝑒 𝑚𝑒𝑦𝑎𝑟𝑎 𝑚𝑎𝑎𝑡𝑎 𝑛𝑎𝑘𝑘𝑎𝑟𝑎 𝑚𝑎𝑎𝑑𝑢 𝑘𝑒𝑑𝑢𝑡ℎ𝑎 𝑚𝑎𝑡ℎ𝑖𝑟𝑖**",
           "**𝑌𝑒𝑛𝑛𝑎 𝑝ℎ𝑖𝑙𝑖𝑝𝑠 𝑢ℎℎ 𝑠𝑎𝑛𝑑𝑎 𝑝𝑜𝑑𝑢𝑣𝑜𝑚𝑎**",
           "**𝐻𝑒𝑙𝑙𝑜 𝑓𝑟𝑎𝑎𝑎𝑛𝑛𝑑𝑑𝑠𝑠**",
           "**𝑉𝑎𝑟𝑎𝑡𝑎𝑎𝑎𝑎.... 𝐷𝑢𝑟𝑟𝑟𝑟𝑟𝑟𝑟**",
           "**𝐴𝑑𝑚𝑖𝑛 𝑝𝑜𝑡𝑎 𝑛𝑎𝑎𝑙 𝑚𝑢𝑑ℎ𝑎𝑙 𝑖𝑛𝑡ℎ𝑎 𝑛𝑎𝑎𝑙 𝑣𝑎𝑟𝑎𝑖 𝑔𝑟𝑜𝑢𝑝 𝑝𝑎𝑘𝑘𝑎𝑚 𝑣𝑎𝑟𝑎𝑣𝑖𝑙𝑙𝑎𝑖...**",
           "**𝑌𝑒𝑛𝑛𝑎 𝑖𝑛𝑡ℎ𝑎 𝑚𝑎𝑎𝑡𝑟𝑎𝑚𝑜 𝑦𝑒𝑛 𝑚𝑎𝑛𝑠𝑢 𝑣𝑎𝑙𝑖𝑘𝑢𝑡ℎ𝑒**",
           "**𝐷𝑒𝑦 𝑝𝑜𝑟𝑢𝑘𝑘𝑖 𝑛𝑒𝑒 ℎ𝑎𝑛𝑑𝑠𝑜𝑚𝑒 𝑑𝑎**",
           "**𝑂𝑖𝑖𝑖 𝑚𝑎𝑚𝑎**",
           "**𝑈𝑛𝑜𝑜𝑑𝑎 𝑠𝑢𝑡ℎ𝑢𝑛𝑎𝑣𝑎𝑛 𝑦𝑒𝑙𝑙𝑎𝑚 𝑜𝑤𝑛 𝑔𝑟𝑜𝑢𝑝 𝑣𝑒𝑐ℎ𝑢 𝑗𝑜𝑙𝑙𝑦 𝑎ℎ 𝑖𝑟𝑢𝑘𝑎𝑛.. 𝑁𝑒𝑒 𝑚𝑎𝑡𝑡𝑢𝑚 𝑦𝑒𝑛 𝑑𝑎 𝑦𝑒𝑛𝑜𝑜𝑑𝑎 𝑢𝑠𝑢𝑟𝑎 𝑒𝑑𝑢𝑡ℎ𝑢𝑡𝑢 𝑖𝑟𝑢𝑘𝑎**",
           "**𝑌𝑒𝑛𝑛𝑎𝑡ℎ𝑎𝑛 𝑖𝑟𝑢𝑛𝑡ℎ𝑎𝑙𝑢 𝑛𝑒𝑒𝑛𝑔𝑎 𝑝𝑒𝑟𝑖𝑦𝑎 𝑎𝑎𝑙𝑢**",
           ]

VC_TAG = [ "**𝐎𝚈𝙴 𝐕𝙲 𝐀𝙰𝙾 𝐍𝙰 𝐏𝙻𝚂🥲**",
         "**𝐉𝙾𝙸𝙽 𝐕𝙲 𝐅𝙰𝚂𝚃 𝐈𝚃𝚂 𝐈𝙼𝙰𝙿𝙾𝚁𝚃𝙰𝙽𝚃😬**",
         "**𝐂𝙾𝙼𝙴 𝚅𝙲 𝙱𝙰𝙱𝚈 𝙵𝙰𝚂𝚃🏓**",
         "**𝐁𝙰𝙱𝚈 𝐓𝚄𝙼 𝐁𝙷𝙸 𝐓𝙷𝙾𝚁𝙰 𝐕𝙲 𝐀𝙰𝙽𝙰🥰**",
         "**𝐎𝚈𝙴 𝐂𝙷𝙰𝙼𝚃𝚄 𝐕𝙲 𝐀𝙰 𝐄𝙺 𝐄𝙰𝙼 𝐇𝙰𝙸🤨**",
         "**𝐒𝚄𝙽𝙾 𝐕𝙲 𝐉𝙾𝙸𝙽 𝐊𝚁 𝐋𝙾🤣**",
         "**𝐕𝙲 𝐀𝙰 𝐉𝙰𝙸𝚈𝙴 𝐄𝙺 𝐁𝙰𝚁😁**",
         "**𝐕𝙲 𝐓𝙰𝙿𝙺𝙾 𝐆𝙰𝙼𝙴 𝐂𝙷𝙰𝙻𝚄 𝐇𝙰𝙸⚽**",
         "**𝐕𝙲 𝐀𝙰𝙾 𝐁𝙰𝚁𝙽𝙰 𝐁𝙰𝙽 𝐇𝙾 𝐉𝙰𝙾𝙶𝙴🥺**",
         "**𝐒𝙾𝚁𝚁𝚈 𝐕𝙰𝙱𝚈 𝐏𝙻𝚂 𝐕𝙲 𝐀𝙰 𝐉𝙰𝙾 𝐍𝙰😥**",
         "**𝐕𝙲 𝐀𝙰𝙽𝙰 𝐄𝙺 𝐂𝙷𝙸𝙹 𝐃𝙸𝙺𝙷𝙰𝚃𝙸 𝐇𝚄🙄**",
         "**𝐕𝙲 𝐌𝙴 𝐂𝙷𝙴𝙲𝙺 𝐊𝚁𝙺𝙴 𝐁𝙰𝚃𝙰𝙾 𝐓𝙾 𝐒𝙾𝙽𝙶 𝐏𝙻𝙰𝚈 𝐇𝙾 𝐑𝙷𝙰 𝐇?🤔**",
         "**𝐕𝙲 𝐉𝙾𝙸𝙽 𝐊𝚁𝙽𝙴 𝐌𝙴 𝐊𝚈𝙰 𝐉𝙰𝚃𝙰 𝐇 𝐓𝙷𝙾𝚁𝙰 𝐃𝙴𝚁 𝐊𝙰𝚁 𝐋𝙾 𝐍𝙰🙂**",
        ]


@app.on_message(filters.command(["tagall"], prefixes=["/", "@", ".", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬. ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠...")
    else:
        return await message.reply("/tagall 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠...")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐁𝐲 /tagalloff , /stopvctag ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stoptagall ||"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["vctag"], prefixes=["/", ".", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬. ")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐁𝐲 /tagalloff , /stopvctag ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stopvctag ||"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["stoptagall", "canceltagall", "offtagall", "tagallstop", "stopvctag", "tagalloff"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠 𝐁𝐚𝐛𝐲.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ 𝐒𝐭𝐨𝐩𝐩𝐞𝐝..♦")
