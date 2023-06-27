import matplotlib.pyplot as plt

# Define the years and corresponding market caps for each cryptocurrency
years = [2017, 2018, 2019, 2020, 2021]  # Add more years as needed
bitcoin_market_cap = [15.5, 66, 121, 186, 900]  # Replace with actual market cap values
ethereum_market_cap = [0.7, 13, 15, 14, 350]  # Replace with actual market cap values
bnb_market_cap = [0, 0, 2.7, 2.6, 90]  # Replace with actual market cap values
ada_market_cap = [0, 0, 1.2, 1.9, 85]  # Replace with actual market cap values
xrp_market_cap = [0.006, 11, 13, 8, 43]  # Replace with actual market cap values
doge_market_cap = [0.002, 0, 0, 0, 0]  # Replace with actual market cap values
# Add more cryptocurrencies and market cap data as needed

# Plot the chart
plt.plot(years, bitcoin_market_cap, label='Bitcoin')
plt.plot(years, ethereum_market_cap, label='Ethereum')
plt.plot(years, bnb_market_cap, label='Binance Coin')
plt.plot(years, ada_market_cap, label='Cardano')
plt.plot(years, xrp_market_cap, label='XRP')
plt.plot(years, doge_market_cap, label='Dogecoin')
# Add more cryptocurrency lines as needed

# Customize the chart
plt.title('Top 10 Cryptocurrencies - Market Capitalization')
plt.xlabel('Year')
plt.ylabel('Market Cap (in billions)')
plt.legend()

# Show the chart
plt.show()
