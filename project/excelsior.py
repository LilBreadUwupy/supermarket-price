#! /bin/python3

from bs4 import BeautifulSoup
import urllib.request
import re 


def iterar_url(n):
    url = "https://gamaenlinea.com/VIVERES/c/001?q=%3Arelevance&page={}".format(n)
    return url 


def get_href_tags(url):
    url = urllib.request.urlopen(url).read().decode()
    soup = BeautifulSoup(url, features="lxml")
    tags = soup("a")
    links = []
    urls = []
    for tag in tags:
        tag = tag.get('href')
        links.append(tag)
    
    for link in links:
        try:
            link = re.findall('/VIVERES/[a-zA-Z-]*/[a-zA-Z-]*/[A-Za-z0-9-]*.*', link)
            if link:
                print(link)
                urls.append(link)
        except TypeError:
            pass

    # for url in urls:
    #     url = 'https://gamaenlinea.com' + url
    #     return url 

def main():
    for n in range(62):
        url = iterar_url(n)
        get_href_tags(url)
    print("Todos los links han sido obtenidos")

main()