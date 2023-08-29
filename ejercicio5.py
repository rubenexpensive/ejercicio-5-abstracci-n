class pacientes:
    def __init__(self):
        self.__name = ""
        self.__cedula = 0
        self.__gender = ""
    
    def getname(self):
        return self.__name

    def setname(self,name):
        self.__name = name
    def setcedula(self,cc):
        self.__cedula = cc
    def setgender(self,gender):
        self.__gender = gender

