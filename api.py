import requests

API_URL = "https://open.er-api.com/v6/latest/USD"


def get_rates():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()

    data = response.json()

    if data["result"] != "success":
        raise Exception("Could not retrieve exchange rates.")

    return data["rates"]


def convert_currency(amount, from_currency, to_currency):
    rates = get_rates()

    if from_currency not in rates:
        raise Exception(f"Unknown currency: {from_currency}")

    if to_currency not in rates:
        raise Exception(f"Unknown currency: {to_currency}")

    usd_amount = amount / rates[from_currency]

    converted = usd_amount * rates[to_currency]

    exchange_rate = rates[to_currency] / rates[from_currency]

    return converted, exchange_rate