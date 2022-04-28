
from ClaseViajeroFrecuente import ViajeroFrecuente
import csv

if __name__=='__main__':
    lista=[]
    c=0
    archivo=open('Libro1.csv')
    reader=csv.reader(archivo,delimiter=',')
    for fila in reader:
        numviajero=fila[0]
        DNI=fila[1]
        nombre=fila[2]
        apellido=fila[3]
        c+=1
        millasacum=int(input('Ingrese la cantidad de millas acumuladas del viajero {}: \n'.format(numviajero)))
    unViajero=ViajeroFrecuente(numviajero,DNI,nombre,apellido,millasacum)
    lista.append(unViajero)
    archivo.close()
    opcion=0
    while opcion!=-1:
        print('1- Consultar Cantidad de Millas Acumuladas\n')
        print('2-Acumular Millas\n')
        print('3-Canjear Millas\n')
        print('4-Ingrese -1 para finalizar\n')
        if opcion==1:
            for i in range(4):
               print('Cantidad total de millas acumuladas del viajero: {} {}',lista[i].returnnumviajero(),';',lista[i].canttotalmillas())
               if opcion==2:
                   numv=input('Ingrese numero de viajero a acumular millas: ')
                   act=input('Ingrese cantidad de millas del ultimo viaje: ')
                   lista[numv-1].acumularmillas(act)
                   print('Cantidad de millas actualizada: ',lista[i].canttotalmillas())
                   if opcion==3:
                       mcanj=input('Ingrese cantidad de millas a canjear: ')
                       if mcanj<=lista[numv-1].canttotalmillas():
                           lista[numv-1].canjearmillas(mcanj)
                           print('Millas actuales: ',lista[i].canttotalmillas())