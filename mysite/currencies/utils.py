import requests


url = 'https://api.exchangeratesapi.io/latest'


def get_currency_rates_from_api(base_currency):
    req = requests.get(url, params={'base': base_currency})

    if req.status_code == 200:
        data = req.json()
        return data['rates']
    return req.status_code
