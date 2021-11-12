import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
from random import random


def Generate_Graph2(n, p):

    #List des sommet de 1 à n
    V = list([v for v in range(1,n+1)])

    #List des arretes
    E = list()

    #Lister toutes les combinaisons possible avec 1 sommet (on notera que le (1,2) et (2,1) representent les meme arrete
    for combination in combinations(V, 2):

        #Nombre aléatoire entre 0 et 1
        a = random()
        print(a)
        if a < p:

            #Ajouter le lien dans la liste
            E.append(combination)
            print("lien avec prob : "  + str(a))
        else:
            print("pas de lien avec prob : " + str(a))
    print("Sommets =",V)
    print("Arretes =",E,"\n")

    #Construction du graph avec la bibliothèque networkx
    g = nx.Graph()
    g.add_nodes_from(V)
    g.add_edges_from(E)

    return g


#Dessin du graph avec la bibliothèque matplotlib
def Dessiner_Graphe(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    plt.title("Génération de graphe aléatoire ")
    plt.show()


"""
n = 5
p = 0.3
G = Generate_Graph2(n,p)
Dessiner_Graphe(G)
"""