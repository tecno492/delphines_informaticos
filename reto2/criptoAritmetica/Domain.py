import Individual, random
from random import shuffle

CONST_INDIVIDUAL_SIZE = 10

class Domain:

    initial_letters = []

    def __init__(self, words, result):
        self.words_list = words
        self.result = result

        for words in self.words_list+[self.result]: #Se guardan las letras iniciales de cada palabra en una lista
            self.initial_letters += [words[0]]

    def generate_random_individual(self):
        individual_out = Individual.Individual()
        out = self.__extract_distinct_letters()
        #----------------------------------------
        shuffle(out)
        while(not self.__is_valid(out)):
            shuffle(out)
        # -------------------------------------------------------
        self.set_individual_atribbutes(individual_out, out)  # Se setean todos los atributos del individuo
        # -------------------------------------------------------
        return individual_out

    def is_solution(self, individual):
        return individual.get_aptitude() == 0

    def crossover(self, parentA, parentB): #Se aplica el metodo de cruzamiento utilzado en el problema de El Viajero
        individual_out = Individual.Individual()
        rep_out = []
        #--------------------------------------------------------
        p1 = random.randint(0,CONST_INDIVIDUAL_SIZE-1)
        p2 = random.randint(0,CONST_INDIVIDUAL_SIZE-1)

        while abs(p1-p2) <= len(self.initial_letters): #Restriccion para que no se tomen menos cromosomas que la cantidad de letras iniciales
            p1 = random.randint(0, CONST_INDIVIDUAL_SIZE-1)
            p2 = random.randint(0, CONST_INDIVIDUAL_SIZE-1)

        if(p1 > p2):
            equal_part = parentA.get_representation()[p2:p1]
        else:
            equal_part = parentA.get_representation()[p1:p2]
        #---------------------------------------------------------
        while not self.__is_valid(equal_part):
            shuffle(equal_part)

        for i in range(0, len(equal_part)): #Se copian los cromosomas seleccionados en el nuevo hijo
            current_letter = equal_part[i]
            rep_out += [current_letter]

        for letter in parentB.get_representation(): #Se selccionan cromosomas del padreB para heredarlos al hijo
            if(letter not in equal_part):
                rep_out += [letter]

        while len(rep_out) < CONST_INDIVIDUAL_SIZE: #Si se copiaron todos los cromosomas diferentes y aun no se llena el hijo, se rellena con '-'
            rep_out += ["-"]
        # -------------------------------------------------------
        self.set_individual_atribbutes(individual_out, rep_out)
        # -------------------------------------------------------
        return individual_out

    def mutate(self, individual):
        individual_out = Individual.Individual()

        p1 = random.randint(0,CONST_INDIVIDUAL_SIZE-1)
        p2 = random.randint(0,CONST_INDIVIDUAL_SIZE-1)
        new_rep = individual.get_representation()
        (new_rep[p1],new_rep[p2]) = (new_rep[p2], new_rep[p1]) #SWAP

        #Se valida que la representacion resultante sea valida y que no haya intercambio entre casillas vacias
        while (new_rep[p1] == '-' and new_rep[p2] == '-') or (not self.__is_valid(new_rep)):
            p1 = random.randint(0, CONST_INDIVIDUAL_SIZE-1)
            p2 = random.randint(0, CONST_INDIVIDUAL_SIZE-1)
            (new_rep[p1], new_rep[p2]) = (new_rep[p2], new_rep[p1])  #SWAP
        # -------------------------------------------------------
        self.set_individual_atribbutes(individual_out, new_rep)
        # -------------------------------------------------------
        return individual_out

    def __extract_distinct_letters(self):
        all_words = self.words_list+[self.result]
        out = ['-','-','-','-','-','-','-','-','-','-'] #No pueden haber mas de 10 letras distintas
        i = 0
        for word in all_words:
            for letter in word:
                if(letter not in out):
                    out[i] = letter
                    i += 1
        return out

    def __is_valid(self, rep): #Verifica si no hay ninguna letra inicial en la posicion 0 del arreglo
        return rep[0] not in self.initial_letters

    def __get_numerical_operators(self, letters): #Retorna un arreglo con cada valor numerico correspondiente a cada palabra a operar
        out = []
        for word in self.words_list:
            res = ""
            for letter in word:
                res += str(letters.index(letter))
            out.append(int(res))
        return out

    def __get_numerical_result_word(self, letters): #Retorna el valor numerico de la palabra resultado
        res = ""
        for letter in self.result:
            res += str(letters.index(letter))
        return int(res)

    def set_individual_atribbutes(self, individual, representation):
        individual.set_representation(representation)
        individual.set_ops(self.__get_numerical_operators(representation))
        individual.set_result(self.__get_numerical_result_word(representation))