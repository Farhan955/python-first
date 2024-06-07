import re

import requests
from bs4 import BeautifulSoup

url = "https://samfatech.com/projects/"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")


tag = soup.div.ul
attributes=tag.attrs #it is key value based

# find the data according to tag and class, it returns only first
title = soup.find("span", class_="elementor-icon-list-text")

#find data array according to tag and class
titles = soup.findAll("span", class_="elementor-icon-list-text")

#find dedata in basis of matching string and gives array
titles = soup.findAll(string=re.compile("Development"))

print(titles)
s = input("okkk?")

