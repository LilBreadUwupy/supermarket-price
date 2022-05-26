CREATE DATABASE IF NOT EXISTS supermarketdb;

USE supermarketdb;

DROP TABLE supermarketlinks;

CREATE TABLE IF NOT EXISTS supermarketlinks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    supermarket VARCHAR(255),
    link VARCHAR(255)
);

INSERT INTO supermarketlinks (supermarket, link) VALUES ("Excelsiorgama", "https://gamaenlinea.com/VIVERES/Aceites-y-aderezos/Sazonadores/SALSA-DE-AJO-EXCELSIOR-GAMA-150-CC/p/10014778");

SELECT * FROM supermarketlinks WHERE supermarket="ExcelsiorGama";

DROP TABLE IF EXISTS products;
DELETE FROM supermarketlinks WHERE supermarket="ExcelsiorGama";

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(255),
    price VARCHAR(255),
    img LONGBLOB,
    supermarket VARCHAR(255),
    link VARCHAR(255)
);

INSERT INTO products(img) SEL

INSERT INTO products (product, price, supermarket, link) VALUES ("Jamón", "$5", "ExcelsiorGama", "https://gamaenlinea.com/VIVERES/Aceites-y-aderezos/Sazonadores/SALSA-DE-AJO");