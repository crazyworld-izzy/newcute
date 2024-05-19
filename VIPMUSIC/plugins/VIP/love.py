from pyrogram import filters
import random
from VIPMUSIC import app


def get_random_message(love_percentage):
    if love_percentage <= 30:
        return random.choice(
            [
                "𝑺𝒕𝒂𝒓𝒕 𝑷𝒂𝒏𝒏𝒖𝒏𝒂 𝑩𝒊𝒌𝒆 𝑹𝒖𝒏 𝑨𝒈𝒖𝒎 🤷🏻🤞🏻 𝑨𝒛𝒉𝒉𝒈𝒆𝒚 𝑵𝒊 𝑰𝒍𝒂 𝑵𝒂 𝑬𝒏 𝑳𝒊𝒇𝒆 𝑬𝒏𝒏𝒂 𝑨𝒈𝒖𝒎 🫣👉🏻🫀",
                "𝑵𝒂𝒎𝒎𝒂 𝑺𝒖𝒕𝒉𝒊 𝑰𝒓𝒖𝒌𝒖𝒕𝒉𝒖 𝑨𝒊𝒓 "" 𝑼𝒖 💨 𝑵𝒊𝒖𝒎 𝑵𝒂𝒏𝒏𝒖𝒎 𝑺𝒆𝒎𝒎𝒂 𝑷𝒂𝒊𝒓 "" 𝑼𝒖 💕👩‍❤️‍👨",
                "𝑷𝒆𝒏𝒏𝒆𝒚 𝑵𝒆 𝑷𝒂𝒌𝒌𝒂 𝑷𝒂𝒓𝒐𝒕𝒕𝒂 😋✨ 𝑼𝒏 𝑽𝒆𝒆𝒕𝒖𝒌𝒌𝒖 𝑴𝒂𝒑𝒊𝒍𝒂𝒊 𝒂𝒉 𝑵𝒂𝒂𝒏 𝑽𝒂𝒓𝒂𝒕𝒕𝒂🙈✨",
            ]
        )
    elif love_percentage <= 70:
        return random.choice(
            [
                "𝑼𝒌𝒌𝒂𝒓𝒂 𝒕𝒉𝒆𝒗𝒂 𝑪𝒉𝒂𝒊𝒓 - 𝒖𝒉 🪑✨ 𝑵𝒆𝒆 𝑲𝒂𝒂𝒕𝒖 𝑬𝒏 𝑴𝒆𝒍𝒂 𝑪𝒂𝒓𝒆 - 𝒖𝒉 🤗✨",
                "𝑲𝒐𝒓𝒂𝒏𝒈𝒖 𝒌𝒌𝒖 𝒊𝒓𝒖𝒌𝒌𝒖𝒎 𝑽𝒂𝒂𝒍𝒖 🐒✨ 𝑵𝒆𝒆 𝒕𝒉𝒂𝒏 𝑬𝒏 𝑨𝒂𝒍𝒖 💌🙀✨",
                "𝑷𝒂𝒂𝒚𝒂𝒔𝒂𝒕𝒉𝒖𝒍𝒂 𝒊𝒓𝒖𝒌𝒌𝒖𝒎 𝑴𝒖𝒏𝒅𝒉𝒊𝒓𝒊 😋✨ 𝑵𝒆𝒆 𝑻𝒉𝒂𝒏 𝑬𝒏 𝑺𝒐𝒑𝒑𝒂𝒏𝒂 𝑺𝒖𝒏𝒅𝒉𝒂𝒓𝒊 😅✨",
            ]
        )
    else:
        return random.choice(
            [
                "𝑺𝒖𝒏𝒅𝒂𝒚 𝑷𝒐𝒗𝒂𝒏𝒈𝒂 𝑩𝒂𝒓 - 𝑼𝒉 🍾🍻 𝑼𝒏𝒏𝒂 𝑷𝒂𝒂𝒕𝒉𝒂𝒅𝒉𝒖 𝑨𝒂𝒈𝒊𝒕𝒆𝒏 𝑮𝒂𝒓 - 𝑼𝒉 🥴✨",
                "𝑵𝒆𝒆 𝑲𝒖𝒑𝒕𝒂 𝑵𝒆𝒗𝒆𝒓 𝑳𝒂𝒕𝒆 - 𝒖𝒉 🤭✨ 𝑽𝒂𝒏𝒅𝒉𝒐𝒏𝒆𝒚 𝑻𝒉𝒐𝒓𝒂 𝑮𝒂𝒕𝒆 - 𝒖𝒉 😚✨",
                "𝑬𝒏𝒂𝒌𝒌𝒂 𝑷𝒂𝒅𝒂𝒄𝒉𝒂𝒏 𝒀𝒆𝒔𝒖 ⛪️✨ 𝑵𝒂𝒂𝒏 𝑨𝒂𝒈𝒊 𝑵𝒊𝒌𝒌𝒖𝒓𝒆𝒏 𝑳𝒐𝒐𝒔𝒖",
            ]
        )


@app.on_message(filters.command("love", prefixes="/"))
def love_command(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        name1 = args[0].strip()
        name2 = args[1].strip()

        love_percentage = random.randint(10, 100)
        love_message = get_random_message(love_percentage)

        response = f"{name1}💕 + {name2}💕 = {love_percentage}%\n\n{love_message}"
    else:
        response = "Please enter two names after /love command."
    app.send_message(message.chat.id, response)
