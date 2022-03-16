import requests

API_KEY = ''

class CurrencyExchange:

    def get_current_rates_from_api(self):

        url = 'http://api.exchangeratesapi.io/v1/latest?access_key='+API_KEY
        return requests.get(url).json()

    def get_rate(self, currency):
        self.currency = currency
        return self.get_current_rates_from_api()['rates'][self.currency]

    def get_converted_amount(self, amount, currency):
        self.amount = amount
        self.currency = currency
        return round(float(self.amount)* float(self.get_rate(self.currency)))
