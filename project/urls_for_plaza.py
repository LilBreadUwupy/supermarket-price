from time import sleep
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import URLError
import re
import pymysql


categories = ['FRUTAS-Y-VEGETALES', 'VÍVERES', 'REFRIGERADOS-Y-CONGELADOS', 'LICORES', 'LIMPIEZA', 'CUIDADO-PERSONAL-Y-SALUD', 'MASCOTAS', 'HOGAR-Y-TEMPORADA', 'OTROS']
cat_number = [ '01', '03', '02', '06', '05', '04', '07', '08', '10']
""" Por cada categoría 'cat=01W' cambia un número"""

def get_url():
    links = []
    for n in cat_number:
        i = 0
        r = get_range(n)
        for page in range(1,r):
            url = f"https://www.elplazas.com/Products.php?cat={n}W&Page={page}"
            print(f"Obteniendo enlaces de {url}... ({i+1}/{r-1})")
            i += 1
            connection = False

            while not connection:
                try:
                    url = urllib.request.urlopen(url).read().decode()
                    soup = BeautifulSoup(url, features='lxml')
                    tags = soup('a')
                    connection = True
                except URLError:
                    print('URlError: reintentando en 10 segundos')
                    sleep(10)
                    
            for tag in tags:
                tag = tag.get('href')
                tag = re.findall('Product.php.code=[0-9]*&suc=[0-9]*', tag)
                if tag:
                    tag = 'https://www.elplazas.com/' + str(tag)
                    tag = tag.replace('[', '').replace("'", "").replace("]", "")
                if tag not in links:
                    links.append(tag)

    return links     


def get_range(n):
    if n == cat_number[0]:
        r = 17
    elif n == cat_number[1]:
        r = 212
    elif n == cat_number[2]:
        r = 34
    elif n == cat_number[3]:
        r = 47
    elif n == cat_number[4]:
        r = 39
    elif n == cat_number[5]:
        r = 66
    elif n == cat_number[6]:
        r = 10
    elif n == cat_number[7]:
        r = 26
    else: 
        r = 1

    return r 


def save_to_db():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="supermarketdb"
    )
    cur = db.cursor()
    
    links = get_url()

    for link in links:
        sql = "INSERT INTO supermarketlinks(supermarket,link) VALUE ('AutomercadoPlazas', '%s')" % (link);
        cur.execute(sql)
    db.commit()
    db.close()
    
    return print("Todos los links han sido guardados en la base de datos")


