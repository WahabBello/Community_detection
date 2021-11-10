import os
os.chdir("/home/isko/Bureau/IATIC 4/iatic s7/Outils Algo/Python/Code/Partie 2'")
import Ordre_Dégénéréscence
import Bron_Kerbosch_ameliore



def find_All_cliques(G):

  #1 : Calculer le k dégénéré et la liste des sommet ordonnée L
  k = Degenerescence(G, False, True)
  L = Degenerescence(G, True)
  print("ordre de dégénérescence k : " + str(k))
  print("Liste ordonnée des sommets L : " + str(L))


  #2 : Calculer la liste d'adjacente générée par G
  print("La liste d'adjacente de G : " + str(G))
  n = len(list (G.keys()) )


  #3 : Initialiser un dictionnaire vide ABR
  ABR = []


  for j in range(1,n+1):
    Nb_Clique = version_ameliore(G)   #les cliques du graphe g
    #print(Nb_Clique)


    for K in Nb_Clique:
      #print(K)

      #ordonner les sommets de k suivant L
      if K in ABR:
        break;
      else:
          ABR.append(K)
          return K
