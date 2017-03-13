import math
from powerlaw import Fit
import random
import numpy as np
import matplotlib.pyplot as plt
import operator
import copy
import networkx as nx
import os

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
    self.reprod_graphs = []
    for i in xrange(nb_graphs):
      self.graphs.append(nx.fast_gnp_random_graph(self.nb_nodes, self.p_edges, seed=None, directed=False))
      #print self.graphs[i].edges()
        
    #========================= methods for the graph not predefined before
      
  def clust_powlaw(self, G):
    # Checks if degree distribution follows power law distribution
    # Returns value of gamma for graph G
    gamma = []
    fit = Fit(sorted(G.degree().values()))
    return fit.power_law.alpha
  
  def clust_coef(self,G):
    # Returns value of average clustering coefficient of each degree
    avgcoef = []
    degrees = []
    tuplist = sorted(G.degree().items(), key=operator.itemgetter(1))
    deg = -1
    i = -1
    L = []
    for tup in tuplist:
      if tup[1] > deg:
        deg = tup[1]
        i += 1
        L.append([tup[0]])
        degrees.append(tup[1])
      elif tup[1] == deg:
        L[i].append(tup[0])
    for nodelist in L:
      avgcoef.append(nx.average_clustering(G,nodelist))
    return degrees, avgcoef
  
  def diameter(self,G):
    nodes = []
    for node in G.nodes():
      if G.degree(node) > 0: nodes.append(node)
    e = {}
    for v in nodes:
      length = nx.single_source_shortest_path_length(G,v) 
      e[v] = max(length.values())
    return max(e.values())
    
  def fitness(self, G):# (returns a float between 0 and 1)	
    # k is the sorted list of degrees, g is the gamma of the power law, 
    # d is the diameter, c_k is the list of clustering coefficients
    k, c_k = self.clust_coef(G)
    g = self.clust_powlaw(G)
    d = self.diameter(G)
    list_d1 = []
    for i in xrange (len(k)) :
      if not k[i] == 0 : # No idea what to do if k[i] equals 0 so i dont consider them here (Antoine)
        list_d1.append( (c_k[i] - 1./k[i])**2 )
    d1  =  np.mean (list_d1)# clustering fitness
    if  g  >  2  and g  <  3 : # power law fitness
      d2  =  0
    else : d2  =  (g - 2.5)**2
    d3  =  (d  -  math.log(math.log(self.nb_nodes)))**2
    fit  =  1./(1 + self.coeff[0]*d1 + self.coeff[1]*d2 + self.coeff[2]*d3) #fitness
    return fit
    
  


  #========================================== methods for the population
  
    def fitness_list(self):  #(returns a list of float)
      list_f = []
      for G in self.graphs:
        list_f.append(self.fitness(G))
      return list_f    

	
    def mutation(self , nb_newborns) : 	  # randomly mutate all the newborns
      if nb_newborns  !=  0 :
        c  =  0 # counter
        while c  !=  nb_newborns :  # only newborns mutate # 
          nb_mut  =  len(self.graphs[- c -1].edges() ) - 1
          c_mut  =  0
          while c_mut !=  nb_mut : # pmut nb_edges times
            print self.graphs[- c -1].edges()
            m  =  random.uniform(0,1)
            if m  <=  self.pmut :
              d  =  random.uniform(0,1) # in/
              if d  <  0.5 : #delete
                deleted  =  random.randint(0, len( self.graphs[- c -1].edges() ) - 1 ) # random edge to be deleted 
                self.graphs[- c-1].remove_edge(self.graphs[- c -1].edges()[deleted][0],self.graphs[- c-1].edges()[deleted][1]) # pop the edge
              else :
                flag  =  False
                while flag  ==  False :
                  node1  =  random.randint (0, len(self.graphs[-c-1].nodes()))
                  node2  =  random.randint (0,len (self.graphs[-c-1].nodes()))
                  if node1  !=  node2 and (min(node1,node2), max(node1,node2)) not in self.graphs[- c-1].edges() : # check if edge doesn't already exists
                    flag  =  True
                    self.graphs[-c-1].add_edge(min(node1,node2), max(node1,node2)) #new edge		
            if len(self.graphs[- c -1].edges() )  ==  0 :
              break
            c_mut +=1
          c += 1


    def reproduction(self):
        list_sorted = self.fitness_list()
        list_fit = copy.copy(list_sorted)
        list_sorted.sort(reverse = True)
        self.reprod_graphs = []
        
        for i in xrange(0, int((self.qreprod)*(self.nb_graphs))):
            self.reprod_graphs.append(self.graphs[list_fit.index(list_sorted[i])]) #So here I have the fittest graphs for the reproduction
	
	nbnewborn = 0
	length_reprod = len(self.reprod_graphs)/2
        
        for i in xrange(0, length_reprod ,1):
            individuals = random.sample(self.reprod_graphs, 2)
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
		nbnewborn+=1
        
        return nbnewborn
        
    def save_pop(self,mypath): # Save the current graph population in a textfile
        if not os.path.isdir(mypath):
            os.makedirs(mypath)
        for i in xrange(len(self.graphs)):
            s = './popsave/g'+str(i)+'.txt'
            fh=open(s,'wb')
            nx.write_adjlist(self.graphs[i],fh)
            fh.close()

    def load_pop(self,nbofgraphs,mypath): # Load a graph population from a directory
	mypath = 'popsave'
        if os.path.isdir(mypath):
	    self.graphs = []
	    for i in xrange(nbofgraphs):
		s = './popsave/g'+str(i)+'.txt'
		fh=open(s,'r')
		self.graphs.append(nx.read_adjlist(fh))
		fh.close()
		#print i+1
	else :
	    print 'Save directory not found'

    def show_best(self): # Plot the graph with the best fitness of our current population
	list_fit = self.fitness_list()
	G = self.graphs[list_fit.index(max(list_fit))]
	deg = nx.degree(G).values()	
	print deg
	pos = nx.spring_layout(G,iterations=200)
	nx.draw(G,pos,node_color = deg,node_size = 800,cmap=plt.cm.Blues)
	print "printing graph number " + str(list_fit.index(max(list_fit))) + " "  
        plt.show()

P1 = Population(1000,0.5,4,0.1,0.1,0.2,[1,1,1])
#P1.load_pop(40,'popsave')
print P1.diameter(P1.graphs[0])

