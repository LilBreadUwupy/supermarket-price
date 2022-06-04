import os
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
            soup = BeautifulSoup(url, "lxml")
            connection = True
        except URLError:
            print("URLError: revise su conexión")
            sleep(20)

    return soup


def check_link(db, link):
    cur = db.cursor()
    sql = "SELECT COUNT(*) FROM products WHERE link='%s'" % link ;
    cur.execute(sql)
    exists = cur.fetchall()
    exists = exists[0][0]
    if exists > 0:
        return True
    else: 
        return False


def get_name(soup):
    product = str(soup.find("div", {"class":"ProductName"}))
    product = product.replace('<div class="ProductName">', '').replace('</div>', '').replace('(UN)', '').replace('\n', '').replace("    ", "").replace("\r", "").lower()

    return product


def get_price(soup):

    price = soup.find("div", {"class":"ProductPrice"})
    price = re.findall('[0-9.]*', str(price))
    price = price[66]

    return price


def get_img(soup, name):

    tags = soup('img')
    for tag in tags:

        img = tag.get('src')
        img = re.findall('./[A-Z-]*/[0-9]*/[A-Za-z0-9]*.jpg[?0-9]*', img)

        if img:
            
            img_name = name.replace(' ', "").replace('/', "").replace("\t", "").replace(",", "")
            img_name = img_name + '.jpg'
            img = "https://www.elplazas.com/" + img[0]
            folder = f"static/img/AutomercadoPlazas/{img_name}"
            connection = False

            while not connection:
                try:
                    r = requests.get(img).content
                    connection = True
                except Exception:
                    print('SSLError: reintentado en 20 segundos')
                    sleep(20)
            with open(folder, "wb") as file:
                file.write(r)
            
            return folder


def save_to_db(db, name, price, img, link):
    cur = db.cursor()
    sql = "INSERT INTO products (product, price, img, supermarket, link) VALUES ('%s', '%s', '%s', 'AutomercadoPlazas', '%s')" % (name, f"Bs{price}", img, link);
    cur.execute(sql)
    db.commit()


def run_script():
    db = open_db()
    cur = db.cursor()
    sql = 'SELECT link FROM supermarketlinks WHERE supermarket="AutomercadoPlazas";'
    cur.execute(sql)
    urls, n = cur.fetchall(), 0
    for url in urls:
        n += 1
        print(f'Obteniendo productos ({n}/{len(urls)})')
        link = url[0]
        exists = check_link(db, link)
        if not exists:
            soup = request_url(link)
            name = get_name(soup)
            price = get_price(soup)
            img = get_img(soup, name)
            db = open_db()
            save_to_db(db, name, price, img, link)
        else: 
            print("El producto ya existe en la base de datos")


run_script()