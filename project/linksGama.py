#! ~/anaconda3/envs/project/bin/python

from urllib.error import URLError
from urllib.error import URLError
from bs4 import BeautifulSoup
import urllib.request
from time import sleep 
import pymysql
import re


# List of categories in https://gamaenlinea.com
CATEGORIES = ["VIVERES", "ALIMENTOS-FRESCOS", "BEBIDAS", "CUIDADO-PERSONAL", "LIMPIEZA", "HOGAR", "MASCOTAS", "OCASI%C3%93N", "CUIDADO-DE-LA-SALUD"]
CATEGORY_NUMBERS = ["001", "002", "003", "004", "005", "006", "007", "008", "011"]


def get_tags(url):
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
    return tags


def clear_tags(tags, category):
    links = []
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
        

def get_range(category):
    if category == CATEGORIES[0]:
        r = 62 #1
    elif category == CATEGORIES[1]:
        r = 22 #1
    elif category == CATEGORIES[2]:
        r = 29 #1
    elif category == CATEGORIES[3]:
        r = 19 #1
    elif category == CATEGORIES[4]:
        r = 11 #1
    elif category == CATEGORIES[5]:
        r = 7 #1
    elif category == CATEGORIES[6]:
        r = 3 #1
    elif category == CATEGORIES[7]:
        r = 4 #1
    else:
        r = 6 #1

    return r 


def open_database():
    database = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="supermarketdb"
    )
    return database


def save_to_db(db, links):
    cur = db.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS supermarketlinks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        supermarket VARCHAR(255),
        link VARCHAR(255)
        );
        """
    cur.execute(sql)

    for link in links:
        sql = "INSERT INTO supermarketlinks (supermarket,link) VALUES ('ExcelsiorGama', '%s')" % (link);    
        cur.execute(sql)
    db.commit()
    db.close()

    return "Links guardados en la base de datos"


def delete_db(db):
    cur = db.cursor()
    option = input("Puede que exista una base de datos anterior ¿Desea borrarla?(Y/n)")
    if option == "Y" or option == "y":
        print("ADVERTENCIA: Esto borrara solo los links del ExcelsiorGama")
        sleep(1)
        print("Base de datos borrada con exito")
        cur.execute("DELETE FROM supermarketlinks WHERE supermarket='ExcelsiorGama';")
        db.commit()
    else:
        pass


def run_script_and_save_data():
    index = 0
    database = open_database()
    delete_db(database)
    
    for category in CATEGORIES:

        category_number = CATEGORY_NUMBERS[index]
        r = get_range(category)
        print(f"Empezando a obtener enlaces de la categoría {category.lower()}...")

        for n in range(r):

            database = open_database()
            url = f"https://gamaenlinea.com/{category}/c/{category_number}?q=%3Arelevance&page={n}"
            print(f"Obteniendo enlaces de {url}... ({n+1}/{r})")
            tags = get_tags(url)
            links = clear_tags(tags, category)
            save_to_db(database, links)
            
        index += 1

run_script_and_save_data()