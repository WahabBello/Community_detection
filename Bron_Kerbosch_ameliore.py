

"""
    Trouver toutes les cliques maximales dans un graphe en utilisant l'algorithme de Bron-Kerbosch dans sa version amelioré.
    Cette version amelioré utilisé l'orde de degenerescence dans le but de potentiellement réduire l'itération.
    Le graphe d'entrée est ici au format liste d'adjacence avec 
    un dict avec des sommets comme clés et des listes de leurs voisins comme valeurs. 
"""

import copy

def version_ameliore(graphe):
  p = set(graphe.keys())
  r = set()
  x = set()
  cliques = []
  for v in degenerescence(graphe,True):
    sommet = graphe[v]
    version_ameliore_avec_pivot(graphe, r.union([v]), p.intersection(sommet), x.intersection(sommet), cliques)
    p.remove(v)
    x.add(v)
  return cliques

def version_ameliore_avec_pivot(graphe, r, p, x, cliques):
  if len(p) == 0 and len(x) == 0:
    cliques.append(r)
  else:
    pivot = next(iter(p.union(x)))
    for v in p.difference(graphe[pivot]):
      sommet = graphe[v]
      version_ameliore_avec_pivot(graphe, r.union([v]), p.intersection(sommet), x.intersection(sommet), cliques)
      p.remove(v)
      x.add(v)



def liste_degrees(graphe):
    """
    Dans cette fonction, nous allons créer un dictionnaire
        où la clé est le degré et la valeur est une liste des noeuds ayant ce degré. 
        
        Paramètres
            Une graphe au format liste d'adjacence. 
        Renvoyer
            Un dictionnaire trié par clé au lieu de la valeur dans l'ordre ascendant 
    """
    
    D={}
    
    for i in graphe.keys():
        try:
            D[len(graphe[i])].append(i)

        except KeyError:
            D[len(graphe[i])]=[i]
    
    D=dict(sorted(D.items()))
    
    return D


def degenerescence(graphe,en_ordre=False,avec_degenerescense=False):
    
    """
    Un algorithme proposé par David W. Matula, et Leland L. Beck pour trouver le noyau k d'un graphe.
        L'implémentation est basée sur leur pseudocode dans wikipedia intitulé "Degeneracy (graph theory)".
        
        Paramètres
            - Une graphe au format liste d'adjacence. 
            - optionnel : True si on veut la liste L dans l'ordre de dégénerescence
            - optionnel : True si on veut la dégénerescence k 
        Renvoyer
            - (par defaut) Un dictionnaire avec le stockage des sommets regoupé de 1-core à k-core
            - la liste L dans l'ordre de dégénerescence
            - la dégénerescence k                           
    
    """
    copie_graphe=copy.deepcopy(graphe)
    
    #k est l'ultime dégénérescence
    k=0
    
    #L'ordre de dégénerescence
    L=[]
    
    #Le stockage des sommets par groupe de 1-core à k-core
    sortie={}

    #La distribution des degrées
    D=liste_degrees(copie_graphe)
    
    #initialisation
    for i in range(1,max(D.keys())):
        sortie[i]=[]
    
    i=0

    while D:
                
        #Le degré minimum dans le graphe actuel
        i=list(D.keys())[0]
                        
        #la dégénerescence k 
        k=max(k,i)
        
        #Choisit un sommet avec le degré minimum
        v=D[i].pop(0)
        
        L.append(v)
        
        del copie_graphe[v]
        
        sortie[k].append(v)

        for liste in copie_graphe.values():
            if v in liste:
                liste.remove(v)

        
        #Recalcul de La distribution des degrées
        D=liste_degrees(copie_graphe)   
    
    #Triage
    for element in sorted(sortie.keys(),reverse=True)[1:]:

        if not sortie[element+1]:
            del sortie[element+1]

        else:
            sortie[element]+=sortie[element+1]
    
    #La sortie depend du besoin
    if en_ordre:
        return L
    elif avec_degenerescense:
        return k
    else:
        return sortie




G = {
        1: [2,3,4],
        2: [1,3,4,5],
        3: [1,2,4],
        4: [1,2,3,5,6],
        5: [2,4,7],
        6: [4],
        7: [5]
    }
    

"""
k = degenerescence(G, False, True)
print("k : " + str(k))

L = degenerescence(G, True)
print("Ordre des sommets : " + str(L))

print(version_ameliore(G))


"""