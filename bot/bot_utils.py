from telegram import ReplyKeyboardMarkup
from db import SushiPars, session


def hello_user(update, context) -> None:
    # Приветствуем пользователя по имени
    name = update.message.from_user.first_name
    update.message.reply_text(
        f'Привет, {name}, приятного использования!',
        reply_markup=main_keyboard()
    )


def create_user_text(update, context) -> None:
    # Собираем данные с сайта и возвращаем в бот в виде текста
    update.message.reply_text(session.query(SushiPars).all())


def main_keyboard() -> None:
    return ReplyKeyboardMarkup(
        [
            ['Покажи сеты']
        ]
    )
