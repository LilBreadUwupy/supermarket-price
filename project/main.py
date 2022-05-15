from time import sleep
from requests_html import HTMLSession
from excelsior import create_file
from bs4 import BeautifulSoup
import urllib
import re 

session = HTMLSession()

def get_urls():
    urls = open('/home/lilbreaduwu/Documentos/proyectos/projectfolder/database/excelsior-gamma-database.txt')
    product_name = None
    price = None
   
    for url in urls:
        while not product_name and not price:
            #print(f"Iniciando sección en {url}")
            r = session.get(url)
            print(r)
            product_name = get_excelsior_gamma_name(r)
            price = get_excelsior_gamma_price(r)
            print(f"{product_name}: ${price}")
        

def get_excelsior_gamma_name(r):
    # Url = """
    product = r.html.find(".name", first=True)
    #product = product.text
    #product = product.lower()
    #product = re.split('id[a-z0-9]*', product)[0]
    #product = soup.find("div", {"class":"name"}).text


    return product


def get_excelsior_gamma_price(r):
    # url = ""
    # try:
    #     price = r.html.find(".from-price-value", first=True).text
    #     price = re.split('Total Ref.[0-9.]*', price)[1]
    # except AttributeError:
    #     price = None
    price = "hi"

    return price

get_urls()