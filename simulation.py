import math
import random
import numpy as np
import matplotlib.pyplot as plt
import population as pop



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
    pop1 = pop.Population(nb_nodes, p_edges, nb_graphs, preprod, pmut, qreprod, coeff)
    #run the simulation
    for x in range(max_time):                  # OR in a second part “while True:”
      if x%text_time == 0 :
        save_pop()

      liste_f = pop1.fitness_list() 
      if max(liste_f) >= lim_fitness :
        save_pop()
        show_best() 
        return "Found it!"
      else :
        nb_newborns = pop1.reproduction()
        pop1.mutation(nb_newborns) #of the newborn only
      
    save_pop()
    show_best() 
    return "Finished!"


P1 = pop.Population(5,0.5,2,0.1,0.1,0.2,[2])
P1.mutation(2)

#~ lim_fitness = argv[1]
#~ text_time = argv[2]
#~ max_time = argv[3]
#~ 
#~ nb_nodes = argv[4]
#~ p_edges = argv[5]
#~ nb_graphs = argv[6]
#~ prob_reproduction = argv[7]
#~ prob_mutation = argv[8]
#~ qtty_reproduction = argv[9]
#~ coefficients = argv[10]

lim_fitness = 1
text_time = 100
max_time = 50

nb_nodes = 5
p_edges = 0.5
nb_graphs = 2
prob_reproduction = 0.1
prob_mutation = 0.1
qtty_reproduction = 0.2
coefficients = [1,1,1]

S = Simulation(lim_fitness, text_time, max_time, nb_nodes, p_edges, nb_graphs, prob_reproduction, prob_mutation, qtty_reproduction, coefficients)
S.run()

