from bs4 import BeautifulSoup
import pymysql
from time import sleep
import urllib.request
from ssl import SSLCertVerificationError 
from urllib.error import URLError
import re


db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="supermarketdb"
    )
cur = db.cursor()


def get_price_and_name():
    
    sql = 'SELECT link FROM supermarketlinks WHERE supermarket="ExcelsiorGama";'
    cur.execute(sql)

    for url in cur.fetchall():
        link = url[0]
        print(f"Obteniendo producto de {link}")
        connection = False
        while not connection:
            try:
                url = urllib.request.urlopen(link).read().decode()
                soup = BeautifulSoup(url, 'lxml')
                connection = True
            except SSLCertVerificationError:
                print("SSLError: reintentando en 10 segundos")
                sleep(10)
            except URLError:
                print("URLError: reintentando en 10 segundos")
                sleep(10)

        # Get product with soup and cut with regex
        product = soup.find("div", {"class":"name"})
        product = str(re.findall('name">[A-ZÁÉÍÓÚ0-9a-záéíóúñÑ &%-/]*<', str(product)))
        product = product.replace('[', '').replace("'", "").replace("]", "").replace('name">', "").replace('<', "").lower()

        #Get price with soup and cut with regex
        price = soup.find("div", {"class":"from-price-value"})
        price = str(re.findall('Total Ref. ([0-9,]*)', str(price)))
        price = price.replace('[', '').replace("'", "").replace("]", "")

        #Write price and product in database 
        sql = "INSERT INTO products (product, price, supermarket, link) VALUES ('%s', '%s', 'ExcelsiorGama', '%s')" % (product, f"${price}", link );
        cur.execute(sql)
    db.commit()

get_price_and_name()
        