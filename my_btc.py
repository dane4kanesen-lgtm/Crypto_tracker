import json
import urllib.request

URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,rub,eur,uah,cny&include_24hr_change=true"


def get_btc_price():
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.load(response)
    return data


def main():
    try:
        prices = get_btc_price()
    except Exception as e:
        print(f"Es ist nicht gelungen, den Kurs yu erhalten.: {e}")
        return

    print("Bitcoin Kurs (BTC):")
    print(f"  USD: ${prices['bitcoin']['usd']:,.2f}")
    print(f"  EUR: €{prices['bitcoin']['eur']:,.2f}")
    print(f"  RUB: {prices['bitcoin']['rub']:,.2f} ₽")
    print(f"  UAH: {prices['bitcoin']['uah']:,.2f} ₴")
    print(f"  CNY: {prices['bitcoin']['cny']:,.2f} ¥")

    print("Ethereum Kurs (ETH):")
    print(f"  USD: ${prices['ethereum']['usd']:,.2f}")
    print(f"  EUR: €{prices['ethereum']['eur']:,.2f}")
    print(f"  RUB: {prices['ethereum']['rub']:,.2f} ₽")
    print(f"  UAH: {prices['ethereum']['uah']:,.2f} ₴")
    print(f"  CNY: {prices['ethereum']['cny']:,.2f} ¥")

    # 24-h Anstieg oder Rückgang
    btc_change = prices['bitcoin']['usd_24h_change']
    if btc_change > 0:
        print(f"📈 BTC 24h-Anstieg: {btc_change:.2f}%")
    else:
        print(f"📉 BTC 24h-Rückgang: {btc_change:.2f}%")

    eth_change = prices['ethereum']['usd_24h_change']
    if eth_change > 0:
        print(f"📈 ETH 24h-Anstieg: {eth_change:.2f}%")
    else:
        print(f"📉 ETH 24h-Rückgang: {eth_change:.2f}%")

    # Wie viel sind meine Bitcoins wert?
    currency = input("IN welcher Währung berechnen? (usd/eur/rub/uah/cny): ").strip().lower()
    if currency in ("usd", "eur", "rub", "uah", "cny"):
        try:
            amount = float(input("Wie viel BTC haben Sie? "))
            total = amount * prices['bitcoin'][currency]
            print(f"{amount} BTC = {total:,.2f} {currency.upper()}")
        except ValueError:
            print("Ungültige Menge eingegeben.")
    else:
        print("Ungültige Währung.")

    # Wie viel Bitcoin kann ich kaufen?
    try:
        euro = float(input("Wie viel Euro haben Sie? "))
        btc_amount = euro / prices['bitcoin']['eur']
        print(f"Für {euro} € Können Sie {btc_amount:.8f} BTC kaufen")
        print(f"Das sind {btc_amount * 100_000_000:,.0f} Satoshis")
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein.")


if __name__ == "__main__":
    main()
