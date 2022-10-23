# -*- coding: utf-8 -*-
from Netflix import *

def test_abrir_ficherocsv(fichero):
    print ("="*25 + "test_lee_fichero" +"="*25)
    LISTA_TUPLAS = abrir_ficherocsv(fichero)
    print('Leídos', len(LISTA_TUPLAS),'registros.')
    print('Los cinco primeros registros son:',LISTA_TUPLAS[:5])
    print('Los cinco últimos registros son:',LISTA_TUPLAS[-5:])



def main():

    test_abrir_ficherocsv('./data/plataforma_streaming.csv')
    
    REGISTROS = abrir_ficherocsv('./data/plataforma_streaming.csv')
    
    
if __name__ == '__main__':
    main()