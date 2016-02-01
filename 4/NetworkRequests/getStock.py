from __future__ import print_function
import urllib
import json

# .read - converts data to string

htmlText = urllib.urlopen("http://www.bloomberg.com/markets/watchlist/recent-ticker/AAPL:US")

# using the json library to interpret json response text

# json.load converts file to json, but takes a file not a string
data = json.load(htmlText)
print(data)

# key is in ' ' quotes, JSON key
print(data['last_price'])

# instead of going through a full page, try to access the particular data through a network re
