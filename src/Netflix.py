# -*- coding: utf-8 -*-

''' Este módulo contiene las funciones principales que decriben el programa'''

import csv
from collections import namedtuple
from Parsers import *
from datetime import datetime 


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