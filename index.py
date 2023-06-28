import matplotlib.pyplot as plt
import matplotlib.dates as Dates
from data.bitcoin import bitcoin 
from data.ethereum import ethereum 
from data.tether import tether 
from data.usdc import usdc 
from data.binancecoin import binancecoin 
from data.ripple import ripple 
from data.tron import tron 
from data.solana import solana 
from data.dogecoin import dogecoin
from data.cardano import cardano
import datetime
import math

# Define the years and corresponding market caps for each cryptocurrency
bitcoin_data = bitcoin["market_caps"]
ethereum_data = ethereum["market_caps"]
tether_data = tether["market_caps"]
usdc_data = usdc["market_caps"]
binancecoin_data = binancecoin["market_caps"]
ripple_data = ripple["market_caps"]
tron_data = tron["market_caps"]
solana_data = solana["market_caps"]
doge_coin_data = dogecoin["market_caps"]
cardano_data = cardano["market_caps"]

years = []
bitcoin_market_cap = []
ethereum_market_cap = []
tether_market_cap = []
usdc_market_cap = []
bnb_market_cap = []
xrp_market_cap = []
tron_market_cap = []
solana_market_cap = []
dogecoin_market_cap = []
cardano_market_cap = []
BILLION = math.pow(10, 9)

for item in bitcoin_data:
    datetime_obj = datetime.datetime.fromtimestamp(item[0] / 1000.0)
    years.append(Dates.date2num(datetime_obj))

    bitcoin_market_cap.append(item[1] / BILLION)

    if item[0] < ethereum_data[0][0]:
        ethereum_market_cap.append(0)
    if item[0] < tether_data[0][0]:
        tether_market_cap.append(0)
    if item[0] < usdc_data[0][0]:
        usdc_market_cap.append(0)
    if item[0] < binancecoin_data[0][0]:
        bnb_market_cap.append(0)
    if item[0] < ripple_data[0][0]:
        xrp_market_cap.append(0)
    if item[0] < tron_data[0][0]:
        tron_market_cap.append(0)
    if item[0] < solana_data[0][0]:
        solana_market_cap.append(0)
    if item[0] < doge_coin_data[0][0]:
        dogecoin_market_cap.append(0)
    if item[0] < cardano_data[0][0]:
        cardano_market_cap.append(0)

for item in ethereum_data:
    ethereum_market_cap.append(item[1] / BILLION)

for item in tether_data:
    tether_market_cap.append(item[1] / BILLION)

for item in usdc_data:
    usdc_market_cap.append(item[1] / BILLION)

for item in binancecoin_data:
    bnb_market_cap.append(item[1] / BILLION)

for item in ripple_data:
    xrp_market_cap.append(item[1] / BILLION)

for item in tron_data:
    tron_market_cap.append(item[1] / BILLION)

for item in solana_data:
    solana_market_cap.append(item[1] / BILLION)

for item in doge_coin_data:
    dogecoin_market_cap.append(item[1] / BILLION)

for item in cardano_data:
    cardano_market_cap.append(item[1] / BILLION)

# Append 0
for item in range(0, len(years) - len(ethereum_market_cap)):
    ethereum_market_cap.insert(0, 0)
for item in range(0, len(years) - len(bnb_market_cap)):
    bnb_market_cap.insert(0, 0)
for item in range(0, len(years) - len(cardano_market_cap)):
    cardano_market_cap.insert(0, 0)
for item in range(0, len(years) - len(xrp_market_cap)):
    xrp_market_cap.insert(0, 0)
for item in range(0, len(years) - len(dogecoin_market_cap)):
    dogecoin_market_cap.insert(0, 0)
for item in range(0, len(years) - len(tether_market_cap)):
    tether_market_cap.insert(0, 0)
for item in range(0, len(years) - len(usdc_market_cap)):
    usdc_market_cap.insert(0, 0)
for item in range(0, len(years) - len(solana_market_cap)):
    solana_market_cap.insert(0, 0)
for item in range(0, len(years) - len(tron_market_cap)):
    tron_market_cap.insert(0, 0)
# Add more cryptocurrencies and market cap data as needed
plt.yscale = 0.1
# Plot the chart
plt.plot_date(years, bitcoin_market_cap, fmt='-', label='Bitcoin')
plt.plot_date(years, ethereum_market_cap, fmt='-',label='Ethereum')
plt.plot_date(years, bnb_market_cap, fmt='-',label='BNB')
plt.plot_date(years, cardano_market_cap, fmt='-',label='Cardano')
plt.plot_date(years, xrp_market_cap, fmt='-',label='XRP')
plt.plot_date(years, dogecoin_market_cap, fmt='-',label='Dogecoin')

plt.plot_date(years, tether_market_cap, fmt='-',label='USDT')
plt.plot_date(years, usdc_market_cap, fmt='-',label='USDC')
plt.plot_date(years, solana_market_cap, fmt='-',label='Solana')
plt.plot_date(years, tron_market_cap, fmt='-',label='Tron')

# Add more cryptocurrency lines as needed

# Customize the chart
plt.title('Top 10 Cryptocurrencies - Market Capitalization')
plt.xlabel('Year')
plt.ylabel('Market Cap (in billions)')
plt.legend()

# Show the chart
plt.show()
