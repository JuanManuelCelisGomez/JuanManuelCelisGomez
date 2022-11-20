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
----------------------------------Entrega 2---------------------------------------------------------------------
'''
def test_ProgramasDeTV_porAño(registros, type):
    print("="*50 + "test_programasDeTV_porAño" +"="*50)
    res = ProgramasDeTV_porAño(registros, type)
    print (f"Hay {len(res)} Programas de TV. Lista de años de lanzamiento de menor a mayor:")
    print(res)


def main():

    test_abrir_ficherocsv('./data/plataforma_streaming.csv')

    REGISTROS = abrir_ficherocsv('./data/plataforma_streaming.csv')
    test_ProgramasDeTV_porAño(REGISTROS,"TV Show")
    
    
if __name__ == '__main__':
    main()