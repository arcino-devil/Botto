import itertools
from uuid import uuid4
from telegram.constants import MAX_CAPTION_LENGTH as MAX_CAP_LEN
from telegram import InlineQueryResultArticle, InputTextMessageContent

def article(
    title="", description="", message_text="", thumb_url=None, reply_markup=None
):
    return InlineQueryResultArticle(
        id=uuid4(),
        title=title,
        description=description,
        thumb_url=thumb_url,
        input_message_content=InputTextMessageContent(
            message_text=message_text, disable_web_page_preview=False
        ),
        reply_markup=reply_markup,
    )

def sort_caps(text, c_id, tv=False, mv=False, anime=False, manga=False):
    if len(text) > MAX_CAP_LEN:
        text = text[: MAX_CAP_LEN - 80]
        text += "</em>"
        if tv:
            text += f"<a href='https://www.themoviedb.org/tv/{c_id}'>...read more</a>"
        if mv:
            text += (
                f"<a href='https://www.themoviedb.org/movie/{c_id}'>...read more</a>"
            )
        if anime:
            text += f"<a href='https://kitsu.io/anime/{c_id}'>...read more</a>"
        if manga:
            text += f"<a href='https://kitsu.io/manga/{c_id}'>...read more</a>"

    return text
