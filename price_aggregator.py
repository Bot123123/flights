from skyscanner_consts import AIRPORT
from skyscanner_wrapper import SkyScanner
from flights_db import add_price

from itertools import permutations
from datetime import datetime
import time

ALL_AIRPORTS = list(map(lambda x: x[1], filter(lambda x: '__' not in x[0], AIRPORT.__dict__.items())))


def get_all_prices():
    date = '2016-12-12'
    for i in filter(lambda x: x[0] != x[1], permutations(ALL_AIRPORTS, 2)):
        ap_from, ap_to = i
        resp = SkyScanner.get_the_cheapest_price(ap_from, ap_to, date)
        if resp['Quotes']:
            print (ap_from, ap_to, resp['Quotes'][0]['MinPrice'])
            date_timestamp = time.mktime(datetime.strptime('2016-12-12', '%Y-%m-%d').timetuple())
            add_price(ap_from, ap_to, resp['Quotes'][0]['MinPrice'], 'USD', date_timestamp)

get_all_prices()
