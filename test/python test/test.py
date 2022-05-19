#! /bin/python3

from ast import Try
from os import link
import pickle
from unicodedata import category
from bs4 import BeautifulSoup
from time import sleep 
import urllib.request
import re 
url = f"https://gamaenlinea.com/VIVERES/c/001?q=%3Arelevance&page=0"
url = urllib.request.urlopen(url).read().decode()
soup = BeautifulSoup(url, features="lxml")
tags = soup("a")

links = []
for tag in tags:
        tag = tag.get('href') 
        
        try:
            tag = re.findall(f'//[A-Za-z0-9-]*/[A-Za-z0-9-]*/[A-Za-z0-9-]*/p/.*', tag)
            if tag:
                tag = 'https://gamaenlinea.com' + str(tag)
                tag =  tag.replace('[', '').replace("'", "").replace("]", "")
                links.append(tag)
        except TypeError:
                pass

print(links)
print(type(links))
