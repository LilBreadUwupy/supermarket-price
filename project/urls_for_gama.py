#! /bin/python3

from bs4 import BeautifulSoup
from time import sleep 
import urllib.request
import pymysql
import pickle
import re 

# List of categories in https://gamaenlinea.com
categories = ["VIVERES", "ALIMENTOS-FRESCOS", "BEBIDAS", "CUIDADO-PERSONAL", "LIMPIEZA", "HOGAR", "MASCOTAS", "OCASI%C3%93N", "CUIDADO-DE-LA-SALUD"]
categories_n = ["001", "002", "003", "004", "005", "006", "007", "008", "011"]


def get_urls():

    index = 0
    links = []

    for category in categories:
       category_n = categories_n[index]
       r = get_range(category)
       index += 1
       print(f"Empezando a obtener enlaces de la categoría {category.lower()}...")
       for n in range(r):
            url = f"https://gamaenlinea.com/{category}/c/{category_n}?q=%3Arelevance&page={n}"
            print(f"Obteniendo enlaces de {url}... ({n+1}/{r})")
            connection = False
            while not connection:
                try:
                    url = urllib.request.urlopen(url).read().decode()
                    soup = BeautifulSoup(url, features="lxml")
                    tags = soup("a")
                    connection = True
                except:
                    print("Error conexión no segura, reintentando en 20 segundos")
                    sleep(20)
            for tag in tags:
                tag = tag.get('href')
                try: 
                    tag = re.findall(f'/{category}/[A-Za-z0-9-%]*/[A-Za-z0-9-%]*/[A-Za-z0-9-%]*/p/.*', tag)
                    if tag:
                        tag = 'https://gamaenlinea.com' + str(tag)
                        tag =  tag.replace('[', '').replace("'", "").replace("]", "")
                        if tag not in links:
                            links.append(tag)
                except TypeError:
                    pass
    return links

def save_to_db():

    db = pymysql.connect(
        host="localhost",
        user='root',
        password='',
        database='supermarketdb'
    )
    cur = db.cursor()

    print(cur.execute('SHOW TABLES;'))

    sql = """CREATE TABLE IF NOT EXISTS supermarketlinks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    supermarket VARCHAR(255),
    link VARCHAR(255));"""

   
    cur.execute(sql)
    links = get_urls()
    for link in links:
        sql = "INSERT INTO supermarketlinks(supermarket,link) VALUE ('ExcelsiorGama', '%s')" % (link);
        cur.execute(sql)
    db.commit()
    db.close()

    return print('Guardado en la base de datos con exito')


def get_range(category):
    if category == categories[0]:
        r = 1#62 
    elif category == categories[1]:
        r = 1#22
    elif category == categories[2]:
        r = 1#29
    elif category == categories[3]:
        r = 1#19
    elif category == categories[4]:
        r = 1#11
    elif category == categories[5]:
        r = 1#7
    elif category == categories[6]:
        r = 1#3
    elif category == categories[7]:
        r = 1#4
    else:
        r = 1#6
        
    return r 

save_to_db()