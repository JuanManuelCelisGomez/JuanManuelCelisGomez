# -*- coding: utf-8 -*-
'''
Este módulo contiene todas las funciones auxiliares relacionadas con el parseo 
de tipos.
'''
from datetime import datetime

def parsea_fecha(cadena):
    '''
    @param cadena: Cadena con una fecha en formato dia/mes/año
    @type param: str
    @return: Un objeto de tipo date con la fecha a la que se refiere la cadena de entrada.
    @rtype: datetime.date
    '''
    return  datetime.strptime(cadena,'%d/%m/%y').date()