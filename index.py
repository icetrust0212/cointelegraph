import matplotlib.pyplot as plt
import matplotlib.dates as Dates

from data import data, years, symbols

whole_data = {}

def get_rank(array, value):
    sorted_array = sorted(array)
    return sorted_array.index(value) + 1
for coin in data:
    whole_data[coin] = []

for index in range(0, 11):
    market_data_year = []
    for coin in data:
        market_cap = data[coin][index]
        market_data_year.append(market_cap)
    
    for coin in data:
        market_cap = data[coin][index]
        rank = get_rank(market_data_year, market_cap)
        whole_data[coin].append(rank)

# Add more cryptocurrencies and market cap data as needed
plt.yscale = 0.1
# Plot the chart
for coin in whole_data:
    plt.plot(years, whole_data[coin], label=symbols[coin])

# Customize the chart
plt.title('Top 10 Cryptocurrencies - Market Capitalization')
plt.xlabel('Year')
plt.xticks(years)
plt.yticks(range(1, 11))
plt.ylabel('Rank (Market Cap)')
plt.legend()

# Show the chart
plt.show()
