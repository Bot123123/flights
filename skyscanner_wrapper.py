from skyscanner_consts import URL
from time import time
import requests

arrival_date = '2016-11-28'

resp = requests.get(URL.MIN_PRICE.format(date=arrival_date, airport_from='KBP', airport_to='LWO')).json()
resp['response_time'] = time()

print resp