from turtle import width
from bs4 import BeautifulSoup
import urllib.request
import os
import pymysql
from PIL import Image
import requests 

url = input("url: ")
url = urllib.request.urlopen(url).read().decode()
soup = BeautifulSoup(url, 'lxml')
tags = soup('img')
for tag in tags:
    img = tag.get('data-src')
    i = 0
    if img:
        img = "https://gamaenlinea.com/" + img 
        i+=1
        r = requests.get(img).content
        
        with open(f'test/img{i}.jpg', "wb+") as f:
            f.write(r)
    
file = 'test/img1.jpg'

db = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='supermarketdb'
)
cur = db.cursor()
sql = 'INSERT INTO products (img) VALUES ("%s")' % r
cur.execute(sql)
db.commit()
  

# sql = "SELECT img FROM products"
# cur.execute(sql)
# img = cur.fetchall()
# print(img)