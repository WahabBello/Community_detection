
from Bron_Kerbosch_ameliore import  *


def find_All_cliques(G):

  #1 : Calculer le k dégénéré et la liste des sommet ordonnée L
  k = degenerescence(G, False, True)

  #2 : Calculer la liste d'adjacente générée par G
  L = degenerescence(G, True)

  n = len(list (G.keys()) )

  #3 : Initialiser un dictionnaire vide ABR
  ABR = []

  for j in range(1,n+1):

    #Les cliques maximales du graphe g
    Nb_Clique = version_ameliore(G)

    for K in Nb_Clique:

      #Ordonner les sommets de k suivant L
      if K in ABR:
        break;
      else:
          ABR.append(K)
          print(K)


"""
G = {
        1: [2,3,4],
        2: [1,3,4,5],
        3: [1,2,4],
        4: [1,2,3,5,6],
        5: [2,4,7],
        6: [4],
        7: [5]
    }


find_All_cliques(G)

"""