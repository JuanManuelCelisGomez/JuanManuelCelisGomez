# -*- coding: utf-8 -*-

''' Este módulo contiene las funciones principales que decriben el programa'''

import csv
from collections import namedtuple
from Parsers import *
from datetime import datetime 
import statistics


''' 
------------------------------------Entregra 1------------------------------------------------------------
La primera entrega contiene una función de apertura de fichero csv
'''

Dats = namedtuple('Dats', 'type,title,director,country,co_production,date_added,release_year,duration,description')

def abrir_ficherocsv (fichero):
    '''
    @param fichero: fichero contiene los datos del csv
    @type: str, parseo de fecha(date.time), int
    @return: Una tupla con todos los datos del csv plataforma_streaming.csv
    '''
    with open (fichero, encoding='utf-8') as f:

        lector = csv.reader(f, delimiter= ";")
        next(lector)
        res=[]
        for type, title, director, country, co_production, date_added, release_year, duration, description in lector:

            tupla = Dats(str(type), str(title), str(director), str(country), str(co_production), parsea_fecha(date_added),\
                 int(release_year), int(duration), str(description))
            res.append(tupla)
    return res



''' 
------------------------------------Entregra 2------------------------------------------------------------

'''

def Peliculas_añolanzamiento(registros,type='Movie',release_year='2020'):
    '''
    Devuelve una lista de tuplas con las peliculas del año 2020.
    @param registros:  lista de tuplas con los datos de una plataforma de streaming
    @param type: Tipo de contenido por el que se van a filtrar los registros.
    @type type: str  
    @param release_year: Año de lanzamiento del contenido.
    @type release_year: int
    @return: Lista de tuplas con las peliculas del año 2020.
    '''
    res = [t for t in registros if t.type==type and t.release_year==release_year]
    return res


def calcula_media_añolanzamiento(registros):
    '''
    @param registros:  lista de tuplas con los datos de una plataforma de streaming
    @return: La media de los años de lanzamiento del contenido de streaming.
    @rtype: float
    '''
    return statistics.mean(t.reale_year for t in registros)


def Contenido_con_mayor_duracion(registros):
    '''
    Devuelve una lista de tuplas con los contenidos que tienen mayor duracion.
    @param registros:  lista de tuplas con los datos de una plataforma de streaming
    @return: Lista de tuplas con los contenidos que tienen mayor duracion 
    '''
    maximo =  max(registros, key = lambda x:x.duration)
    res = [t for t in registros if t.duration == maximo.duration]
    return 

def ProgramasDeTV_porAño(registros, type):
    '''
    Devuelve una lista de tuplas con dos datos en cada tupla (año de lanzamiento y nombre), en la que se refleja los
    años de lanzamiento de menor a mayor de los programas de television. 

    @param registros:  lista de tuplas con los datos de una plataforma de streaming.
    @param type: Contenido por el que se van a filtrar los registros.
    @type type: str
    @return: lista de tuplas con dos datos en cada tupla (año de lanzamiento y nombre), en la que se refleja los
    años de lanzamiento de menor a mayor de los programas de television. 
    @rtype: (str, int, str,)
    '''
    
    Programas = [(t.type,t.release_year,t.title)for t in registros if t.type == type]
    res = sorted(Programas)
    return res