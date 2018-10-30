#In this example we will consider two genes: no_of_blades,length of blade
#(We are trying to find something about fans i guess)

import math
population_size=int(input('Enter the population size: '))
chromosomes=[]
fitness_values=[]

def fitness_func(ip_chromosome):
    return (sum(ip_chromosome)*12.3)*math.pi #Can be anything

for i in range(population_size):
    ip=[int(x) for x in input('Enter '+str(i+1)+" chromosome's gene: ").split(" ")]
    chromosomes.append(ip)
    fitness_values.append(fitness_func(ip))
print("Chromosomes: ",chromosomes)
print("Fitness Values: ",fitness_values)
