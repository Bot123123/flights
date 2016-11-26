import os
import time
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#TODO: create db only if db_file doesnt exist
engine = create_engine('sqlite:///{current_path}/flight.db'.format(current_path=os.path.dirname(os.path.abspath(__file__))), echo=True)
Base = declarative_base()


class Flights(Base):

    __tablename__ = "prices"

    id = Column(Integer, primary_key=True)
    ap_from = Column(String)
    ap_to = Column(String)
    min_price = Column(Integer)
    currency = Column(String)
    date = Column(Integer)
    current_time = Column(Integer)


    def __init__(self, ap_from, ap_to, min_price, currency, date):
        self.ap_from = ap_from
        self.ap_to = ap_to
        self.min_price = min_price
        self.currency = currency
        self.date = date
        self.current_time = int(time.time())


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def add_price(ap_from, ap_to, min_price, currency, date):
    session = Session()
    session.add(Flights(ap_from, ap_to, int(min_price), currency, int(date)))
    session.commit()

