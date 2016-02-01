import urllib
import re
from bs4 import BeautifulSoup

make = raw_input("Please enter Make: ")
model = raw_input("Please enter Model: ")

htmlFile = urllib.urlopen("http://www.cbg.ie/used-cars/" + make + "/" + model + "/all/")
htmlText = htmlFile.read()

soup = BeautifulSoup(htmlText, 'html.parser')
tag = soup.find_all('div', {'class': 'ads_txt'})
for info in tag:
    if len(info.attrs) >= 1:
        print(info.contents[1].text)
        print(info.contents[3].text)
