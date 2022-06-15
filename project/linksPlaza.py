from time import sleep
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import URLError
from linksGama import open_database
import re
import pymysql

# Plazas' categories list

categories = ['FRUTAS-Y-VEGETALES', 'VÍVERES', 'REFRIGERADOS-Y-CONGELADOS', 'LICORES', 'LIMPIEZA', 'CUIDADO-PERSONAL-Y-SALUD', 'GOURMET PLAZAS', 'MASCOTAS', 'HOGAR-Y-TEMPORADA', 'OTROS']
cat_number = [ '01', '03', '02', '06', '05', '04', '09', '07', '08', '10']


def get_tags(url):
    connection = False
    while not connection:
        try: 
            link = urllib.request.urlopen(url).read().decode()
            soup = BeautifulSoup(link, "lxml")
            tags = soup("a")
            connection = True
        except URLError:
            print("URLError: revise su conexión")
            sleep(20)
    
    return tags


def clear_tags(tags):
    links = []
    for tag in tags:
        tag = tag.get('href')
        tag = re.findall('Product.php.code=[0-9]*&suc=[0-9]*', tag)
        if tag:
            tag = 'https://www.elplazas.com/' + str(tag)
            tag = tag.replace('[', '').replace("'", "").replace("]", "")
            if tag not in links:
                links.append(tag)

    return links


def save_to_db(db, links):
    cur = db.cursor()

    for link in links:
        sql = "INSERT INTO supermarketlinks(supermarket,link) VALUE ('AutomercadoPlazas', '%s')" % (link);
        cur.execute(sql)
    db.commit()
    db.close()
    

def get_range(n):
    if n == cat_number[0]:
        r = 16
    elif n == cat_number[1]:
        r = 223
    elif n == cat_number[2]:
        r = 35
    elif n == cat_number[3]:
        r = 46 #Limpieza
    elif n == cat_number[4]:
        r = 39
    elif n == cat_number[5]:
        r = 71
    elif n == cat_number[6]:
        r = 2
    elif n == cat_number[7]:
        r = 10
    elif n == cat_number[8]:
        r = 29
    else: 
        r = 2

    return r 


def run_script():
    for n in cat_number:
        i = 0
        r = get_range(n)
        for page in range(1,r):
            url = f"https://www.elplazas.com/Products.php?cat={n}W&Page={page}"
            print(f"Obteniendo enlaces de {url}... ({i+1}/{r-1})")
            i += 1
            tags = get_tags(url)
            links = clear_tags(tags)
            database = open_database()
            save_to_db(database, links)
        
        print("Todos los links han sido obtenidos")
                    
    return links     

run_script()
