# Supermarket Price

## Sobre el proyecto 

Supermarket-price es una aplicación web en desarrollo cuyo objetivo es almacenar productos
de distintos supermercados venezolanos y ofrecerle al usuario una guía/tabla comparando el precio del producto. 

## Planes de ejecución 

Hoy mayo de 2022 el proyecto lleva 5 días de desarrollo, solo se ha conseguido extraer los links mediantes python, usando lás librerías bs4 y html_requests iterando cada link obtenido mediante regex y almacenandolo en un archivo de prueba 

El objetivo es lograr obtener los productos de cada uno de los supermercados mediante bs4 y htmlrequest, obteniendo a su vez el nombre y precio en dólares para almacenarlo en una base de datos SQL

Una vez logrado el backend, con uso de Javascript o Flask se busca montar la aplicación web para finalmente darle vida con html y css 

## Duración del proyecto

No existe una fecha estimada para la culminación del proyecto, debido a falta de aprendizaje en ciertas areas puede demorar más tiempo de lo que tardaría otra persona

# Archivos del proyecto 

## Carpeta project

### Excelsior.py

Excelsior.py obtiene todos los elementos del sitio web de Gamma express, devolviendolo un conjunto de archivos con todos los links obtenidos

#### Import 

En excelsior.py importamos bs4 y urllib request para poder obtener la url, decodificarla y pasarsela a BS4

#### Get href tag()

La función más importante de este archivo es get_href_tag, allí decodificaremos y le pasaremos el url de la lista de productos del gamma (en la cual varía solo la categoría)

`
 url = urllib.request.urlopen(url).read().decode()
            soup = BeautifulSoup(url, features="lxml")
            tags = soup("a")
            `

Dentro de la misma función itenaremos todos los href de la etiqueta "a" hasta que nos retorne una lista con todos los links obtenidos los cuales más adelante guardaremos en un archivo dentro de la función main

#### main()

La función main en excelsior.py crea un bucle for por cada categoría existente en la página del gamma, las categorías se encuentran en una lista creada manualmente que solo se puede modificar desde el código

por cada una de estas categorías obtendremos un archivo y escribiremos uno a uno los links sobre ellos usando la función write_file()

para ayudar al proceso de desarrollo se imprimen mensajes en la terminal indicando en que categoría estamos y cuantas páginas de esa misma categoría faltan por obtener
