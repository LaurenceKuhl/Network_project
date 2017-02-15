import math
import random
import numpy as np
import matplotlib.pyplot as plt

import networkx as nx



class Population:
  def __init__(self, nb_nodes, nb_graphs, prob_reproduction, prob_mutation, qtty_reproduction, coefficients):
    self.nb_nodes = nb_nodes
    self.nb_graphs = nb_graphs 
    self.preprod = prob_reproduction
    self.pmut = prob_mutation
    self.qreprod = qtty_reproduction
    self.coeff = coefficients
    
    self.graphs = []
    for i in xrange(nb_graphs):
      g = nx.Graph()
      
      self.graphs.append(
      
    
    
    
G=nx.Graph()
G.add_node(1)
print G.nodes()
