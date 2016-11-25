from skyscanner_consts import URL, AIRPORT
from time import time
import requests


class SkyScanner:

    @staticmethod
    def get_the_cheapest_price(ap_from, ap_to, arrival_date):
        """

        :param ap_from: <sting> aiport id from consts.AIRPORT
        :param ap_to: <sting> aiport id from consts.AIRPORT
        :arrival_date: <string> date in format 'YYYY-MM-DD'
        :return:
        """
        resp = requests.get(URL.MIN_PRICE.format(date=arrival_date, airport_from=ap_from, airport_to=ap_to)).json()
        resp['response_time'] = time()
        return resp


# if __name__ == '__main__':
#     arrival_date = '2016-11-28'
#     ap_from = AIRPORT.UA_KYIV
#     ap_to = AIRPORT.UA_LVIV
#
#     print (SkyScanner.get_the_cheapest_price(ap_from, ap_to, arrival_date))
