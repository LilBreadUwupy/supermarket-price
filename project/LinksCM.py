from bs4 import BeautifulSoup
import urllib.request 
import pymysql
import re


branch_offices = ["Av-Presidente-Medina-02", "Plaza-Las-Americas-03", "Los_Ruices_04", "Chacaito-07", "Bello-Monte-08", "La-Boyera-18", "altos-mirandinos-23", "Montalban-25", "Bello-Campo-43", "La-Lagunita-44", "el-marques-09", "La-Alameda-50", "Manzanares_52", "la-guaira-53"]
categories = ['viveres', 'refrigerados', 'fruteria-y-vegetales', 'cuidado-personal', "articulos-de-limpieza", "licores", "hogar-temporada"]

def request_url():
    url = "https://tucentralonline.com/la-guaira-53/comprar/viveres/"
    url = urllib.request.urlopen(url).read().decode()
    soup = BeautifulSoup(url, 'lxml')
    tags = soup('a')
    for tag in tags:
        tag.get('href')
        print(tag)



request_url()