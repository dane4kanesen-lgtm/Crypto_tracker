# Crypto Tracker

Kleines Python-Skript, das ich geschrieben habe, um die aktuellen Kurse von Bitcoin und Ethereum abzufragen. Die Daten kommen von der kostenlosen CoinGecko-API.

## Was das Programm macht

Nach dem Start zeigt es die Kurse von BTC und ETH in USD, EUR, RUB, UAH und CNY an, dazu, ob der Kurs in den letzten 24 Stunden gestiegen oder gefallen ist.

Danach kann man noch zwei Sachen ausrechnen lassen:
- wie viel die eigenen Bitcoins gerade wert sind
- wie viele BTC bzw. Satoshis man für einen bestimmten Euro-Betrag bekommt

## Starten

Man braucht nur Python 3, extra Bibliotheken sind nicht nötig.

    python my_btc.py

## Warum ich das gemacht habe

Ich wollte ausprobieren, wie man mit Python Daten aus dem Internet holt. Am Anfang hat die Anfrage nicht funktioniert, bis ich gemerkt habe, dass man einen User-Agent mitschicken muss. Außerdem habe ich gelernt, wie man JSON ausliest und falsche Eingaben mit try/except abfängt.

## Ideen für später

- den Kursverlauf speichern und als Diagramm anzeigen
- mehr Coins einbauen
- vielleicht eine kleine Oberfläche mit tkinter
