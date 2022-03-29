import statistics
import time

import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

price_history = []
time_lst = []

print('\n__________Bitcoin Data Collector__________\n')
user_input = int(input('How long would you like to run the program in minutes?: '))
for _ in range(user_input):
    result = requests.get('https://coinmarketcap.com/')
    soup = BeautifulSoup(result.text,'html.parser')
    span_tags = soup.find_all('span',class_ = 'sc-1eb5slv-0 jWIOUU')
    btc_price = (span_tags[-2].contents[0])
    btc_price = btc_price.replace(',','')
    price_history.append(float(btc_price[1:]))
    time_lst.append(time.strftime('%H:%M'))
    print('Retrieved BTC Price: ',btc_price)
    time.sleep(60)
print('Prices: ',price_history)
print('Relative Change:  $',round(((price_history[-1]-price_history[0])/price_history[0])*100,2))
print('Mean: ',statistics.mean(price_history))
print('Median: ',statistics.median(price_history))
print('Standard Deviation: ',statistics.stdev(price_history))
print('Variance: ',statistics.variance(price_history))
plt.plot(time_lst,price_history,color = 'red', marker = 'o')
plt.title('BTC Prices In Minute Intervals',fontsize = 14)
plt.xlabel('Time',fontsize=14)
plt.ylabel('BTC Prices',fontsize=14)
plt.grid = True
plt.show()