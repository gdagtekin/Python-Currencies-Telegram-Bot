from pip._vendor import requests
import time
import json

requestInterval = 300
lastCurrenciesTs = int(time.time()) - requestInterval - 1
jsonResponse = ""

currenciesURL = "https://finans.truncgil.com/v3/today.json"

def getCurrencies():
    global lastCurrenciesTs
    global jsonResponse
    global requestInterval
    if (lastCurrenciesTs + requestInterval) < int(time.time()):
        print("request sent")
        response = requests.get(currenciesURL)
        lastCurrenciesTs = int(time.time())
        jsonResponse = response.json()
        return jsonResponse

    else:
        print("data retrieved from cache")
        return jsonResponse


def getCurrency(name, currency):
    json = getCurrencies()
    price = json[currency]["Selling"]
    message = currency + " / TL" + "\n\n" + name + "  ->  " + price
    return message


def getMetal(name, currency):
    json = getCurrencies()
    price = json[currency]["Selling"]
    message = name + "  ->  " + price
    return message


def main() -> None:
    getCurrencies()


if __name__ == "__main__":
    main()
