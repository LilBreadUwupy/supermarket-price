from urllib.error import URLError
from urllib.error import URLError
from bs4 import BeautifulSoup
import urllib.request
from time import sleep 
import pymysql
import re

#  Gama's categories list

CATEGORIES = ["VIVERES", "ALIMENTOS-FRESCOS", "BEBIDAS", "CUIDADO-PERSONAL", "LIMPIEZA", "HOGAR", "MASCOTAS", "OCASI%C3%93N", "CUIDADO-DE-LA-SALUD"]
CATEGORY_NUMBERS = ["001", "002", "003", "004", "005", "006", "007", "008", "011"]


def get_tags(url):

    """
    Function:
        Send a request to url and get the tags in the html

    Args: 
        url (String): link of one Excelsior gama's category

    Returns: 
        tags (list): list with tags 'a'

    """

    connection = False
    while not connection:
        try:
            url = urllib.request.urlopen(url).read().decode()
            soup = BeautifulSoup(url, features="lxml")
            tags = soup("a")
            connection = True
        except URLError:
            print("URLError: revise su conexión, reintentando en 20s")
            sleep(20)
    return tags


def clear_tags(tags, category):

    """
    Function:
        Create a list links, get tag 'href' and add all links that point to a product

    Args:
        tags (list): list with tags 'a'
        category (string): The name of the actual excelsior gama's  category

    Returns: 
        links (list): Gama's product link list
    """

    links = []
    for tag in tags:
        tag = tag.get('href')
        try: 
            tag = re.findall(f'/{category}/[A-Za-z0-9-%]*/[A-Za-z0-9-%]*/[A-Za-z0-9-%]*/p/.*', tag)
            if tag:
                tag = 'https://gamaenlinea.com' + str(tag)
                tag =  tag.replace('[', '').replace("'", "").replace("]", "")
                if tag not in links:
                    links.append(tag)
        except TypeError:
            pass
    return links
        

def get_range(category):

    """
    Function:
        Compare the current category to know the number of pages to iterate
    
    Args:
        category (string): The name of the actual excelsior gama's category

    Returns:
        range (int): range to iterate the category
    """

    if category == CATEGORIES[0]:
        range = 62 #1
    elif category == CATEGORIES[1]:
        range = 22 #1
    elif category == CATEGORIES[2]:
        range = 29 #1
    elif category == CATEGORIES[3]:
        range = 19 #1
    elif category == CATEGORIES[4]:
        range = 11 #1
    elif category == CATEGORIES[5]:
        range = 7 #1
    elif category == CATEGORIES[6]:
        range = 3 #1
    elif category == CATEGORIES[7]:
        range = 4 #1
    else:
        range = 6 #1

    return range


def open_database():

    """
    Function:
        Open mysql database using pymysql
    
    Returns: 
        database: database connection

    """

    database = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="supermarketdb"
    )
    return database


def save_to_db(db, links):
    
    """
    Function:
        Insert links in database
    
    Args:
        db: database connection
        links (list): Gama's product link list
    
    Returns:
        info
    """

    cur = db.cursor()

    for link in links:
        sql = "INSERT INTO supermarketlinks (supermarket,link) VALUES ('ExcelsiorGama', '%s')" % (link);    
        cur.execute(sql)
    db.commit()
    db.close()

    return "Links guardados en la base de datos"


def delete_db(db):

    """
    Function:
        Ask the user if he wants to delete the db 

    Args:
        db: database connection
    """

    cur = db.cursor()
    option = input("Puede que exista una base de datos anterior ¿Desea borrarla?(Y/n)")
    if option == "Y" or option == "y":
        print("ADVERTENCIA: Esto borrara solo los links del ExcelsiorGama")
        sleep(1)
        print("Base de datos borrada con exito")
        cur.execute("DELETE FROM supermarketlinks WHERE supermarket='ExcelsiorGama';")
        db.commit()
    else:
        pass


def run_script_and_save_data():

    """
    Function:
    
        Declare a variable index, open the 
        database using the open_database() function
        iterate each category in categories
        Gets the range for the following for.

        Inside the following for loop, open 
        the database again modify a str to get 
        the correct link and using the above 
        functions get the links to Gama's products
        At the end add one to the variable index
    
    """

    index = 0
    database = open_database()
    delete_db(database)
    
    for category in CATEGORIES:

        category_number = CATEGORY_NUMBERS[index]
        r = get_range(category)
        print(f"Empezando a obtener enlaces de la categoría {category.lower()}...")

        for n in range(r):

            database = open_database()
            url = f"https://gamaenlinea.com/{category}/c/{category_number}?q=%3Arelevance&page={n}"
            print(f"Obteniendo enlaces de {url}... ({n+1}/{r})")
            tags = get_tags(url)
            links = clear_tags(tags, category)
            save_to_db(database, links)
            
        index += 1


if __name__ == "__main__":
    run_script_and_save_data()