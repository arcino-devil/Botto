import requests as r

from telegram.ext import InlineQueryHandler
from telegram.ext.dispatcher import run_async
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from Botto import dispatcher
from Botto.helper import string as st
from Botto.helper.parsa import article
from Botto.helper.database import user_sql as sq
from Botto import LOG_GID

anime_url = "https://kitsu.io/api/edge"

@run_async
def inlinequery(update, context):
    query = update.inline_query.query
    chet = inline_query.from_user
    sq.update_user(
        update.inline_query.from_user.id, update.inline_query.from_user.username
    )
    results = []
    if len(query) > 0:
     if query.startswith("<anime>"):
            query = query.replace("<anime>", "")
            res = r.get(f"{anime_url}/anime?filter%5Btext%5D={query}")
            if res.status_code != 200:
                return
            res = res.json()["data"]

            for con in res:
                data = con["attributes"]
                results.append(
                    article(
                        title=data["titles"].get("en", "NA"),
                        description=data["titles"].get("ja_jp", ""),
                        thumb_url=data["posterImage"]["original"],
                        message_text=st.ANIME_STR.format(
                            data["titles"].get("en", ""),
                            data["titles"].get("ja_jp", ""),
                            data.get("subtype", "N/A"),
                            data.get("ageRatingGuide", "N/A"),
                            data.get("averageRating", "N/A"),
                            data.get("status", "N/A"),
                            data.get("startDate", "N/A"),
                            data.get("endDate", "N/A"),
                            data.get("episodeLength", "N/A"),
                            data.get("episodeCount", "N/A"),
                            data.get("synopsis", "N/A"),
                        )
                        + f"<a href='{data['posterImage']['original']}'>&#xad</a>",
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton(text="I want this", callback_data="re_wa"),
                            InlineKeyboardButton(text="I Dont Want this", callback_data="re_no")]]
                             ),
                            )
                           )
                          )
     elif query.startswith("<manga>"):
            query = query.replace("<manga>", "")
            res = r.get(f"{anime_url}/manga?filter%5Btext%5D={query}")
            if res.status_code != 200:
                return
            res = res.json()["data"]

            for con in res:
                data = con["attributes"]
                results.append(
                    article(
                        title=data["titles"].get("en", "NA"),
                        description=data["titles"].get("ja_jp", ""),
                        thumb_url=data["posterImage"]["original"],
                        message_text=st.MANGA_STR.format(
                            data["titles"].get("en", ""),
                            data["titles"].get("ja_jp", ""),
                            data.get("subtype", "N/A"),
                            data.get("averageRating", "N/A"),
                            data.get("status", "N/A"),
                            data.get("startDate", "N/A"),
                            data.get("endDate", "N/A"),
                            data.get("volumeCount", "N/A"),
                            data.get("chapterCount", "N/A"),
                            data.get("serialization", "N/A"),
                            data.get("synopsis", "N/A"),
    )
                        + f"<a href='{data['posterImage']['original']}'>&#xad</a>",
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton(text="I want this", callback_data="re_wa"),
                            InlineKeyboardButton(text="I Dont Want this", callback_data="re_no")]]
                             ),
                            )
                           )

update.inline_query.answer(results[:50], cache_time=10)

@run_async 
def re_for_funcs(update, context):
    query = update.callback_query
    chet_id = callback_query.from_user.username
     msg = dispatcher.get_history(f"{chet_id}", limit=1)
    query.answer()
    match = query.data.split("_")[1]
    if match == "wa":
       dispatcher.send_message(f"{LOG_GID}", f"{msg}")
     if match == "no":
          dispatcher.send_message(f"{LOG_GID}", "I couldn't find the correct anime")


    INLINE_HANDLER = InlineQueryHandler(inlinequery)
    re_funcs_handler = CallbackQueryHandler(re_for_funcs, pattern=r"re_")

    dispatcher.add_handler(INLINE_HANDLER)
    dispatcher.add_handler(re_funcs_handler)

       
   

 
