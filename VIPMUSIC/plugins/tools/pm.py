import re
from pyrogram import filters
import random
from VIPMUSIC import app


@app.on_message(filters.command(["pm","dm","inbox","private"], prefixes=["pm","dm","inbox","private]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"**odi poda baddu paiya, {sender}enna eanda pm kupdara 🤬🤬**")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**odi poda baddu paiya, {sender}nna eanda pm kupdara 🤬🤬**")
    else: {emoji}**")


def get_random_sticker():
    stickers = [
        "CAACAgIAAx0CerTvRQACFMZmNQ-LfqqGQRXrcIVN3R4rOjMi3QAC_R8AAp5mwUuLKHqA38PyoB4E", # Sticker 1
        "CAACAgIAAx0CerTvRQACFMZmNQ-LfqqGQRXrcIVN3R4rOjMi3QAC_R8AAp5mwUuLKHqA38PyoB4E", # Sticker 2
        "CAACAgIAAx0CerTvRQACFMZmNQ-LfqqGQRXrcIVN3R4rOjMi3QAC_R8AAp5mwUuLKHqA38PyoB4E", # Sticker 3
        "CAACAgIAAx0CerTvRQACFMZmNQ-LfqqGQRXrcIVN3R4rOjMi3QAC_R8AAp5mwUuLKHqA38PyoB4E", # Sticker 4
        "CAACAgIAAx0CerTvRQACFMZmNQ-LfqqGQRXrcIVN3R4rOjMi3QAC_R8AAp5mwUuLKHqA38PyoB4E", # Sticker 5
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "😡",
        "😤",
        "🤬",
    ]
    return random.choice(emojis)
