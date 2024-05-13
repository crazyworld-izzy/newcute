import asyncio
import datetime
from VIPMUSIC import app
from pyrogram import Client
from VIPMUSIC.utils.database import get_served_chats
from config import START_IMG_URL, AUTO_GCAST_MSG, AUTO_GCAST, LOGGER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

AUTO_GCASTS = f"{AUTO_GCAST}" if AUTO_GCAST else True

START_IMG_URLS = "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"

MESSAGES = f"""  **╭──────⌁᳀⌁╾─────╮\n ‎ ‎ ‎ ‎ [𝐓ᴇᴀᴍ 𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ](https://t.me/Team_Hypers_Networks)\n╰─────╼⌁᳀⌁╾─────╯

𝐈ᴛ'ꜱ 𝐓ʜᴇ 𝐌ᴏꜱᴛ 𝐓ʜᴇᴍᴇ-ᴀʙʟᴇ 𝐎ꜰ 𝐀ʟʟ 𝐒ᴩᴇᴄɪꜰɪᴄ 𝐁ᴏᴛꜱ 𝐓ʜᴇ 𝐍ᴇᴛᴡᴏʀᴋ 𝐈ꜱ 𝐁ᴀꜱᴇᴅ 𝐎ɴ 𝐃ᴇᴠᴇʟᴏᴩɪɴɢ 𝐁ᴏᴛꜱ 𝐀ɴᴅ 𝐆ɪᴠɪɴɢ 𝐓ʜᴇ 𝐒ᴄᴏᴩᴇ 𝐎ꜰ 𝐀ʟʟ 𝐅ᴇᴀᴛᴜʀᴇꜱ 𝐎ꜰ 𝐓ʜᴇ 𝐔ᴩᴄᴏᴍɪɴɢ 𝐁ᴏᴛꜱ.

𝐅ʀᴏᴍ 𝐓ʜᴇ 𝐍ᴇᴛᴡᴏʀᴋ - 𝐖ᴇ 𝐀ʀᴇ 𝐏ʀᴇꜱᴇɴᴛɪɴɢ 𝐓ʜᴇ [ ᴄᴜᴛᴇ ɢɪʀʟ ](https://t.me/Rose_milk_chat_bot)

𝐈ᴛ 𝐈ꜱ 𝐎ɴᴇ 𝐎ꜰ 𝐓ʜᴇ 𝐌ᴏꜱᴛ 𝐀ᴅᴠᴀɴᴄᴇᴅ 𝐁ᴏᴛꜱ 𝐈ɴ 𝐓ʜᴇ 𝐍ᴇᴛᴡᴏʀᴋ.

𝐖ʜɪᴄʜ 𝐇ᴀꜱ 𝐁ᴇᴇɴ 𝐔ᴩᴅᴀᴛᴇᴅ 𝐒ɪɴᴄᴇ 𝐀 𝐖ʜɪʟᴇ.

𝐓ʜᴇ 𝐔ᴩᴅᴀᴛᴇᴅ 𝐅ᴇᴀᴛᴜʀᴇꜱ 𝐀ʀᴇ 𝐋ɪꜱᴛᴇᴅ 𝐁ᴇʟᴏᴡ.🦋

[🦋‌𝆺𝅥𓆩〭〬𝐂𖽪֟፝‌𖾓𖾝ԍ𖽹𖾜֟፝𖾘‌𝆺𝅥😻⤍🖤]

𝐍ᴇᴡ 𝐔ᴘᴅᴀᴛᴇ

𝐒ᴀɢᴀᴍᴀᴛᴀ - /ꜱɢ

𝐓ᴀɢᴀʟʟ - /ᴛᴀɢᴀʟʟ ( ᴄᴜᴢ ᴛᴀɢ )

𝐌ᴇɴᴛɪᴏɴ - /ᴀʟʟ

𝐔ɴʟɪᴍɪᴛᴀᴅ 𝐓ᴀɢ - /ᴜᴛᴀɢ

𝐏ɪᴄᴋᴜᴘ 𝐋ɪɴᴇ- /ᴜʀᴜᴛᴛᴜ, /ᴩɪᴄᴋᴜᴩ

𝐈ᴍᴀɢᴇ 𝐃ᴏᴡɴʟᴏᴀᴅ- /ɪᴍᴀɢᴇ ᴇx:- ʟᴏᴠᴇ

𝐈ᴍᴀɢᴇ 𝐐ᴜʟɪᴛʏ 𝐔ᴘɢʀᴀᴅᴇ - /ᴜᴩꜱᴄᴀʟᴇ

𝐓ʀᴀɴꜱʟᴀᴛᴇ - /ᴛʀ

𝐍ᴏᴛɪᴄ:-

𝐖ᴇʟᴄᴏᴍᴇ 𝐍ᴏᴛɪᴄ

𝐋ᴇғᴛ 𝐍ᴏᴛɪᴄ

𝐉ᴏɪɴ 𝐑ᴇǫ 𝐍ᴏᴛɪᴄ

𝐏ᴍ 𝐃ᴍ 𝐍ᴏᴛɪᴄ

𝐆ɴ 𝐍ᴏᴛɪᴄ

𝐁ᴀᴅ 𝐖ᴏʀᴅꜱ 𝐍ᴏᴛɪᴄ

𝐈ɴғᴏ 𝐍ᴏᴛɪᴄ

𝐎ᴡɴᴇʀ - [𝐼𝑧𝑧𝑦𝑦𝑖𝑟](https://t.me/King_0f_izzy) ❤🖤✨ 

𝐍ᴇᴛᴡᴏʀᴋ - [𝐻𝑦𝑝𝑒𝑟 𝑁𝑒𝑡𝑤𝑜𝑟𝑘](https://t.me/Team_Hypers_Networks) 😎✨**"""


BUTTONS = InlineKeyboardMarkup(
    [
       [
            InlineKeyboardButton("🍷 𝐊𖽹𖽴𖽡𖽖𖽳 𝐌𖽞 😻", url=f"https://t.me/Rose_milk_chat_bot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
       ]
    ]    
)

MESSAGE = f"""**╭──────⌁᳀⌁╾─────╮\n ‎ ‎ ‎ ‎ [𝐓ᴇᴀᴍ 𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ](https://t.me/Team_Hypers_Networks)\n╰─────╼⌁᳀⌁╾─────╯

𝐈ᴛ'ꜱ 𝐓ʜᴇ 𝐌ᴏꜱᴛ 𝐓ʜᴇᴍᴇ-ᴀʙʟᴇ 𝐎ꜰ 𝐀ʟʟ 𝐒ᴩᴇᴄɪꜰɪᴄ 𝐁ᴏᴛꜱ 𝐓ʜᴇ 𝐍ᴇᴛᴡᴏʀᴋ 𝐈ꜱ 𝐁ᴀꜱᴇᴅ 𝐎ɴ 𝐃ᴇᴠᴇʟᴏᴩɪɴɢ 𝐁ᴏᴛꜱ 𝐀ɴᴅ 𝐆ɪᴠɪɴɢ 𝐓ʜᴇ 𝐒ᴄᴏᴩᴇ 𝐎ꜰ 𝐀ʟʟ 𝐅ᴇᴀᴛᴜʀᴇꜱ 𝐎ꜰ 𝐓ʜᴇ 𝐔ᴩᴄᴏᴍɪɴɢ 𝐁ᴏᴛꜱ.

𝐅ʀᴏᴍ 𝐓ʜᴇ 𝐍ᴇᴛᴡᴏʀᴋ - 𝐖ᴇ 𝐀ʀᴇ 𝐏ʀᴇꜱᴇɴᴛɪɴɢ 𝐓ʜᴇ [ ᴄᴜᴛᴇ ɢɪʀʟ ](https://t.me/Rose_milk_chat_bot)

𝐈ᴛ 𝐈ꜱ 𝐎ɴᴇ 𝐎ꜰ 𝐓ʜᴇ 𝐌ᴏꜱᴛ 𝐀ᴅᴠᴀɴᴄᴇᴅ 𝐁ᴏᴛꜱ 𝐈ɴ 𝐓ʜᴇ 𝐍ᴇᴛᴡᴏʀᴋ.

𝐖ʜɪᴄʜ 𝐇ᴀꜱ 𝐁ᴇᴇɴ 𝐔ᴩᴅᴀᴛᴇᴅ 𝐒ɪɴᴄᴇ 𝐀 𝐖ʜɪʟᴇ.

𝐓ʜᴇ 𝐔ᴩᴅᴀᴛᴇᴅ 𝐅ᴇᴀᴛᴜʀᴇꜱ 𝐀ʀᴇ 𝐋ɪꜱᴛᴇᴅ 𝐁ᴇʟᴏᴡ.🦋

[🦋‌𝆺𝅥𓆩〭〬𝐂𖽪֟፝‌𖾓𖾝ԍ𖽹𖾜֟፝𖾘‌𝆺𝅥😻⤍🖤]

𝐍ᴇᴡ 𝐔ᴘᴅᴀᴛᴇ

𝐒ᴀɢᴀᴍᴀᴛᴀ - /ꜱɢ

𝐓ᴀɢᴀʟʟ - /ᴛᴀɢᴀʟʟ ( ᴄᴜᴢ ᴛᴀɢ )

𝐌ᴇɴᴛɪᴏɴ - /ᴀʟʟ

𝐔ɴʟɪᴍɪᴛᴀᴅ 𝐓ᴀɢ - /ᴜᴛᴀɢ

𝐏ɪᴄᴋᴜᴘ 𝐋ɪɴᴇ- /ᴜʀᴜᴛᴛᴜ, /ᴩɪᴄᴋᴜᴩ

𝐈ᴍᴀɢᴇ 𝐃ᴏᴡɴʟᴏᴀᴅ- /ɪᴍᴀɢᴇ ᴇx:- ʟᴏᴠᴇ

𝐈ᴍᴀɢᴇ 𝐐ᴜʟɪᴛʏ 𝐔ᴘɢʀᴀᴅᴇ - /ᴜᴩꜱᴄᴀʟᴇ

𝐓ʀᴀɴꜱʟᴀᴛᴇ - /ᴛʀ

𝐍ᴏᴛɪᴄ:-

𝐖ᴇʟᴄᴏᴍᴇ 𝐍ᴏᴛɪᴄ

𝐋ᴇғᴛ 𝐍ᴏᴛɪᴄ

𝐉ᴏɪɴ 𝐑ᴇǫ 𝐍ᴏᴛɪᴄ

𝐏ᴍ 𝐃ᴍ 𝐍ᴏᴛɪᴄ

𝐆ɴ 𝐍ᴏᴛɪᴄ

𝐁ᴀᴅ 𝐖ᴏʀᴅꜱ 𝐍ᴏᴛɪᴄ

𝐈ɴғᴏ 𝐍ᴏᴛɪᴄ

𝐎ᴡɴᴇʀ - [𝐼𝑧𝑧𝑦𝑦𝑖𝑟](https://t.me/King_0f_izzy) ❤🖤✨ 

𝐍ᴇᴛᴡᴏʀᴋ - [𝐻𝑦𝑝𝑒𝑟 𝑁𝑒𝑡𝑤𝑜𝑟𝑘](https://t.me/Team_Hypers_Networks) 😎✨**"""

"""🔐ᴜꜱᴇ » [/start](https://t.me/{app.username}?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

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
