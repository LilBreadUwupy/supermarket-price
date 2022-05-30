from urls_for_gama import get_urls
import pymysql

conn = pymysql.connect(host='localhost', user= 'root', password='')
cur = conn.cursor()
cur.execute('USE supermarketdb')

links = get_urls()

for link in links:
    print(link)
    cur.execute('INSERT INTO supermarketlinks (supermarket, link) VALUES ("Excelsiorgama", %s);', (link))
    print('Guardando link en la base de datos...')
