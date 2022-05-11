#! /bin/python3
from bs4 import BeautifulSoup
import urllib.request
import re 

url = "https://gamaenlinea.com/VIVERES/c/001?q=%3Arelevance&page=0"
url = urllib.request.urlopen(url).read().decode()


def get_href_tags():
    soup = BeautifulSoup(url, features="lxml")
    tags = soup("a")
    links = []

    for tag in tags:
        tag = tag.get('href')
        links.append(tag)
        
    
    for link in links:
        try:
            print(re.findall('/VIVERES/[a-zA-Z-]*/[a-zA-Z-]*/[A-Za-z0-9-]*.*', link))
        except TypeError:
            print("NoneType")
    

    


get_href_tags()