import math
import random
import numpy as np
import matplotlib.pyplot as plt

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
  
  #def fitness(): (returns a float between 0 and 1)

  #========================================== methods for the population
  
  #def fitness_list(): (returns a list of float)
  #def reproduction(): (returns void)

  def mutation( self , nb_newborns) : 	  # randomly mutate all the newborns
	  if nb_newborns  !=  0 :
		  c  =  0 # counter
		  while c  !=  nb_newborns :  # randomly delete one edge, then add a new one and check wether or not it was already there
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

    
    
    
#P1 = Population(5,0.5,2,0.1,0.1,0.2,[2])

