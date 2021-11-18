import requests as r

from telegram.ext import (
    MessageHandler,
    CommandHandler,
    Filters,
    ConversationHandler,
    CallbackQueryHandler,
)
import os, sys, importlib
from telegram.ext.dispatcher import run_async
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pyrogram import Client
from Botto import dispatcher
from Botto.helper import string as st



Class Starter:
    def _init_(self, name):
              self.photo= ""
              self.text=st.START_MSG.format(name)
              self.reply_markup=InlineKeyboardMarkup(
                     [[InlineKeyboardButton (text="Request", callback_data="h_req"),
                       InlineKeyboardButton (text="Query", callback_data="h_resp")],
                      [InlineKeyboardButton (text="Broken Links", callback_data="h_bl"),
                       InlineKeyboardButton (text="Feeling Lucky", callback_data="h_lucky")]]),
                      )

@run_async 
def start(update, context):
    if update.effective_chat.type == "private":
        stuff = Starter(update.effective_user.first_name)
        return update.effective_message.reply_photo(
            photo=stuff.photo, caption=stuff.text, reply_markup=stuff.reply_markup
        )

    update.effective_message.reply_text(st.START_STRING_GRP)


def h_for_func(update, context):
    query = update.callback_query
    query.answer()
    match = query.data.split("_")[1]
    markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Go back", callback_data="back_btn_help"),
          InlineKeyboardButton(text="Request", switch_inline_query_current_chat="<req> ")]]
    )
    if match == "req":
        query.message.edit_caption(caption=st.REQ_MSG, reply_markup= InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Go back", callback_data="back_btn_help"),
          InlineKeyboardButton(text="about", callback_data="about")]]
    ))
    elif match == "resp":
        query.message.edit_caption(caption=st.QMSG, reply_markup=markup)
    elif match == "bl":
        query.message.edit_caption(caption=st.BL_MSG, reply_markup=markup)
