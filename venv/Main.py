# lets get some stock info!

import requests
import bs4 as bs

# get the tickers names
file = open("Tickers.txt", "r")
x = []
# driver = webdriver.Chrome("Users/Gavin/Applications/Google\ Chrome.app")

# Put all the tickers into a list
for i in file:
    i = i.replace("\n", "")
    x.append(i)

get_data(x)


def get_data(arr):  # Go through the list of tickers and get data
    for j in range(0, len(x)):
        tick = arr[j]
        url = "https://finance.yahoo.com/quote/" + tick + "?p=&.tsrc=fin-srch"
        data = requests.get(url).text
        soup = bs(data.text, 'html.parser')
        mydivs = soup.findAll('span', {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
        print(mydivs)


# open the html

# parse the html for prices

# run an algorithm to find the hottest stock

# store the info to the text file
