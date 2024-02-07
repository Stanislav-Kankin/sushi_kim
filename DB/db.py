from sqlalchemy import(
    create_engine, Table, Column, MetaData,
    String, Integer
)
from sqlalchemy.orm import declarative_base, Session

engine = create_engine('sqlite:///my_db_kim.db')
session = Session(bind=engine)

Base = declarative_base()

class SushiPars(Base):
    __tablename__ = 'sushi_kim'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    price = Column(String(10), nullable=False)
    link = Column(String(), nullable=False)

Base.metadata.create_all(engine)