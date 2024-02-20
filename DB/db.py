from sqlalchemy import (
    create_engine, Column,
    String, Integer
)
from sqlalchemy.orm import declarative_base, Session
from pars_main import (
    create_link, create_name, create_price,
    link_list, names_list, price_list
)

engine = create_engine('sqlite:///my_db_kim.db')  # Делаем движок
session = Session(bind=engine)  # Используем класс Session для работы с базой

Base = declarative_base()
create_link()
create_name()
create_price()


class SushiPars(Base):
    __tablename__ = 'sushi_kim'
    id = Column(Integer, primary_key=True)     # ID в базе
    name = Column(String(20), nullable=False)  # Название товара
    price = Column(String(10), nullable=False)  # цена товара, сделал строкой
    link = Column(String(), nullable=False)    # ссылка, сделал строкой


Base.metadata.create_all(engine)

if len(names_list) == len(price_list) == len(link_list):
    # Итерация по данным и добавление их в базу данных
    for i in range(len(names_list)):
        sushi_data = SushiPars(
            name=names_list[i],
            price=price_list[i],
            link=link_list[i]
            )
        session.add(sushi_data)

    # Сохранение изменений в базе данных
    session.commit()
