from sqlalchemy import (
    create_engine, Column,
    String, Integer
)
from sqlalchemy.orm import declarative_base, Session

engine = create_engine('sqlite:///my_db_kim.db')  # Делаем движок
session = Session(bind=engine)  # Используем класс Session для работы с базой

Base = declarative_base()


class SushiPars(Base):
    __tablename__ = 'sushi_kim'
    id = Column(Integer, primary_key=True)     # ID в базе
    name = Column(String(20), nullable=False)  # Название товара
    price = Column(String(10), nullable=False)  # цена товара, сделал строкой
    link = Column(String(), nullable=False)    # ссылка, сделал строкой


Base.metadata.create_all(engine)
