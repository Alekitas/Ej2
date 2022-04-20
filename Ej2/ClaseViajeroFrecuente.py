class ViajeroFrecuente:
    __numviajero=''
    __DNI=''
    __nombre=''
    __apellido=''
    __millasacum=''
    def __init__(self,numviajero,DNI,nombre,apellido,millasacum):
        self.__numviajero=numviajero
        self.__DNI=DNI
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millasacum=millasacum
    def canttotalmillas(self):
        millas=int(input('Ingrese cantidad de millas: '))
        return millas
    def acumularmillas(self,millas):
        pass
    def canjearmillas(self):
        pass