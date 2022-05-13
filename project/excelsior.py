#! /bin/python3

import pickle
from bs4 import BeautifulSoup
from time import sleep 
import urllib.request
import re 

categories = ["VIVERES", "ALIMENTOS-FRESCOS", "BEBIDAS", "CUIDADO-PERSONAL", "LIMPIEZA", "HOGAR", "MASCOTAS", "OCASION", "CUIDADO-DE-LA-SALUD"]
categories_n = ["001", "002", "003", "004", "005", "006", "007", "008", "009"]


def get_href_tags(category, category_n, r):
    for n in range(r):

        url = f"https://gamaenlinea.com/{category}/c/{category_n}?q=%3Arelevance&page={n}"
        connection = False
        print(f"Obteniendo enlaces de {url}... ({n+1}/{r})")

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
            try: 
                tag = re.findall(f'/{category}/[a-zA-Z-]*/[a-zA-Z-]*/[A-Za-z0-9-]*.*', tag)

                if tag:
                    tag = 'https://gamaenlinea.com' + str(tag) + "\n"
                    tag =  tag.replace('[', '').replace("'", "").replace("]", "")
                    links.append(tag)

            except TypeError:
                pass
        
    return links


def create_file():
    index_category = 0

    for category in categories:

        file_directory = "/home/lilbreaduwu/Documentos/proyectos/projectfolder/test/"
        file_name = f"excelsior-gamma-{category.lower()}.pkl"
        file_data = file_directory + file_name
        
        
        try:
            print(f"Cargando el archivo {file_name}")
            with open(file_data, "rb") as file:
                all_links = pickle.load(file)
                #file.write(f"Lista de enlaces en la categoría {category.lower()}")
        except FileNotFoundError:
            print("Archivo no encontrado! descargando datos de internet...")
            sleep(2)
            all_links = main(category, index_category)
            index_category += 1
            with open(file_data, "wb") as file:
                # file.write(all_links)
                print(f"Escribiendo datos en {file_name}...")
                sleep(2)
                pickle.dump(all_links, file)
    
   
    print("Todos los links han sido cargados")
    return all_links


def get_range(category):

    if category == categories[0]:
        r = 2 #62
    elif category == categories[1]:
        r = 2#22
    elif category == categories[2]:
        r = 2#29
    elif category == categories[3]:
        r = 19#19
    elif category == categories[4]:
        r = 11#11
    elif category == categories[5]:
        r = 7#7
    elif category == categories[6]:
        r = 3#3
    elif category == categories[7]:
        r = 4#4
    else:
        r = 6#6
        
    return r 


def main(category, index_category):
    
    

    print(f"Empezando a obtener enlaces de la categoría {category.lower()}...")
    sleep(5)

    category_n = categories_n[index_category]
    r = get_range(category)
    links = get_href_tags(category, category_n, r)
    

    return links


create_file()