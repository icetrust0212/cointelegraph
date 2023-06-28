import requests
import time

coins = ["bitcoin", "ethereum", "binancecoin", "cardano", "ripple", "dogecoin", "tether", "usd-coin", "solana", "tron"]
years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

def fetch_market_cap(coin, date):
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/history?date={date}&localization=false"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        market_data = data["market_data"]
        market_cap = market_data["market_cap"]["usd"]
        return market_cap
    else:
        return 0

market_cap_data = []

for coin in coins:
    data_per_year = []
    
    for year in years:
        if year == 2023:
            date = f"27-6-{year}"
        else:
            date = f"31-12-{year}"

        market_cap = fetch_market_cap(coin, date)
        data_per_year.append(market_cap)
        time.sleep(10)
    
    print(coin)
    print(data_per_year)
    print('\n')
    market_cap_data.append(data_per_year)


print(market_cap_data)



