# lets get some stock info!

from get_data import *


file = open("Tickers.txt", "r")

# run an algorithm to find the hottest stock

get_data(get_tick(file))
file.close()

# store the info to the text file
