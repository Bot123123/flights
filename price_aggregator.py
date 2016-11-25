from skyscanner_consts import AIRPORT
from skyscanner_wrapper import SkyScanner
from itertools import permutations


ALL_AIRPORTS = list(map(lambda x: x[1], filter(lambda x: '__' not in x[0], AIRPORT.__dict__.items())))


def get_all_prices():
    date = '2016-12-12'
    for i in filter(lambda x: x[0] != x[1], permutations(ALL_AIRPORTS, 2)):
        ap_from, ap_to = i
        resp = SkyScanner.get_the_cheapest_price(ap_from, ap_to, date)
        if resp['Quotes']:
            print (resp['Quotes'][0]['MinPrice'])

get_all_prices()
