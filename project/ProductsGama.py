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
            soup = BeautifulSoup(url, 'lxml')
            connection = True
        except URLError:
            print("URLError: reintentando en 10 segundos")
            sleep(10)
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

    product = soup.find("div", {"class":"name"})
    product = str(re.findall('name">[A-Z ÁÉÍÓÚ0-9a-záéíóúñÑ &;%-/´° #"]*<', str(product)))
    product = product.replace('[', '').replace("'", "").replace("]", "").replace('name">', "").replace('<', "").replace(".", "").replace("amp;", "").replace("&", "").lower()

    return product


def get_price(soup):

    price = soup.find("div", {"class":"from-price-value"})
    price = str(re.findall('Total Ref. ([0-9,]*)', str(price)))
    price = price.replace('[', '').replace("'", "").replace("]", "")

    return price


def create_folder(name, link):
    
    category = str(re.findall('https://gamaenlinea.com/([A-Z0-9-%]*)/', link))
    category = category.replace('[', '').replace("'", "").replace("]", "").lower()
    try:
        os.mkdir('static/img/ExcelsiorGama/' + category)
    except FileExistsError:
        pass

    name = name.replace("/", "").replace(" ", "").replace("'", "")
    try:
        os.mkdir(f'static/img/ExcelsiorGama/{category}/'  +  name)
    except FileExistsError:
        pass
    
    folder = f'static/img/ExcelsiorGama/{category}/{name}/'
    
    return folder
    


def get_img(soup, folder):
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

            img_name = f'img{n}.jpg'

            with open(folder + img_name, "wb") as file:
                file.write(r)
    
    img = folder + 'img1.jpg'

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
        exists = check_link(db, link)
        if not exists:
            soup = request_url(link)
            name = get_name(soup)
            folder = create_folder(name, link)
            img = get_img(soup, folder)
            price = get_price(soup)
            db = open_db()
            save_to_db(db, name, price, img, link )
        else:
            print("El producto ya esta en la base de datos")
        

get_links_and_run_script()
