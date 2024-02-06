import requests

from bs4 import BeautifulSoup

# headers = {
#    """User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1)
# AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"""
# }

suhi_kim_url = ("https://sushikim.ru/sety-rollov")
response = requests.get(suhi_kim_url).text

soup = BeautifulSoup(response, "html.parser")  # html.parser

data_name = soup.find_all("div", class_="rm-module-title")
# собрал в кучу блок с названием
data_price = soup.find_all("span", class_="rm-module-price")

names_list = []  # названия сетов
price_list = []  # цена
link_list = []  # ссылка на сет


def create_name() -> list:
    for elem_name in data_name:
        names_list.append(elem_name.text.replace("\n", ""))
        # добавляем в список название


def create_price() -> list:
    for elem_price in data_price:
        price_list.append(elem_price.text)
        # добавляем в список цены


def create_link() -> list:
    links = soup.find_all("a", class_="order-0")
    # добавляем в список ссылки
    for link in links:
        link_list.append(link.get("href"))


def create_user_text(update, context) -> None:
    create_name()
    create_price()
    create_link()
    if len(names_list) == len(price_list) == len(link_list):
        for i in range(len(names_list)):
            update.message.reply_text(
                f'ссылка на товар - {link_list[i]}\n'
                f'Сет {names_list[i]} по цене {price_list[i]}'
            )