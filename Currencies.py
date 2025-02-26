import requests
import time
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

CURRENCIES_URL = "https://finans.truncgil.com/v3/today.json"
REQUEST_INTERVAL = 300  

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

class CurrencyFetcher:
    def __init__(self):
        self.last_fetch_time = 0
        self.cached_response = {}

    def get_currencies(self):
        current_time = int(time.time())
        if (self.last_fetch_time + REQUEST_INTERVAL) < current_time:
            try:
                logging.info("Fetching new currency data...")
                response = requests.get(CURRENCIES_URL, timeout=10, headers=headers)
                response.raise_for_status()
                self.cached_response = response.json()
                self.last_fetch_time = current_time
            except requests.RequestException as e:
                logging.info(f"Error fetching data: {e}")
                logging.info("data retrieved from cache")
                return self.cached_response
        else:
            logging.info("Using cached data.")
        
        return self.cached_response

    def get_currency(self, name: str, currency: str) -> str:
        data = self.get_currencies()
        if currency in data:
            price = data[currency]["Selling"]
            return f"{currency} / TL\n\n{name}  ->  {price}"
        return "Currency data not available."

    def get_metal(self, name: str, metal: str) -> str:
        data = self.get_currencies()
        if metal in data:
            price = data[metal]["Selling"]
            return f"{name}  ->  {price} TL"
        return "Currency data not available."


if __name__ == "__main__":
    fetcher = CurrencyFetcher()
