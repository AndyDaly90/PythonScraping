from __future__ import print_function
import urllib
import json
import time

symbolsList = open("symbols.txt").read()
symbolsList = symbolsList.split("\n")

for symbol in symbolsList:                      # + means create file
    newFile = open("Prices/" + symbol + ".txt", "w+")
    newFile.close()

    htmlText = urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/" + symbol + ":US")
    data = json.load(htmlText)
    dataPoints = data["data_values"]
    lastValue = dataPoints[-1][1]
                                                # append
    newFile = open("Prices/" + symbol + ".txt", "a")

    print("Last Value for", symbol, lastValue)
    time.sleep(2)
    for point in dataPoints:
            newFile.write(str("Symbol: "+symbol+","+"Price: " + str(point[1]) + "\n"))
    newFile.close()
