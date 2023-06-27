import requests

# Define the cryptocurrency symbols and time range
cryptocurrencies = ['bitcoin', 'ethereum', 'binancecoin', 'cardano', 'ripple', 'dogecoin']  # Add more symbols as needed
start_date = '01-01-2013'
end_date = '28-06-2023'

# Define the CoinGecko API endpoint
url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={",".join(cryptocurrencies)}&order=market_cap_desc&per_page=10&page=1&sparkline=false&price_change_percentage=1h'

# Make the API request
response = requests.get(url)
data = response.json()
print(data)
# Extract historical market cap data for each cryptocurrency
for currency_data in data:
    currency_name = currency_data['name']
    currency_market_caps = currency_data['market_caps']
    
    print(f'{currency_name} Market Cap Data:')
    for i, market_cap in enumerate(currency_market_caps):
        date = market_cap[0]
        value = market_cap[1]
        print(f'{date}: {value}')
    
    print('\n')

