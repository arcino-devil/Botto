import requests as r

from telegram.ext import (
    MessageHandler,
    CommandHandler,
    Filters,
    ConversationHandler,
    CallbackQueryHandler,
)

from typing import List, Union
from Botto.Config import COMMAND_PREFIXES, BOT_NAME
from telegram.ext.dispatcher import run_async
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pyrogram import Client
from Botto import dispatcher
from Botto.helper import string as st
from Botto.helper import sort_caps

base_url = "https://kitsu.io/api/edge"
tempdict = {}

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)

@Client.on_message(command["start",f"start@{BOT_NAME}"])
    def _start(client, message):
        client.send_message(
              message.chat.id,
              text=st.


