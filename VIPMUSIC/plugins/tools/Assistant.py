from pyrogram import Client, filters
import asyncio
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
from pyrogram.errors import (
    PeerIdInvalid,
    ChatWriteForbidden
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", "10284859"))
API_HASH = getenv("API_HASH", "b0ad58eb8b845ba0003e0d9ce5fc2196")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://monivps5:monivps5@cluster0.kmbq8we.mongodb.net/?retryWrites=true&w=majority")
STRING1 = getenv("STRING_SESSION", "BQE9p8oAHK2EhvZYJF_Nq8-Cj0PlqY6vs_REMoHtxEVP7Fuotd-JdlPs_4CQgxYEEQZ4hztyzbqKe6enTVtKuWAGqZyvwhrGKQrnzg4B6eCZT4XVQcJin1xIdAShEQsSCniPljZiFf0D5CyeRR2GkOymHNX5iK-6WBHhtA2zIemxlQrdvX1lKbZSGG8AlaIkRlalYOVtBpF76J74FpsRhwfRA7N8m5yzyK_12w8EJIL5QLbkgt-rhjBa9_CU-g8LG69hhrQ2iwenh4RZmn1-SLW6VtsMwh8wV-FYSq9x_lqYnMMaeJRte_fXoHHH6MY_GdvF8J7AUEeKihRJDlhDXHkWs8MqwQAAAAGEyHmmAA")


client = Client(STRING1, API_ID, API_HASH)



@client.on_message(
    filters.command("alive", prefixes=["/", ".", "?", "-"])
    & filters.private & filters.group)
async def start(client, message):
    await message.reply_text(f"**ᴀʟᴇxᴀ ᴀɪ ᴜsᴇʀʙᴏᴛ ғᴏʀ ᴄʜᴀᴛᴛɪɴɢ ɪs ᴡᴏʀᴋɪɴɢ**")
    
