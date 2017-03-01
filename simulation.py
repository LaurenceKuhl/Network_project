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
    for x in range(max_time):                          # OR in a second part “while True:”
      liste_f = pop1.fitness_list() 
      if max(liste_f)==1 : 
        return the best graph
      else {
		  pop1.reproduction(liste_f, prob_reproduction, qtty_reproduction)
		  mutation() #of the newborn only
		  liste_f = fitness_list()
      }


P1 = pop.Population(5,0.5,2,0.1,0.1,0.2,[2])
P1.mutation(2)
