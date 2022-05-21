import pymysql

conn = pymysql.connect( host='localhost', user='root', password='')
cur = conn.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS supermarketdb')
