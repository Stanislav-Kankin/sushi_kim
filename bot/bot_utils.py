from telegram import ReplyKeyboardMarkup
from pars.pars_main import (
    create_link, create_name, create_price,
    link_list, names_list, price_list
    ) 


def hello_user(update, context) -> None:
    # Приветствуем пользователя по имени
    name = update.message.from_user.first_name
    update.message.reply_text(
        f'Привет, {name}, приятного использования!',
        reply_markup=main_keyboard()
    )


def create_user_text(update, context) -> None:
    # Собираем данные с сайта и возвращаем в бот в виде текста
    create_name()
    create_price()
    create_link()
    if len(names_list) == len(price_list) == len(link_list):
        for i in range(len(names_list)):
            update.message.reply_text(
                f'ссылка на товар - {link_list[i]}\n'
                f'Сет {names_list[i]} по цене {price_list[i]}'
            )


def main_keyboard() -> None:
    return ReplyKeyboardMarkup(
        [
            ['Покажи сеты']
        ]
    )
