import matplotlib.pyplot as plt
import matplotlib.dates as Dates

import datetime
import math


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
