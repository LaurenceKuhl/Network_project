import math
from powerlaw import Fit
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
  
  def clust_powlaw(self):
    gamma = []
    for G in self.graphs:
	  fit = Fit(sorted(G.degree().values()))
	  gamma.append(fit.power_law.alpha)
    return gamma
    
  def fitness(self, n, k, g, d, c_k):# (returns a float between 0 and 1)	
   # n is the number of nodes, k is the list of degrees, g is the gamma of the power law, d is the diameter, c_k is the list of clustering coefficients 
    list_d1 = []
    for i in xrange (len(k)) :
      list_d1.append( (c_k[i] - 1./k[i])**2 )
    d1  =  np.mean (list_d1)# clustering fitness
    if  g  >  2  and g  <  3 : # power law fitness
      d2  =  0
    else : d2  =  (g - 2.5)**2
    d3  =  (d  -  math.log(math.log(n)))**2
    fit  =  1./(1 + self.coeff[0]*d1 + self.coeff[1]*d2 + self.coeff[2]*d3) #fitness
    return fit
    

  #========================================== methods for the population
  
  def fitness_list(self):  #(returns a list of float)
    list_f = []
    for G in self.graphs:
	  liste_f.append(fitness(G))
	return liste_f    
	  
  #def reproduction(): (returns void)

  def mutation(self , nb_newborns) : 	  # randomly mutate all the newborns
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

    
    
    
P1 = Population(1000,0.5,2,0.1,0.1,0.2,[2])
print P1.clust_powlaw()

