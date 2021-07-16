import requests


def fetch_crypto_price(ticker):
    ticker = ticker.upper()
    r = requests.get(
        f"https://min-api.cryptocompare.com/data/price?fsym={ticker}&tsyms=USD")
    if r.status_code == 200:
        response = r.json()
        if response.get("Response") == "Error":
            return "the specified ticker does not exist!"
        else:
            return f"1 {ticker} ~ ${response['USD']:,}"
    else:
        return "an error occured while fetching price info!"


if __name__ == "__main__":
    while True:
        ticker = input("Enter a ticker: ")
        print(fetch_crypto_price(ticker), "\n")
