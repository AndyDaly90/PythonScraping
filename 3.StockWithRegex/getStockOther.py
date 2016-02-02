from __future__ import print_function
import urllib
import re

htmlFile = urllib.urlopen("https://www.google.com/finance?q=AAPL")
htmlText = htmlFile.read()

regex = '<span id="ref_[^.]*_l">(.+?)</span>'

pattern = re.compile(regex)
result = re.findall(pattern, htmlText)
print(result)
