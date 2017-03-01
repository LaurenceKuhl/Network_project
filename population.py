import math
from powerlaw import Fit
import random
import numpy as np
import matplotlib.pyplot as plt
import copy

import networkx as nx



class Population:
  def __init__(self, nb_nodes, p_edges, nb_graphs, prob_reproduction, prob_mutation, qtty_reproduction, coefficients):
    self.nb_nodes = nb_nodes
    self.p_edges = p_edges
    self.nb_graphs = nb_graphs 
    self.preprod = prob_reproduction
    self.pmut = prob_mutation
    self.qreprod = qtty_reproduction
    self.coeff = coefficients
    
    self.graphs = []
    for i in xrange(nb_graphs):
      self.graphs.append(nx.fast_gnp_random_graph(self.nb_nodes, self.p_edges, seed=None, directed=False))
      #print self.graphs[i].edges()
        
  #========================= methods for the graph not predefined before
  
  def clust_powlaw(self):
    gamma = []
    for G in self.graphs:
	  fit = Fit(sorted(G.degree().values()))
	  gamma.append(fit.power_law.alpha)
    return gamma
    
  #def fitness(): (returns a float between 0 and 1)	

  #========================================== methods for the population
  
  #def fitness_list(): (returns a list of float)
  #def reproduction(): (returns void)

  def mutation( self , nb_newborns) : 	  # randomly mutate all the newborns
	  if nb_newborns  !=  0 :
		  c  =  0 # counter
		  while c  !=  nb_newborns :  # randomly delete one edge, then add a new one and check wether or not it was already there
			  m = random.uniform(0,1)
			  if m <= self.pmut :
			  	  deleted  =  random.randint(0, len( self.graphs[- c -1].edges() ) - 1 ) # random edge to be deleted 
			  	  self.graphs[- c-1].remove_edge(self.graphs[- c -1].edges()[deleted][0],self.graphs[- c-1].edges()[deleted][1]) # pop the edge
			  	  flag  =  False
			  	  while flag  ==  False :
				  	  node1  =  random.randint (0, len(self.graphs[-c-1].nodes()))
				  	  node2  =  random.randint (0,len (self.graphs[-c-1].nodes()))
				  	  if node1  !=  node2 and (min(node1,node2), max(node1,node2)) not in self.graphs[- c-1].edges() : # check if edge doesn't already exists
					  	  flag  =  True
					  	  self.graphs[-c-1].add_edge(min(node1,node2), max(node1,node2)) #new edge		
					  	  #what about left-without-edges nodes ?	
			  	  c += 1

  def reproduction(self):
    list_sorted = self.fitness_list()
    list_fit = copy.copy(list_fittest)
    list_sorted.sort(reverse = True)
    reprod_graphs = []
    
    for i in xrange(0, (self.qreprod)*(self.nb_graphs)):
      reprod_graphs.append(self.graphs[list_fit.index(list_sorted[i])]) #So here I have the fittest graphs for the reproduction
      
    nbnewborn = 0
    length_reprod = len(reprod_graphs)/2
    
    for i in xrange(0, length_reprod ,1):
      individuals = random.sample(reprod_graphs, 2)
      self.reprod_graphs.remove(individuals[0])
      self.reprod_graphs.remove(individuals[1])
      
      if (random.uniform(0,1) < self.preprod) :
        qty = int(random.uniform(0,1))
        indiv1 = individuals[0].edges()
        indiv2 = individuals[1].edges()
        newborn = nx.fast_gnp_random_graph(self.nb_nodes, 0, seed=None, directed=False)
        
        for i in xrange(0, qty*len(indiv1)):
          newborn.add_edge(indiv1[i][0], indiv1[i][1])
        
        for i in xrange(0, (1-qty)*len(indiv2)):
          newborn.add_edge(indiv2[i][0], indiv2[i][1])
        
        self.graphs.remove(self.graphs[list_fit.index(list_sorted[-1])])
        self.graphs.append(newborn)
        nbnewborn++
        
    return nbnewborn
        
        
      
      
      
      
    
    
P1 = Population(1000,0.5,2,0.1,0.1,0.2,[2])
print P1.clust_powlaw()

