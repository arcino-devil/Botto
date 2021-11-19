import os
import sys
from pyrogram import Client
from telethon import TelegramClient
from telegram.ext import Updater
from telegram import ChatAction, ParseMode
from Botto.Config import TOKEN, ID, HASH, LOG_GID, WORMKER

TOKEN = TOKEN
API_ID = ID
WORKERS = WORMKER
API_HASH = HASH
LOG_GID = LOG_GID

updater = Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient('ADC_Req', API_ID, API_HASH)
pgram = Client('ADC_Pyro', api_id=API_ID, api_hash=API_HASH,bot_token=TOKEN)
dispatcher = updater.dispatcher
  
print("Starting Pyrogram Client")
pgram.start
print("Aquiring BOT Client Info")


bottie = pgram.get_me()

BOT_ID = bottie.id
BOT_USERNAME = bottie.username
BOT_NAME = bottie.first_name
BOT_MENTION = bottie.mention



end_credits = """
INFO GATHERED!
Client: ADC Pyro
Copyright: (c) 2021 
AuraMoon55
"""
print(end_credits)
