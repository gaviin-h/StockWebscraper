
import requests
from bs4 import *
import time
import lxml

# driver = webdriver.Chrome("Users/Gavin/Applications/Google\ Chrome.app")

# Put all the tickers into a list
result = open("data", "w")


def get_tick(file):
    x = []
    for i in file:
        i = i.replace("\n", "")
        x.append(i)
    return x


def get_data(arr):  # Go through the list of tickers and get data, rests for 5 seconds after
    for j in range(0, len(arr)):
        tick = arr[j]
        url = "https://finance.yahoo.com/quote/" + tick + "?p=&.tsrc=fin-srch"
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'lxml')

        price_box = soup.find('span', {'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'})
        price = price_box.text
        price_change = soup.find('span', {'data-reactid': '16'})
        change = price_change.text

        result.write(tick + ' ' + price + ' ' + change + '\n')

        """ DONT TOUCH THIS I NEED IT TO HELP PARSE THE HTML"""
        """price_box = soup.find_all('span')
        for x in price_box:
            result.writelines(str(x) + "\n")"""

        time.sleep(5)

        # open the html || should use helper methods

        # analyse the html and push the data to a new txt file called data.txt
