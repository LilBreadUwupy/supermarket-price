import os
from unicodedata import name
from bs4 import BeautifulSoup
import pymysql
from time import sleep
import urllib.request
import requests 
from ssl import SSLCertVerificationError 
from requests.exceptions import SSLError
from urllib.error import URLError
import re


def open_db():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="supermarketdb"
    )
    return db


def request_url(link):
    connection = False
    while not connection:
        try:
            url = urllib.request.urlopen(link).read().decode()
            soup = BeautifulSoup(url, 'lxml')
            connection = True
        except URLError:
            print("URLError: reintentando en 10 segundos")
            sleep(10)
    return soup


def get_name(soup):

    product = soup.find("div", {"class":"name"})
    product = str(re.findall('name">[A-ZÁÉÍÓÚ0-9a-záéíóúñÑ &%-/]*<', str(product)))
    product = product.replace('[', '').replace("'", "").replace("]", "").replace('name">', "").replace('<', "").lower()

    return product


def get_price(soup):

    price = soup.find("div", {"class":"from-price-value"})
    price = str(re.findall('Total Ref. ([0-9,]*)', str(price)))
    price = price.replace('[', '').replace("'", "").replace("]", "")

    return price


def get_img(soup, name):
    tags = soup('img')
    n = 0 
    for tag in tags:
        img = tag.get('data-src')
        if img:
            n += 1
            img = "https://gamaenlinea.com/" + img 
            connection = False
            while not connection:
                try:
                    r = requests.get(img).content
                    connection = True
                except Exception:
                    print('SSLError: reintentado en 20 segundos')
                    sleep(20)

            name = name.replace('/', '').replace(' ', '\\')

            try:
                os.mkdir('static/img/ExcelsiorGama/' + name)
            except FileExistsError:
                pass 

            file_directory = f'static/img/ExcelsiorGama/{name}/'
            name_img = f'img{n}.jpg'

            with open(file_directory + name_img, "wb") as file:
                file.write(r)
    
    img = file_directory + 'img1.jpg'

    return img


def save_to_db(db, name, price, img, link):
    cur = db.cursor()
    sql = "INSERT INTO products (product, price, img, supermarket, link) VALUES ('%s', '%s', '%s', 'ExcelsiorGama', '%s')" % (name, f"${price}", img,  link );
    cur.execute(sql)
    db.commit()


def get_links_and_run_script():
    db = open_db()
    cur = db.cursor()
    sql = 'SELECT link FROM supermarketlinks WHERE supermarket="ExcelsiorGama";'
    cur.execute(sql)
    urls = cur.fetchall()
    n = 0
    for url in urls:
        n += 1
        print(f'Obteniendo productos ({n}/{len(urls)})')
        link = url[0]
        soup = request_url(link)
        name = get_name(soup)
        img = get_img(soup, name)
        price = get_price(soup)
        db = open_db()
        save_to_db(db, name, price, img, link )
        

get_links_and_run_script()
# soup = request_url('https://gamaenlinea.com/ALIMENTOS-FRESCOS/Carnes/Pollo/POLLO-A-LA-BRASA-1-UN/p/28002125')
# name = get_name(soup)
# print(get_img(soup, name))
