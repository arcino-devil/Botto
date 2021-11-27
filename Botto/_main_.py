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
from Botto import dispatcher, updater
from Botto.helper import string as st
from Botto.func import ALL_FUNCS

from func_name in ALL_FUNCS:
       imported_module = importlib.import_module("Botto.func." + func_name)

       



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

Class Abt:
    def _init_(self, name):
              self.photo= ""
              self.text=st.ABT_MSG.format(name)
              self.reply_markup=InlineKeyboardMarkup(
                     [[InlineKeyboardButton (text="Meet The Dev", callback_data="h_req"),
                       InlineKeyboardButton (text="Go Back", callback_data="back_btn_help")]]
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
        [[InlineKeyboardButton(text="REQUEST MANGA", switch_inline_query_current_chat="<manga> "),
          InlineKeyboardButton(text="REQUEST ANIME", switch_inline_query_current_chat="<anime> ")],
         [InlineKeyboardButton(text="Go Back", callback_data="back_btn_help")]]
    ))
    elif match == "resp":
        query.message.edit_caption(caption=st.QMSG, reply_markup=markup)
    elif match == "bl":
        query.message.edit_caption(caption=st.BL_MSG, reply_markup=markup)

@run_async
def back_btn(update, context):
    query = update.callback_query
    query.answer()
    match = query.data.split("_")
    if "help" in match:
        return start(update)
    stuff = Starter(update.effective_user.first_name)
    query.message.edit_caption(caption=stuff.text, reply_markup=stuff.reply_markup)
    elif "about" in match:
         return about(update)
    stuff = Abt(update.effective_user.first_name)
    query.message.edit_caption(caption=stuff.text, reply markup=stuff.reply_markup)
             


    start_handler = CommandHandler("start", start)
    help_funcs_handler = CallbackQueryHandler(h_for_funcs, pattern=r"h_")
    back_btn_handler = CallbackQueryHandler(back_btn, pattern=r"back_btn")

    dispatcher.add_handler(help_funcs_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(back_btn_handler)

    updater.start_polling(timeout=15, read_latency=4)
    updater.idle()


    if __name__ == "__main__":
    main()

