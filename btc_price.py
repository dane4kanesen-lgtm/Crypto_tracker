import json
import urllib.request

URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,rub,eur"


def get_btc_price():
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.load(response)
    return data["bitcoin"]


def main():
    try:
        prices = get_btc_price()
    except Exception as e:
        print(f"Не удалось получить курс: {e}")
        return

    print("Курс биткоина (BTC):")
    print(f"  USD: ${prices['usd']:,.2f}")
    print(f"  EUR: €{prices['eur']:,.2f}")
    print(f"  RUB: {prices['rub']:,.2f} ₽")


if __name__ == "__main__":
    main()
