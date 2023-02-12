import random, Domain, Cost_Function, math

class GeneticSol:

    aproximations = []

    def __init__(self, words_list, result):
        self.__domain = Domain.Domain(words_list, result)
        self.__f_cost = Cost_Function.CostFunction()
        self.__genetic_solution(self.__domain, self.__f_cost, 500, 0.1, 0.5, 15000)

    def __genetic_solution(self, domain, cost_function, pop_size, elite_prop, mutate_prob, max_iter):

        population = []

        for i in range(0, pop_size):

            ind = domain.generate_random_individual()
            ind.set_aptitude(cost_function.function(ind))

            if(domain.is_solution(ind)):
                print("Solucion: ")
                print(ind.final_representation(), "\n\nFuncion de costo:\n", ind.get_aptitude())
                return

            population.insert(self.__correct_ind(ind.get_aptitude(), population), ind)


        while max_iter > 0:

            parents = math.floor(len(population) * elite_prop)

            next_generation = population[0:parents]

            children = len(population) - parents

            while children > 0:

                parentA = next_generation[random.randint(0,len(next_generation)-1)]
                parentB = next_generation[random.randint(0,len(next_generation)-1)]

                child = domain.crossover(parentA, parentB)

                prob = random.uniform(0, 1) #TODO Usar libreria para flotantes

                if prob <= mutate_prob:
                    child = domain.mutate(child)

                child.set_aptitude(cost_function.function(child))

                if(domain.is_solution(child)):
                    print("Solucion: ")
                    print(child.final_representation(),"\n\nFuncion de costo:\n",child.get_aptitude())
                    return

                next_generation.insert(self.__correct_ind(child.get_aptitude(), next_generation), child)

                children -= 1

            population = next_generation

            max_iter -= 1
        #------------------------------------------------
        #Si no se encuentra solucion se muestran las 3 mejores aproximaciones
        self.aproximations = population[0:3]
        self.__aprox_3(self.aproximations)

    def __correct_ind(self, aptitude, pop): #Metodo para saber donde colocar un individuo en la poblacion segun su aptitud
        for i in range(0, len(pop)):
            if(pop[i].get_aptitude() > aptitude):
                return i
        return 0

    def __aprox_3(self, aprox):
        for i in range(0,len(aprox)):
            print("Aproximacion ", i+1, ":")
            print(aprox[i].final_representation())
            print("\nFuncion de costo: ")
            print(aprox[i].get_aptitude(),"\n")