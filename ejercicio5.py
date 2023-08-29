import datetime


class pacientes:
    def __init__(self):
        self.__name = ""
        self.__cedula = 0
        self.__gender = ""
        self.__visitas = {}
    
    def getname(self):
        return self.__name
    def getcedula(self):
        return self.__cedula
    def getgender (self):
        return self.__gender
    def getvisitas(self):
        return self.__visitas

    def setname(self,name):
        self.__name = name
    def setcedula(self,cc):
        self.__cedula = cc
    def setgender(self,gender):
        self.__gender = gender
    def setvisitas(self,lista):
        self.__visitas = lista

class visita:
    def __init__(self):
        self.__date = datetime.datetime(1,1,1)
        self.__registro = ""
        self.__notas = ""
    
    def getdate(self):
        return self.__date
    def getregistro(self):
        return self.__registro
    def getnotas(self):
        return self.__notas
    
    def setdate(self,date):
        self.__date = date
    def setregistro(self,url):
        self.__registro = url
    def setnotas(self,notas):
        self.__notas = notas

class indice:
    def __init__(self):
        self.__potencia_delta = 0.0
        self.__potencia_theta = 0.0
        self.__potencia_alfa1 = 0.0
        self.__potencia_alfa2 = 0.0
        self.__potencia_beta = 0.0
        self.__potencia_gamma = 0.0
    
    def getpotencia_delta (self):
        return self.__potencia_delta
    


