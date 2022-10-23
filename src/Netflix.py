# -*- coding: utf-8 -*-

import csv
from collections import namedtuple
from Parsers import parsea_fecha

Dats = namedtuple('Dats', 'type, title, director, country, co_production, date_added, release_year, duration, description')

def abrir_ficherocsv (fichero):

    with open (fichero, encoding='uft-8') as f:

        lector = csv.reader(f)
        next(lector)
        res=[]
        for type, title, director, country, co_production, date_added, release_year, duration, description in lector:

            tupla = Dats(type, title, director, country, co_production, parsea_fecha(date_added),\
                 int(release_year), int(duration), description)
            res.append(tupla)
    return res