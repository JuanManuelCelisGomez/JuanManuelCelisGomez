Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso 22/23)
Autor/a: Juan Manuel Celis Gómez; uvus:<juacelgom>


El proyecto tiene como objetivo analizar los datos de una plataforma de streaming. El dataset original tiene 9 columnas.

Estructura de las carpetas del proyecto:

/src: Contiene los diferentes módulos de Python que conforman el proyecto.
Netflix.py: Contiene las funciones para analizar los datos de la plataforma de streaming.
NetflixTest.py: Contiene funciones de test para probar las funciones del módulo Netflix.py. En este módulo está el main.
parsers.py: Contiene funciones de parseo de datos.

/data: Contiene el dataset o datasets del proyecto
plataforma_streaming.csv: Archivo con los datos de la plataforma de streaming que vamos a analizar.
Estructura del dataset
Cada fila del dataset recoge los datos de una plataforma de streaming en la cual disponemos de diferentes características para los productos que ofrecen. 

type: de tipo str, representa el tipo de producto que ofrece la plataforma.
tittle: de tipo str, representa el nombre del producto ofrecido.
director: de tipo str, representa el nombre del creador del producto.
country: de tipo str, representa el pais de creación del producto.
co_production: de tipo str, representa si el producto es una coproducción.
date_added: de tipo date.time, representa la fecha en la que el producto fué subido a la plataforma.
release_year: de tipo int, representa el año de lanzamiento del producto.
duration: de tipo int, representa la duración de visualización del producto.
description: de tipo str, representa la descripción del producto.

Tipos implementados
Para trabajar con los datos del dataset se ha definido la siguiente tupla con nombre:

Dats = namedtuple('Dats', 'type,title,director,country,co_production,date_added,release_year,duration,description')

en la que los tipos de cada uno de los campos son los siguientes:

Dats(str(type), str(title), str(director), str(country), str(co_production), parsea_fecha(date_added),int(release_year), int(duration), str(description))

En este proyecto se han implementado las siguientes funciones, que están clasificadas según los bloques y tipos de funciones que se requieren en cada una de las entregas. El módulo principal es el módulo Netflix.py, así que aquí es donde se hará referencia a cada uno de los bloques de las entregas.

Módulo Netflix
Entrega 1
Bloque 0
lee_fichero(fichero): lee los datos del fichero csv y devuelve una lista de tuplas de tipo Info con los datos del fichero. Para implementar esta función se han definido las siguientes funciones auxiliares en el módulo parsers:
parsea_fecha(cadena): Función para convertir de cadena a fecha.


Módulo NetflixTest
En el módulo de pruebas se han definido las siguientes funciones de pruebas, cada una de las cuales se usa para probar la función con que tiene el mismo nombre (pero sin comenzar por test\_ del módulo Netflix. Por ejemplo, la función test_abrir_ficherocsv prueba la función abrir_ficherocsv.

test_abrir_ficherocsv(fichero)

Módulo parsers
Este módulo contiene las siguientes funciones de parseo de datos:

parsea_fecha(cadena): Dada una cadena una fecha en formato dia/mes/año (%d/%m/%Y), devuelve un objeto de tipo date con la fecha a la que se refiere la cadena de entrada.