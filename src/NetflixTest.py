# -*- coding: utf-8 -*-
'''
Este módulo contiene el test del módulo Netflix, actualmente proporciona un error de conversión de datos.
'''
from Netflix import *

'''
-------------------------------------Entrega 1------------------------------------------------------
'''

def test_abrir_ficherocsv(fichero):
    '''
    @param cadena: fichero contiene los datos del csv
    @return: dos tuplas que contienen los cinco primeros registros y los cinco últimos registros
    '''
    print ("="*25 + "test_lee_fichero" +"="*25)
    LISTA_TUPLAS = abrir_ficherocsv(fichero)
    print('Leídos', len(LISTA_TUPLAS),'registros.')
    print('Los cinco primeros registros son:',LISTA_TUPLAS[:5])
    print('Los cinco últimos registros son:',LISTA_TUPLAS[-5:])

'''
-------------------------------------------------------------------------------------------------------
'''

def main():

    test_abrir_ficherocsv('./data/plataforma_streaming.csv')
    
    REGISTROS = abrir_ficherocsv('./data/plataforma_streaming.csv')
    
    
if __name__ == '__main__':
    main()