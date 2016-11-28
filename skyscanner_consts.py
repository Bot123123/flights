API_KEY = 'ho367819377743254221696195510147'
API_URL = 'http://partners.api.skyscanner.net/apiservices'

class CURRENCY:
    USD = 'USD'

#TODO: move currency and other params to consts
class URL:
    MIN_PRICE = '{api_url}/browsequotes/v1.0/UA/{currency}/en-GB/{{airport_from}}/{{airport_to}}/{{date}}?apiKey={key}'\
        .format(currency=CURRENCY.USD, api_url=API_URL, key=API_KEY)


class AIRPORT:
    UA_KYIV = 'KBP'
    UA_KYIV2 = 'IEV'
    UA_LVIV = 'LWO'
    UA_ODESA = 'ODS'
    UA_DNK = 'DNK'