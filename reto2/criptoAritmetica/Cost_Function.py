class CostFunction:

    def function(self, individual):
        '''
        :Function = |R - S|
        :R = valor numerico de la palabra resultado
        :S = suma de los valores numericos de todas las palabras a operar
        '''
        sum_words = self.__sum_words(individual)
        resul_word = individual.get_result()
        return abs(resul_word-sum_words)

    def __sum_words(self, individual):
        res = 0
        for i in range(0, len(individual.get_ops())):
            res += individual.get_ops()[i]
        return res