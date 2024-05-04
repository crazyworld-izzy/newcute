import re
from pyrogram import filters
import random
from VIPMUSIC import app


@app.on_message(filters.command(["unda","baadu","uthi","otha","omala","kudhi","hevidiya","oolu","uck","mbu","akku","tem","ajii","oka","bu","dangomal","aai punda","ara punda","ombi","thaaaa"], prefixes=["p","b","k","g","g","k","t","p","f","o","n","i","g","o","m","a","n","m","o","o"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"**╭──────⌁᳀⌁╾─────╮\n ‎ ‎ ‎ ‎ [𝐓ᴇᴀᴍ 𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ]((https://t.me/Team_Hypers_Networks)\n╰─────╼⌁᳀⌁╾─────╯</b>\n\n<b>𝐍ᴀ 𝐈ʀᴜᴋᴀ 𝐏ᴀᴋᴋᴀᴍᴇᴀ 𝐄ᴀ 𝐈ᴘᴀᴅɪ 𝐕ᴀʀᴛʜᴀ 𝐏ᴇʀsᴀ 🥺🥺</b>\n\n<b> {sender}</b>\n\n<b>𝐁ʙʏ 𝐈ᴘᴀᴅɪ 𝐋ᴀ 𝐏ᴇᴀsᴀᴛʜᴀ 𝐊ᴀsᴛʜᴀᴍ 𝐈ʀᴜᴋᴜ 🥺👩‍🦯👩‍🦯🚶‍♀**")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**╭──────⌁᳀⌁╾─────╮\n ‎ ‎ ‎ ‎ [𝐓ᴇᴀᴍ 𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ]((https://t.me/Team_Hypers_Networks)\n╰─────╼⌁᳀⌁╾─────╯</b>\n\n<b>𝐍ᴀ 𝐈ʀᴜᴋᴀ 𝐏ᴀᴋᴋᴀᴍᴇᴀ 𝐄ᴀ 𝐈ᴘᴀᴅɪ 𝐕ᴀʀᴛʜᴀ 𝐏ᴇʀsᴀ 🥺🥺</b>\n\n<b> {sender}</b>\n\n<b>𝐁ʙʏ 𝐈ᴘᴀᴅɪ 𝐋ᴀ 𝐏ᴇᴀsᴀᴛʜᴀ 𝐊ᴀsᴛʜᴀᴍ 𝐈ʀᴜᴋᴜ 🥺👩‍🦯👩‍🦯🚶‍♀**")


def get_random_sticker():
    stickers = [
        "CAACAgIAAxkBAALZv2Y1N3SQv-XLAAEWoEPuRHKhcBS8ogACzUMAAkIx6UjssitCRhpjxjQE", # Sticker 1
        "CAACAgIAAxkBAALZwGY1N3R92y-_7iflIJnbC1LFA5xiAAKZOwAC8rboSJO_j_VUOTKeNAQ", # Sticker 2
        "CAACAgUAAxkBAALZwmY1N3TljXSxgoatcCuwLl0nywjuAAJMBQACRp7ZVlBMX_5LR7zONAQ", # Sticker 3
        "CAACAgIAAxkBAALZwWY1N3QZJMZMW3X3DWAKr9dfE6vlAAJ4QgACuIXpSG7QUOzunghRNAQ", # Sticker 4
        "CAACAgEAAxkBAALZw2Y1N3RWHVYxc9cOqId4-LQS1rNXAALWBAACUSkNOcGyHWEutXHhNAQ", # Sticker 5
        "CAACAgUAAxkBAALZxGY1N3RwjFiNZwfs_zqVJoHNI97OAALUCgACSseYVR60yHu3hH3nNAQ", # Sticker 6
        "CAACAgUAAxkBAALZxWY1N3QEMM3PB6z71PZp67yyPQecAAL5CAACPJKZVed8chNvQaiGNAQ", # Sticker 7
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "🥺",
        "👩‍🦯",
        "🚶‍♀",
    ]
    return random.choice(emojis)
