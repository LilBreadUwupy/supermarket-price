#! /bin/python3

from os import link
from bs4 import BeautifulSoup
from time import sleep 
import urllib.request
import pickle
import re 

# List of categories in https://gamaenlinea.com
categories = ["VIVERES", "ALIMENTOS-FRESCOS", "BEBIDAS", "CUIDADO-PERSONAL", "LIMPIEZA", "HOGAR", "MASCOTAS", "OCASI%C3%93N", "CUIDADO-DE-LA-SALUD"]
categories_n = ["001", "002", "003", "004", "005", "006", "007", "008", "011"]


def get_urls(category, category_n, r):

    links = []
    print(f"Empezando a obtener enlaces de la categoría {category.lower()}...")
    sleep(30)
    
    for n in range(r):
        # Create a url 
        url = f"https://gamaenlinea.com/{category}/c/{category_n}?q=%3Arelevance&page={n}"
        print(f"Obteniendo enlaces de {url}... ({n+1}/{r})")

        # Check url
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

        # Iterar urls in tags
        for tag in tags:
            tag = tag.get('href')
            try: 
                # Cut tag with regex
                tag = re.findall(f'/{category}/[A-Za-z0-9-%]*/[A-Za-z0-9-%]*/[A-Za-z0-9-%]*/p/.*', tag)
                if tag:
                    # Create a link clickeable
                    tag = 'https://gamaenlinea.com' + str(tag) + "\n"
                    tag =  tag.replace('[', '').replace("'", "").replace("]", "")
                    # Check if the link not exist
                    if tag not in links:
                        links.append(tag)
            except TypeError:
                pass
    return links

def create_file():

    # Declare variables
    index_category = 0
    links = False
    all_links = []

    # File data
    file_name = 'excelsior-gama-database.pkl' 
    file_directory = "/home/lilbreaduwu/Documentos/proyectos/projectfolder/database/"
    file_data = file_directory + file_name

    # Try load the file
    try:
        print(f"Cargando el archivo {file_name}")
        with open(file_data, "rb") as file:
                all_links = pickle.load(file)
    # If NotFoundError create a file
    except FileNotFoundError:
        print("Archivo no encontrado! descargando datos de internet...")

        # Get url for category in https://gamaenlinea.com
        for category in categories:
            #Declare variables to get_url function
            category_n = categories_n[index_category]
            r = get_range(category)
            sleep(2)

            # Call get_urls 
            links = get_urls(category, category_n, r)
            all_links.append(links)
            # Pass to next category
            index_category += 1

            # Open file and write links inside
       
        with open(file_data, "ab") as file:
            print(f"Escribiendo datos en {file_name}...")
            pickle.dump(all_links, file)
        

    # Exit
    print("Todos los links han sido cargados")
    return all_links


def get_range(category):

    # Get range for category

    if category == categories[0]:
        r = 62#62 
    elif category == categories[1]:
        r = 22#22
    elif category == categories[2]:
        r = 29#29
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