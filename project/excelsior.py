#! /bin/python3

import pickle
from bs4 import BeautifulSoup
from time import sleep 
import urllib.request
import re 

categories = ["VIVERES", "ALIMENTOS-FRESCOS", "BEBIDAS", "CUIDADO-PERSONAL", "LIMPIEZA", "HOGAR", "MASCOTAS", "OCASI%C3%93N", "CUIDADO-DE-LA-SALUD"]
categories_n = ["001", "002", "003", "004", "005", "006", "007", "008", "011"]


def get_href_tags(category, category_n, r):

    links = []
    print(f"Empezando a obtener enlaces de la categoría {category.lower()}...")
    
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

        for tag in tags:
            tag = tag.get('href')
            try: 
                tag = re.findall(f'/{category}/[A-Za-z0-9-%]*/[A-Za-z0-9-%]*/[A-Za-z0-9-%]*/p/.*', tag)
                if tag:
                    tag = 'https://gamaenlinea.com' + str(tag) + "\n"
                    tag =  tag.replace('[', '').replace("'", "").replace("]", "")
                    links.append(tag)

            except TypeError:
                pass
        
    return links


def create_file():
    index_category = 0
    all_links = False
    file_name = 'excelsior-gamma-database.pkl' 
    file_directory = "/home/lilbreaduwu/Documentos/proyectos/projectfolder/database/"
    file_data = file_directory + file_name

    try:
        print(f"Cargando el archivo {file_name}")
        with open(file_data, "rb") as file:
                all_links = pickle.load(file)
    except FileNotFoundError:
        print("Archivo no encontrado! descargando datos de internet...")
        for category in categories:

            category_n = categories_n[index_category]
            r = get_range(category)
            sleep(2)

            all_links = get_href_tags(category, category_n, r)

           

            with open(file_data, "ab") as file:
                #file.write(f"Categoría: {category}\n")
                print(f"Escribiendo datos en {file_name}...")
                pickle.dump(all_links, file)
                #for link in all_links:
                    #file.write(link)
            index_category += 1


    print("Todos los links han sido cargados")

    return all_links


def get_range(category):

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
        r = 6#6
        
    return r 