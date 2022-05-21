CREATE DATABASE IF NOT EXISTS supermarketdb;

USE supermarketdb;

DROP TABLE supermarketlinks;

CREATE TABLE IF NOT EXISTS supermarketlinks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    supermarket VARCHAR(255),
    link VARCHAR(255)
);

INSERT INTO supermarketlinks (supermarket, link) VALUES ("Excelsiorgama", "https://gamaenlinea.com/VIVERES/Aceites-y-aderezos/Sazonadores/SALSA-DE-AJO-EXCELSIOR-GAMA-150-CC/p/10014778");