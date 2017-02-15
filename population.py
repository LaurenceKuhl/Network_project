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
    
#P1 = Population(5,0.5,2,0.1,0.1,0.2,[2])

