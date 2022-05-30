#! ~/anaconda3/envs/project/bin/python

from urllib.error import URLError
from bs4 import BeautifulSoup
from time import sleep 
import urllib.request
from urllib.error import URLError
import pymysql
import re 

# List of categories in https://gamaenlinea.com
CATEGORIES = ["VIVERES", "ALIMENTOS-FRESCOS", "BEBIDAS", "CUIDADO-PERSONAL", "LIMPIEZA", "HOGAR", "MASCOTAS", "OCASI%C3%93N", "CUIDADO-DE-LA-SALUD"]
CATEGORY_NUMBERS = ["001", "002", "003", "004", "005", "006", "007", "008", "011"]


def get_urls():

    index = 0
    links = []
    for category in CATEGORIES:

       category_number = CATEGORY_NUMBERS[index]
       r = get_range(category)
       index += 1
       print(f"Empezando a obtener enlaces de la categoría {category.lower()}...")
       sleep(30)

       for n in range(r):

            url = f"https://gamaenlinea.com/{category}/c/{category_number}?q=%3Arelevance&page={n}"
            print(f"Obteniendo enlaces de {url}... ({n+1}/{r})")
            connection = False

            while not connection:
                try:
                    url = urllib.request.urlopen(url).read().decode()
                    soup = BeautifulSoup(url, features="lxml")
                    tags = soup("a")
                    connection = True
                except URLError:
                    print("URLError: revise su conexión a https://gamaenlinea.com, reintentando en 20s")
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
    print("Todos los enlaces han sido obtenidos")
    return links


def save_to_db():
    print('Conectando a la base de datos...')
    db = pymysql.connect(
        host="localhost",
        user='root',
        password='',
        database='supermarketdb'
    )
    cur = db.cursor()

    if input('Puede que exista una base de datos anterior ¿Desea borrarla?(y/n)') == "Y":
        sql = "DELETE FROM supermarketlinks WHERE supermarket='ExcelsiorGama';"
        cur.execute(sql)
        print("Base de datos borrada con exito")
    else:
        return "Como existe una base de datos, se ha detido el proceso"
    
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

    return print('Todos los links han sido guardados en la base de datos con exito')


def get_range(category):
    if category == CATEGORIES[0]:
        r = 62 
    elif category == CATEGORIES[1]:
        r = 22
    elif category == CATEGORIES[2]:
        r = 29
    elif category == CATEGORIES[3]:
        r = 19
    elif category == CATEGORIES[4]:
        r = 11
    elif category == CATEGORIES[5]:
        r = 7
    elif category == CATEGORIES[6]:
        r = 3
    elif category == CATEGORIES[7]:
        r = 4
    else:
        r = 6
        
    return r 


save_to_db()