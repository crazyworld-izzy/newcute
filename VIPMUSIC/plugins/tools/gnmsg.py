import re
from pyrogram import filters
import random
from VIPMUSIC import app


@app.on_message(filters.command(["ood night","ood night","i8","weet dreams","weet dreams","i8","n","n"], prefixes=["g","G","n","N","s","S","g","G"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"**𝐂ʜʟᴍ 𝐕.ᴄᴀʟʟ 𝐏ᴇᴀsᴀʟᴀᴍ 𝐏ᴀʀᴛʜᴀ 𝐀ᴛʜᴜᴋᴜʟʟᴀ 𝐓ʜᴜɴɢᴀ 𝐏ᴏʀɪʏᴇᴀ 🥺😢👩‍🦯</b>\n\n<b>{sender}</b>\n\n<b>𝐂ʜᴇʀʀɪ 𝐁ʙʏ 𝐍ᴀᴍᴍᴀ 𝐃ʀᴇᴀᴍ 𝐋ᴀ 𝐑ᴏᴍᴀɴᴄᴇ 𝐏ᴀɴɴᴀʟʟᴀᴍ 🙈😏❤️**")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**𝐂ʜʟᴍ 𝐕.ᴄᴀʟʟ 𝐏ᴇᴀsᴀʟᴀᴍ 𝐏ᴀʀᴛʜᴀ 𝐀ᴛʜᴜᴋᴜʟʟᴀ 𝐓ʜᴜɴɢᴀ 𝐏ᴏʀɪʏᴇᴀ 🥺😢👩‍🦯</b>\n\n<b>{sender}</b>\n\n<b>𝐂ʜᴇʀʀɪ 𝐁ʙʏ 𝐍ᴀᴍᴍᴀ 𝐃ʀᴇᴀᴍ 𝐋ᴀ 𝐑ᴏᴍᴀɴᴄᴇ 𝐏ᴀɴɴᴀʟʟᴀᴍ 🙈😏❤️</b>\n\n<b>{emoji}**")


def get_random_sticker():
    stickers = [
        "CAACAgQAAxkBAALZeGY1ILUPxohB0luoydqksVTuoX4zAAIHEAACLNsJUL3QO8ZF22ANNAQ", # Sticker 1
        "CAACAgEAAxkBAALZeWY1ISKokwYWad4wKQABfS_9_jx0cwACXgQAAjO2mUdGJHmjJt0XijQE", # Sticker 2
        "CAACAgUAAxkBAALZemY1IWcGaVbdSngItwwX45xTT9QIAAIHCQACq6yJV0lq6JFdFk7rNAQ", # Sticker 3
        "CAACAgUAAxkBAALZe2Y1IXOtVPGl4fazaqYAARMduBhFzwACIQoAAp3ykFeX0LLsBqaZ8zQE", # Sticker 4
        "CAACAgUAAxkBAALZfGY1Ic97NbnmKZpoSfzBfTXN_p84AALuBQAC5tOxVCQr3PRKSJ9vNAQ", # Sticker 5
        "CAACAgUAAxkBAALZfWY1IeUXeA9R8CR8l8L21f8XGW4lAAJABwACkLqwVODj_VQsKv8CNAQ", # Sticker 6
        "CAACAgQAAxkBAALZfmY1IgdQZG1hUEnvgqra-eRHVvTTAAJPDgACVBOpUJTgjnyWTMB-NAQ", # Sticker 7
        "CAACAgUAAxkBAALZkGY1JTTDtrQkb-RHipGbThlTLB4tAALPCAACfqvBVy9tJEb8PKOZNAQ", # Sticker 8
        "CAACAgUAAxkBAALZkWY1JTjpG3dCi9Vcoyq92vrpj2gQAALYBwAC1X3AV_SIwOW7YwO7NAQ", # Sticker 9
        "CAACAgUAAxkBAALZkmY1JUIVQ0wbdKfjRpfrIoNMK3iVAAK6BwACMenIVydDlnhGaHYtNAQ", # Sticker 10
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "😴",
        "😪",
        "💤",
    ]
    return random.choice(emojis)
