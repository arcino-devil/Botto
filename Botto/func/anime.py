import requests as r

from telegram.ext import (
    MessageHandler,
    CommandHandler,
    Filters,
    ConversationHandler,
    CallbackQueryHandler,
)

from telegram.ext.dispatcher import run_async
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply

from Botto import dispatcher
from Botto.helper import strings as st
from Botto.helper import sort_caps

base_url = "https://kitsu.io/api/edge"
tempdict = {}
