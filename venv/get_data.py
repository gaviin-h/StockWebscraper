
import requests
from bs4 import *
import lxml

# driver = webdriver.Chrome("Users/Gavin/Applications/Google\ Chrome.app")

# Put all the tickers into a list


def get_tick(file):
    for i in file:
        i = i.replace("\n", "")
        x = []
        x.append(i)
        return x


def get_data(arr):  # Go through the list of tickers and get data
    for j in range(0, len(arr)):
        tick = arr[j]
        result = open("data", "w")

        url = "https://finance.yahoo.com/quote/" + tick + "?p=&.tsrc=fin-srch"
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'lxml')

        price_box = soup.find('span', {'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'})
        price = price_box.text

        result.write(tick + " " + price)

        # open the html || should use helper methods

        # analyse the html and push the data to a new txt file called data.txt
