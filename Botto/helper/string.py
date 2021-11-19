ANIME_STR = """
<b>{}</b> | <b>{}</b>
• Category : <pre>{}</pre>
• Type : <pre>{}</pre>
• Average Rating : <pre>{}</pre>
• Status : <pre>{}</pre>
• First aired : <pre>{}</pre>
• Last aired : <pre>{}</pre>
• Runtime : <pre>{} minutes</pre>
• No of episodes : <pre>{}</pre>
• Synopsis : <em>{}</em>
"""

MANGA_STR = """
<b>{}</b> | <b>{}</b>
• Type : <pre>{}</pre>
• Average Rating : <pre>{}</pre>
• Status : <pre>{}</pre>
• First release : <pre>{}</pre>
• Last release : <pre>{}</pre>
• Volume count : <pre>{}</pre>
• No of chapters : <pre>{}</pre>
• Serialization : <pre>{}</pre>
• Synopsis : <em>{}</em>
"""

START_MSG = """
Welcome To Manga Support Bot

This Bot Will Help You To :-
- Make Requests For Manga
- Ask Queries
- Contact Us

How To Use This Bot :-

✨If You Want To Request an Manga Then Press Request Button

✨If You Want To Ask a Query Then Press Query Button

✨If You Want a Trending Title Press Feeling Lucky Button

🚫Please Refrain From Spamming Or Else You Might Get Banned Permanently

Please Choose From Below"""

REQ_MSG = """
To Request An Anime :-

✨Enter It's Name/Title In English Please 🏷 

✨When The Result You Want Comes Press   I Want This Anime

✨Please Don't Request Hentai/18+ Content Or Else You Might Get Banned 🚫 """

BL_MSG="""
To Report a Broken/Dead link 🔗 :-

Please Forward The Link To This Bot Or Write The Episode Number And Name Of The Anime """

QMSG = """
To Ask a Query Please Write It Here :-

Like If You Want To Know About
• Cross Promo
• Paid Promo
• Any Other Stuff """

TOP_QUERY = """
query ($gnr: String, $page: Int) {
  Page (perPage: 15, page: $page) {
    pageInfo {
      lastPage
      total
    }
    media (genre: $gnr, sort: SCORE_DESC, type: ANIME) {
      title {
        romaji
      }
    }
  }
}
"""

TOPT_QUERY = """
query ($gnr: String, $page: Int) {
  Page (perPage: 15, page: $page) {
    pageInfo {
      lastPage
      total
    }
    media (tag: $gnr, sort: SCORE_DESC, type: ANIME) {
      title {
        romaji
      }
    }
  }
}
"""

ALLTOP_QUERY = """
query ($page: Int) {
  Page (perPage: 15, page: $page) {
    pageInfo {
      lastPage
      total
    }
    media (sort: SCORE_DESC, type: ANIME) {
      title {
        romaji
      }
    }
  }
}
"""
