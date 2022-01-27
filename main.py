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
    BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("Channel 🔰", url = "https://telegram.me/jetbots"),InlineKeyboardButton("Support Group ⭕️", url = "https://telegram.me/jetbots_support")],[InlineKeyboardButton("Repo 🗂️", url = "https://t.me/jettastic"),InlineKeyboardButton("Deploy 🗃️", url = "https://t.me/jettastic")],[InlineKeyboardButton("Developer 💡", url = "https://t.me/jettastic")]])
    await update.reply_text(
        text=TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
	
@Ek.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    HELP = "Hai {} \n\n**There Is Nothing To Know More.** \n- Send Me A Song Name, I Will Give Lyrics Of That Song. \nBot By @EKBOTZ_UPDATE "
    HELP_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/jetbots"),InlineKeyboardButton("🗃️ Source Code", url = "https://t.me/jettastic")]])
    await update.reply_text(
        text=HELP.format(update.from_user.mention),
        reply_markup=HELP_BUTTON,
        disable_web_page_preview=True,
        quote=True
        )
	
@Ek.on_message(filters.private & filters.command(["about", "source", "repo"]))
async def about(bot, update):
    ABOUT = "**🤖 Bot :** Lyrics Search Bot\n\n**🧑‍💻 Developer :** [Jettastic](https://t.me/jettastic)\n\n**💻 Channel :** @jetbots\n\n**☎️ Support :** @jetbots_support \n\n**🗂️ Source Code :** [Click Here](https://t.me/jettastic)\n\n**⚙️ Language :** Python 3\n\n**🛡️ Framework :** Pyrogram"
    await update.reply_text(
	text=ABOUT,
	disable_web_page_preview=True,
	quote=True
	)

@Ek.on_message(filters.private & filters.text)
async def sng(bot, message):
        hy = await message.reply_text("`Searching 🔎`")
        song = message.text
        chat_id = message.from_user.id
        rpl = lyrics(song)
        await hy.delete()
        try:
                await hy.delete()
                await Ek.send_message(chat_id, text = rpl, reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Dev 🔗 ", url = f"t.me/jettastic")], [InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/jetbots"),InlineKeyboardButton("🗃️ Developer", url = "https://t.me/jettastict")]]))
        except Exception as e:
        	await message.reply_text(f"I Can't Find A Song With `{song}`", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻 Developer", url = f"t.me/jettastic")], [InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/jetbots"),InlineKeyboardButton("🗃️ Developer", url = "https://t.me/jettastic")]]))


def search(song):
        r = requests.get(API + song)
        find = r.json()
        return find
       
def lyrics(song):
        fin = search(song)
        text = f'**🎶 Successfully Extracted Lyrics Of {song} 🎶**\n\n\n\n'
        text += f'`{fin["lyrics"]}`'
        text += '\n\n\n**Made With ❤️ By @jetbots**'
        return text


Ek.run()
