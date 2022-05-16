from bs4 import BeautifulSoup
from urls_for_gama import create_file
import urllib
import re


urls = create_file()
repeat_urls = []

product_info = {
    'Supermarket-Gama': {
        'Product': 'Salsa',
        'Price' : '1.7',
        'Link' : 'https://gamaenlinea.com/VIVERES/Aceites-y-aderezos/Sazonadores/SALSA-DE-AJO-EXCELSIOR-GAMA-150-CC/p/10014778',
        'ID' : '001'
    }   
}

def get_price_and_name():

    #Itera urls
    for url in urls:
        repeat_urls.append(url)
        url = urllib.request.urlopen(url).read().decode()
        soup = BeautifulSoup(url, 'lxml')

        # Get product with soup and cut with regex
        product = soup.find("div", {"class":"name"})
        product = str(re.findall('name">[A-Z0-9a-z /  %-]*<', str(product)))
        product = product.replace('[', '').replace("'", "").replace("]", "").replace('name">', "").replace('<', "").lower()

        #Get price with soup and cut with regex
        price = soup.find("div", {"class":"from-price-value"})
        price = str(re.findall('Total Ref. ([0-9,]*)', str(price)))
        price = price.replace('[', '').replace("'", "").replace("]", "")

            
        print(f"Producto: {product} precio: ${price}")

