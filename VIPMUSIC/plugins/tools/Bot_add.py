import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message
from config import LOGGER_ID as LOG_GROUP_ID
from VIPMUSIC import app  
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.utils.database import delete_served_chat
from VIPMUSIC.utils.database import get_assistant


photo = [
    "https://telegra.ph/file/ee9a616090d78437e823f.jpg",
    "https://telegra.ph/file/ee9a616090d78437e823f.jpg",
    "https://telegra.ph/file/ee9a616090d78437e823f.jpg",
    "https://telegra.ph/file/ee9a616090d78437e823f.jpg",
    "https://telegra.ph/file/ee9a616090d78437e823f.jpg",
]

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = message.chat.username if message.chat.username else "🍷 𝐏𖽷𖽹ᵥ𖽖𖾓𖽞  𝐆𖽷𖽙𖽪𖽳 😻"
                msg = (
                    f"** 🦋‌𝆺𝅥𓆩〭〬𝐂𖽪֟፝‌𖾓𖾝 ԍ𖽹𖾜֟፝𖾘 ‌𝆺𝅥😻⤍🖤 #𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ**\n\n"
                    
                    f"**🍷 𝐂𖽻𖽖𖾓 𝐍𖽖𖽧𖽞 😻** {message.chat.title}\n"
                    
                    f"**🍷 𝐂𖽻𖽖𖾓  𝐈𖽴 😻** {message.chat.id}\n"
                    
                    f"**🍷 𝐂𖽻𖽖𖾓 𝐔𖾗𖽞𖽷𖽡𖽖𖽧𖽞 😻** @{username}\n"
                    
                    f"**🍷 𝐌𖽞𖽧𖽜𖽞𖽷𖾗 😻** {count}\n"
                    
                    f"**🍷 𝐀𖽴𖽴𖽞𖽴 𝐁ʏ 😻** {message.from_user.mention}"
                )
                await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"🍷 𝐀𖽴𖽴𖽞𖽴 𝐁ʏ 😻", url=f"tg://openmessage?user_id={message.from_user.id}")]
             ]))
                await userbot.join_chat(f"{username}")
    except Exception as e:
        print(f"Error: {e}")
