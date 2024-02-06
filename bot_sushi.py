from telegram.ext import (
    Updater, MessageHandler,
    CommandHandler, Filters
)

from config import TOKEN
from bot_utils import hello_user
from pars_main import create_user_text


def start_bot() -> None:
    bot = Updater(TOKEN, use_context=True)
    dp = bot.dispatcher

    dp.add_handler(CommandHandler(
        'start', hello_user
    ))

    dp.add_handler(MessageHandler(
        Filters.regex('^(Покажи сеты)$'), create_user_text
    ))

    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    start_bot()
