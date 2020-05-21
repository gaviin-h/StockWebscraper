
import requests
from bs4 import *
import time
import csv
import lxml

# driver = webdriver.Chrome("Users/Gavin/Applications/Google\ Chrome.app")


# result = open('data.txt', 'w')

def get_tick(file):
    x = []
    for i in file:
        i = i.replace("\n", "")
        x.append(i)
    return x


def get_data(arr):  # Go through the list of tickers and get data, rests for 5 seconds after
    data = open('data.csv', 'a+', newline='')
    writer = csv.writer(data)
    # writer.writerow(["TICK", "%Change", "Prev Open", "Prev Close", "Prev Volume", "Open"]) OPTIONAL LABELS

    for j in range(0, len(arr)):
        tick = arr[j]
        url = "https://finance.yahoo.com/quote/" + tick + "/history?p=" + tick
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')

        try:
            morning_open = soup.find('span', {'data-reactid': '53'}).text
            prev_close = soup.find('span', {'data-reactid': '74'}).text
            prev_open = soup.find('span', {'data-reactid': '68'}).text
            prev_volume = soup.find('span', {'data-reactid': '78'}).text
            close = soup.find('span', {'data-reactid': '59'}).text

            morning_open = morning_open.replace(',', '')
            prev_close = prev_close.replace(',', '')
            prev_open = prev_open.replace(',', '')
            prev_volume = prev_volume.replace(',', '')
            close = close.replace(',', '')

            percent_change = ((float(close) - float(morning_open)) / float(morning_open)) * 100

            writer.writerow([tick, percent_change, prev_open, prev_close, morning_open, prev_volume])

            """ DON'T TOUCH THIS I NEED IT TO HELP PARSE THE HTML"""
            """
            price_box = soup.find_all('td', {'class': 'Py(10px) Pstart(10px)'})
            for x in price_box:
                result.writelines(str(x) + "\n")
            """

        except AttributeError:
            pass

        time.sleep(5)
    data.close()
