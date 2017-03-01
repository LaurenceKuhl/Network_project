import math
import random
import numpy as np
import matplotlib.pyplot as plt
import population as pop



class Simulation:
  def __init__(self, lim_fitness, text_time, max_time):
    self.lim_fitness = lim_fitness
    self.text_time = text_time
    self.max_time = max_time 
    
  #def show_best(): (returns a figure and a list of the realistic parameters)
  #def save_pop(): (save a file ".txt")
  
  #runs the simulation (returns void or "finished")
  #def run():
	#initialise the population
    #poeple = pop.Population()
    #run the simulation
    #liste_f = fitness_list() 
    #for x in range(max_time):                          # OR in a second part while True:
		  #if best fitness ever: return the best graph
		  #pop.reproduction(liste_f, prob_reproduction, qtty_reproduction)
		  #mutation() #of the newborn only
		  #liste_f = fitness_list()


P1 = pop.Population(5,0.5,2,0.1,0.1,0.2,[0.3,0.3,0.4])
P1.mutation(2)
P1.fitness(5,[1,2,3],2.1,2, [2,3,5])
