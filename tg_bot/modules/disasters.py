import json
import html
import os

from typing import List, Optional

from telegram import Bot, Update, ParseMode, TelegramError
from telegram.ext import CommandHandler, run_async
from telegram.utils.helpers import mention_html

from tg_bot import dispatcher, WHITELIST_USERS, SUPPORT_USERS, SUDO_USERS, OWNER_ID
from tg_bot.modules.helper_funcs.extraction import extract_user


def check_user_id(user_id: int, bot: Bot) -> Optional[str]:

    if not user_id:
        reply = "That...is a chat!"
    
    elif user_id == bot.id:
        reply = "This does not work that way."

    else:
        reply = None
    
    return reply


@run_async
def whitelistlist(bot: Bot, update: Update):

    reply = "<b>Whitelist Users🤍:</b>\n"
    for each_user in WHITELIST_USERS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            first_name = user.first_name
            reply += """• <a href="tg://user?id={}">{}</a>\n""".format(user_id, first_name)
        except TelegramError:
            pass
    update.effective_message.reply_text(reply, parse_mode=ParseMode.HTML)


@run_async
def supportlist(bot: Bot, update: Update):

    reply = "<b>Support Users🧡:</b>\n"
    for each_user in SUPPORT_USERS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            first_name = user.first_name
            reply += """• <a href="tg://user?id={}">{}</a>\n""".format(user_id, first_name)
        except TelegramError:
            pass
    update.effective_message.reply_text(reply, parse_mode=ParseMode.HTML)


@run_async
def sudolist(bot: Bot, update: Update):

    reply = "<b>Sudo Users❤:</b>\n"
    for each_user in SUDO_USERS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            first_name = user.first_name
            reply += """• <a href="tg://user?id={}">{}</a>\n""".format(user_id, first_name)
        except TelegramError:
            pass
    update.effective_message.reply_text(reply, parse_mode=ParseMode.HTML)



__help__ = """
**Owner/Sudo only:**
 - /whitelistlist - List whitelisted users.
 - /supportlist - List support users.
 - /sudolist - List sudo users.
"""



WHITELISTLIST_HANDLER = CommandHandler(["whitelistlist"], whitelistlist, filters=CustomFilters.sudo_filter | CustomFilters.support_filter)
SUPPORTLIST_HANDLER = CommandHandler(["supportlist"], supportlist, filters=CustomFilters.sudo_filter | CustomFilters.support_filter)
SUDOLIST_HANDLER = CommandHandler(["sudolist"], sudolist, filters=CustomFilters.sudo_filter | CustomFilters.support_filter)


dispatcher.add_handler(WHITELISTLIST_HANDLER)
dispatcher.add_handler(SUPPORTLIST_HANDLER)
dispatcher.add_handler(SUDOLIST_HANDLER)

__mod_name__ = "Bot Admins"
__handlers__ =[WHITELISTLIST_HANDLER, SUPPORTLIST_HANDLER, SUDOLIST_HANDLER]
