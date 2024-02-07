from telegram import ReplyKeyboardMarkup
from pars.pars_main import create_user_text


def hello_user(update, context):
    name = update.message.from_user.first_name
    update.message.reply_text(
        f'Привет, {name}, приятного использования!',
        reply_markup=main_keyboard()
    )


def check_set(update, context):
    message = create_user_text()
    for user_text in message:
        update.message.reply_text(user_text)


def main_keyboard() -> None:
    return ReplyKeyboardMarkup(
        [
            ['Покажи сеты']
        ]
    )
