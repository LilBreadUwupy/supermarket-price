#! /bin/python3

from fileinput import filename
from unicodedata import category
from bs4 import BeautifulSoup
from time import sleep 
import urllib.request
import re 


def get_url(category, category_number, n):
    url = "https://gamaenlinea.com/{}/c/{}?q=%3Arelevance&page={}".format(category, category_number, n)
    
    return url


def get_href_tags(url, category):
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

    links = []

    for tag in tags:
        tag = tag.get('href')
        links.append(tag)
    
    urls = []

    for link in links:
        try:
            link = re.findall(f'/{category}/[a-zA-Z-]*/[a-zA-Z-]*/[A-Za-z0-9-]*.*', link)
            if link:
                urls.append(link)
        except TypeError:
            pass

    links.clear()

    for url in urls:
        url = 'https://gamaenlinea.com' + str(url)
        url = url.replace('[', '').replace("'", "").replace("]", "")
        links.append(url)
        
    return links


def create_file(category):
    file_directory = "/home/lilbreaduwu/Documentos/proyectos/projectfolder/test/"
    file_name = f"Excelsior-gamma-{category.lower()}.txt"
    file_data = file_directory + file_name
    file = open(file_directory + file_name, "a")
    file.write(f"Lista de enlaces en la categoría {category.lower()}")

    return file_data


def write_file(file_data, urls):
    file = open(file_data, "a")
    file.write(urls + "\n")


def list_of_page_to_range(category, categories):

    if category == categories[0]:
        r = 62
    elif category == categories[1]:
        r = 22
    elif category == categories[2]:
        r = 29
    elif category == categories[3]:
        r = 19
    elif category == categories[4]:
        r = 11
    elif category == categories[5]:
        r = 7
    elif category == categories[6]:
        r = 3
    elif category == categories[7]:
        r = 4
    else:
        r = 6
        
    return r 


def main():
    categories = ["VIVERES", "ALIMENTOS-FRESCOS", "BEBIDAS", "CUIDADO-PERSONAL", "LIMPIEZA", "HOGAR", "MASCOTAS", "OCASION", "CUIDADO-DE-LA-SALUD"]
    category_numbers = ["001", "002", "003", "004", "005", "006", "007", "008", "009"]
    index_category = 0

    for category in categories:

        print(f"Empezando a obtener enlaces de la categoría {category.lower()}...")
        sleep(5)
        file_data = create_file(category)

        category_number = category_numbers[index_category]
        r = list_of_page_to_range(category, categories)
        for n in range(r):
            
            url = get_url(category, category_number, n)
            links = get_href_tags(url, category)

            print(f"Obteniendo enlaces de {url}... ({n+1}/{r})")

            for link in links:
                write_file(file_data, link)

        index_category += 1

    print("Todos los links han sido obtenidos")


main()