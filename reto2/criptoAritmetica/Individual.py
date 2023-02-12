class Individual:

    ops = [] #Representaciones numericas de cada palabra a operar
    result = 0 #Representacion numerica de la palabra resultado

    def __init__(self):
        self.__aptitude = 0
        self.__representation = []

    def set_aptitude(self, new_aptitude):
        self.__aptitude = new_aptitude

    def get_aptitude(self):
        return self.__aptitude

    def get_representation(self):
        return self.__representation

    def set_representation(self, new_rep):
        self.__representation = new_rep

    def get_ops(self):
        return self.ops

    def set_ops(self, new_ops):
        self.ops = new_ops

    def get_result(self):
        return self.result

    def set_result(self, new_res):
        self.result = new_res

    def final_representation(self): #Retorna una lista de tuplas con la letra y numero asociado para cada letra distinta
        out = []
        for i in range(0,len(self.__representation)):
            if(self.__representation[i] != '-'):
                out.append((self.__representation[i],i))
        return out
