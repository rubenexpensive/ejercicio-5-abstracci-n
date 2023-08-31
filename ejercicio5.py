import datetime
# import mysql.connector
# import mongo


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
    def getpotencia_theta(self):
        return self.__potencia_theta
    def getpotencia_alfa1(self):
        return self.__potencia_alfa1
    def getpotencia_alfa2(self):
        return self.__potencia_alfa2
    def getpotencia_beta(self):
        return self.__potencia_beta
    def getpotencia_gamma (self):
        return self.__potencia_gamma
    
    def setpotencia_delta(self,delta):
        self.__potencia_delta = delta
    def setpotencia_theta(self,theta):
        self.__potencia_theta = theta
    def setpotencia_alfa1(self,alfa1):
        self.__potencia_alfa1 = alfa1
    def setpotencia_beta(self,beta):
        self.__potencia_beta = beta
    def setpotencia_gamma(self,gamma):
        self.__potencia_gamma = gamma

class sistema:
    def __init__(self):
        self.__dicpacientes = {}

    def verificarsiexiste (self,nombre):
        if nombre in self.__dicpacientes:
            print("El paciente ya existe")
            return True

    # def ingresarpaciente (self,name,cc,gender,list):
    #     name = 

    def deletepaciente (self,cc):
        if cc in self.__dicpacientes:
            return True
    
    #def guardar (self,paciente):
        


