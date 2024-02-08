import requests

from bs4 import BeautifulSoup

suhi_kim_url = ("https://sushikim.ru/sety-rollov")
response = requests.get(suhi_kim_url).text

soup = BeautifulSoup(response, "html.parser")  # html.parser

data_name = soup.find_all("div", class_="rm-module-title")
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





