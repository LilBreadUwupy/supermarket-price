from bs4 import BeautifulSoup
import urllib.request
import re


categories = ['FRUTAS-Y-VEGETALES', 'VÍVERES', 'REFRIGERADOS-Y-CONGELADOS', 'LICORES', 'LIMPIEZA', 'CUIDADO-PERSONAL-Y-SALUD', 'MASCOTAS', 'HOGAR-Y-TEMPORADA', 'OTROS']
cat_number = [ '01', '03', '02', '06', '05', '04', '07', '08', '10']
""" Por cada categoría 'cat=01W' cambia un número"""

def get_url():
    links = []
    for n in cat_number:

        url = f"https://www.elplazas.com/Products.php?cat={n}W"
        url = urllib.request.urlopen(url).read().decode()
        soup = BeautifulSoup(url, features='lxml')
        tags = soup('a')
        for tag in tags:
            tag = tag.get('href')
            tag = re.findall('Product.php.code=[0-9]*&suc=[0-9]*', tag)
            if tag:
                tag = 'https://www.elplazas.com/' + str(tag)
                tag = tag.replace('[', '').replace("'", "").replace("]", "")
                print(tag)
            if tag not in links:
                links.append(tag)


get_url()



