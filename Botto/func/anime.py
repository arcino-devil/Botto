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
              text=st.START_MSG,
              reply_markup=InlineKeyboardMarkup(
                     [[InlineKeyboardButton (text="Request", callback_data="h_req"),
                       InlineKeyboardButton (text="Query", callback_data="h_resp")],
                      [InlineKeyboardButton (text="Broken Links", callback_data="h_bl"),
                       InlineKeyboardButton (text="Feeling Lucky", callback_data="h_lucky")]]),
                      )

def h_for_func(update, context):
    query = update.callback_query
    query.answer()

