import matplotlib.pyplot as plt
import matplotlib.dates as Dates
import math
from data import data, years, symbols

whole_data = {}

def get_rank(array, value):
    sorted_array = sorted(array)
    return max(sorted_array.index(value) + 1 - len(sorted_array) + 10, 0)
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
    coin_data = []
    date = []
    flag = False
    for i in range(0, len(years)):
        if whole_data[coin][i] > 0:
            date.append(i + 2013)
            coin_data.append(whole_data[coin][i])
            flag = True
        elif flag:
            date.append(i + 2013)
            coin_data.append(whole_data[coin][i])

        
    plt.plot(date, coin_data, label=symbols[coin])

# Customize the chart
plt.title('Top 10 Cryptocurrencies - Market Capitalization')
plt.xlabel('Year')
plt.xticks(years)
plt.yticks(range(1, 11))
plt.ylabel('Rank (Market Cap)')
plt.legend(loc=5, bbox_to_anchor=(1.1, 0.5))

# Show the chart
plt.show()
