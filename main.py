from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

import requests 

import os


API = "https://apis.xditya.me/lyrics?song="


Ek = Client(
    "Lyrics-Search-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


@Ek.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    TEXT = "Hai {} \n\n**I Am Lyrics Search Bot. Send Me A Song Name, I Will Give You The Lyrics. ** \n\nFor Know More /help"
    BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("Channel 🔰", url = "https://telegram.me/EKBOTZ_UPDATE"),InlineKeyboardButton("Support Group ⭕️", url = "https://telegram.me/ekbotz_support")],[InlineKeyboardButton("Repo 🗂️", url = "https://github.com/M-fazin/Github-Search-Bot"),InlineKeyboardButton("Deploy 🗃️", url = "https://heroku.com/deploy?template=https://github.com/M-fazin/Github-Search-Bot")],[InlineKeyboardButton("Developer 💡", url = "https://github.com/M-fazin/")]])
    await update.reply_text(
        text=TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
	
@Ek.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    HELP = "Hai {} \n\n**There Is Nothing To Know More.** \n- Send Me A Song Name, I Will Give Lyrics Of That Song. \nBot By @EKBOTZ_UPDATE "
    HELP_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/EKBOTZ_UPDATE"),InlineKeyboardButton("🗃️ Source Code", url = "https://github.com/M-fazin/Github-Search-Bot")]])
    await update.reply_text(
        text=HELP.format(update.from_user.mention),
        reply_markup=HELP_BUTTON,
        disable_web_page_preview=True,
        quote=True
        )
	
@Ek.on_message(filters.private & filters.command(["about", "source", "repo"]))
async def about(bot, update):
    ABOUT = "**🤖 Bot :** Lyrics Search Bot\n\n**🧑‍💻 Developer :** [M-fazin](https://github.com/M-fazin)\n\n**💻 Channel :** @EKBOTZ_UPDATE\n\n**☎️ Support :** @ekbotz_support \n\n**🗂️ Source Code :** [Github Search Bot](https://github.com/M-fazin/Github-Search-Bot)\n\n**⚙️ Language :** Python 3\n\n**🛡️ Framework :** Pyrogram"
    await update.reply_text(
	text=ABOUT,
	disable_web_page_preview=True,
	quote=True
	)

@Ek.on_message(filters.private & filters.text)
async def sng(bot, message):
        hy = await message.reply_text("`Processing`")
        song = message.text
        chat_id = message.from_user.id
        rpl = userinfo(username)
        try:
                await hy.delete()
                await message.reply_text(chat_id, caption = rpl, reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Link 🔗 ", url = f"github.com/{username}")], [InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/EKBOTZ_UPDATE"),InlineKeyboardButton("🗃️ Source Code", url = "https://github.com/M-fazin/Github-Search-Bot")]]))
        except requests.ConnectionError as exception:
        	await hy.delete()
        	await message.reply_text(f"I Can't Find A User With `{username}`", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻 Developer", url = f"github.com/M-fazin")], [InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/EKBOTZ_UPDATE"),InlineKeyboardButton("🗃️ Source Code", url = "https://github.com/M-fazin/Github-Search-Bot")]]))