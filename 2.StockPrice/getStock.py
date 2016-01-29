from __future__ import print_function
import urllib
import re
# ^ - new string, . - any character, * can be repeated
# (.+?) - I want want anything within brackets

symbolFile = open("symbols.txt")
symbolsList = symbolFile.read()
newList = symbolsList.split("\n")

for symbol in newList:
    url = "http://finance.yahoo.com/q?s=" + symbol
    htmlFile = urllib.urlopen(url)
    htmlText = htmlFile.read()
    regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmlText)
    print("Price of: ", symbol, "is ", price)
