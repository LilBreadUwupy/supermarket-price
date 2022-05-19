from bs4 import BeautifulSoup
from urls_for_gama import create_file
from time import sleep
import urllib.request
from ssl import SSLCertVerificationError 
from urllib.error import URLError
import re

list_urls = create_file()


product_info = {

    'supermarket': 'Excelsior gamma',
    'ID': '',
    'Link' : '',
    'Product' : '',
    'Price' : ''

    }   

product_data = {
        'Gama express': ''
    }

def get_price_and_name():
    id = 1
    lost_links = 0
    #Itera urls
    for urls in list_urls:
        for url in urls:
            print(f'Obteniendo producto en {url}...({id}/{len(urls)})')
            new_product = product_info.copy()
            new_product['Link'] = url.replace('\n', '')
            new_product['ID'] = id
            connection = False

            while not connection:
                try:
                    url = urllib.request.urlopen(url).read().decode()
                    soup = BeautifulSoup(url, 'lxml')
                    connection = True
                except SSLCertVerificationError:
                    print("SSLCertVerificationError: reintentando en 20 segundos")
                    sleep(20)
                except URLError:
                    print("URLError: reintentando en 10 segundos")
                    sleep(10)
                    #lost_links += 1

            # Get product with soup and cut with regex
            product = soup.find("div", {"class":"name"})
            product = str(re.findall('name">[A-ZÁÉÍÓÚ0-9a-záéíóúñÑ %-/]*<', str(product)))
            new_product['Product'] = product.replace('[', '').replace("'", "").replace("]", "").replace('name">', "").replace('<', "").lower()

            #Get price with soup and cut with regex
            price = soup.find("div", {"class":"from-price-value"})
            price = str(re.findall('Total Ref. ([0-9,]*)', str(price)))
            new_product["Price"] = price.replace('[', '').replace("'", "").replace("]", "")

            id += 1
            product_data['Gama express'] = new_product 
            with open('Prueba2.txt', 'a') as file:
                file.write(str(new_product) + '\n')

            for r in range(1,11):
                if str(id) == f'{r}00': 
                    print('Durmiendo 60 segundos antes de continuar')
                    sleep(60)

    print(f"Base de datos obtenida, se perdieron{lost_links} durante el proceso creando archivo...")
    

get_price_and_name()
