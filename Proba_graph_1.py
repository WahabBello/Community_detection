import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
from random import random


def Generate_Graph2(n, p):
    V = list([v for v in range(1,n+1)]) #List des sommet de 1 à n
    E = list()     #List des arretes

    for combination in combinations(V, 2):  #Lister toutes les combinaisons possible avec 1 sommet
        a = random()    #Nombre aléatoire entre 0 et 1
        print(a)
        if a < p:
            E.append(combination)   #Ajouter le lien dans la liste
            print("lien avec prob : "  + str(a))
        else:
            print("pas de lien avec prob : " + str(a))
    print(V)
    print(E)

    #Construction du graph avec la bibliothèque networkx
    g = nx.Graph()
    g.add_nodes_from(V)
    g.add_edges_from(E)

    return g


def Dessiner_Graphe(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    plt.title("Random Graph Generation ")
    plt.show()

#Main
"""
n = 5
p = 0.3
G = Generate_Graph2(n,p)

Dessiner_Graphe(G)
"""