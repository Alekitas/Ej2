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
    
    def muestra(self):
        return self.__numviajero+';'+self.__DNI+';'+self.__apellido+';'+self.__millasacum
    def returnnumviajero(self,numviajero):
        return self.__numviajero
    def canttotalmillas(self):
        millas=int(input('Ingrese cantidad de millas: '))
        return millas
    
    def acumularmillas(self,millas):
        self.__millasacum+=millas
        return self.__millasacum
    
    def canjearmillas(self,millasacum,millascanj):
        if millascanj<=self.__millasacum:
            return self.__millasacum
        else: print('ERROR')