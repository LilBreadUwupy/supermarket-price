import urllib.request
from bs4 import BeautifulSoup
import requests
import re



link = "https://www.elplazas.com/Product.php?code=10011193&suc=1013"
url = urllib.request.urlopen(link).read().decode()
soup = BeautifulSoup(url, 'lxml')

tags = soup('img')
n = 0
for tag in tags: 
    img = tag.get('src')
    img = re.findall('./[A-Z-]*/[0-9]*/img.jpg[?0-9]*', img)
    if img:
        img = img[0]
        img = "https://www.elplazas.com/" + img
        n += 1
        img_name = f"img{n}.jpg"
        r = requests.get(img).content
        with open('.' + img_name, "wb") as file:
            file.write(r)
