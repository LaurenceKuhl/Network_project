import math
import random
import numpy as np
import matplotlib.pyplot as plt
import population as pop
import sys



class Simulation:
	def __init__(self, lim_fitness, text_time, max_time, nb_nodes, p_edges, nb_graphs, prob_reproduction, prob_mutation, qtty_reproduction, coefficients):
		self.lim_fitness = lim_fitness
		self.text_time = text_time
		self.max_time = max_time 
		#usefull for the population
		self.nb_nodes = nb_nodes
		self.p_edges = p_edges
		self.nb_graphs = nb_graphs 
		self.preprod = prob_reproduction
		self.pmut = prob_mutation
		self.qreprod = qtty_reproduction
		self.coeff = coefficients
    
  #def show_best(): (returns a figure and a list of the realistic parameters)
  #def save_pop(): (save a file ".txt")
  
  #runs the simulation (returns void or "finished")

	def run(self):
		#initialise the population
		pop1 = pop.Population(self.nb_nodes, self.p_edges, self.nb_graphs, self.preprod, self.pmut, self.qreprod, self.coeff)
		#run the simulation
		results = []
		for x in xrange(max_time):                  # OR in a second part "while True:"
			if (x+1)%text_time == 0 :
				print 'saving population'
				pop1.save_pop()

			liste_f = pop1.fitness_list() 
			if max(liste_f) >= lim_fitness :
				pop1.save_pop()
				pop1.show_best() 
				return "Found it!"
			else :
				nb_newborns = pop1.reproduction()
				pop1.mutation(nb_newborns) #of the newborn only
				list_fit = pop1.fitness_list()
				print x , max(list_fit) , np.mean(list_fit)
				results.append([max(list_fit), np.mean(list_fit)])
				
		return results




#~ P1 = pop.Population(5,0.5,2,0.1,0.1,0.2,[0.3,0.3,0.4])
#~ P1.mutation(2)

#~ P1.fitness(5,[1,2,3],2.1,2, [2,3,5])


#~ lim_fitness = sys.argv[1]
#~ text_time = sys.argv[2]
#~ max_time = sys.argv[3]
#~ 
#~ nb_nodes = sys.argv[4]
#~ p_edges = sys.argv[5]
#~ nb_graphs = sys.argv[6]
#~ prob_reproduction = sys.argv[7]
#~ prob_mutation = sys.argv[8]
#~ qtty_reproduction = sys.argv[9]
#~ coefficients = sys.argv[10]

lim_fitness = 1
text_time = 100
max_time = 500
nb_nodes = 20
p_edges = 0.2
nb_graphs = 40
prob_reproduction = 0.1
prob_mutation = 0.1
qtty_reproduction = 0.2
coefficients = [1,1,1]

S = Simulation(lim_fitness, text_time, max_time, nb_nodes, p_edges, nb_graphs, prob_reproduction, prob_mutation, qtty_reproduction, coefficients)
A = S.run()
a1 = []
a2 = []
for i in range(len(A)):
	a1.append(A[i][0])
	a2.append(A[i][1])
x = range(len(A))

plt.plot(x,A)
plt.ylabel('yoloswag')
plt.show()

