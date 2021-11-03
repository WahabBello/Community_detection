# Trouver toutes les cliques maximales dans un graphe en utilisant l'algorithme de Bron-Kerbosch. Le graphe d'entrée est ici
# au format liste d'adjacence, un dict avec des sommets comme clés et des listes de leurs voisins comme valeurs.

# from collections import defaultdict
import copy

def version_ameliore(graphe):
  p = set(graphe.keys())
  r = set()
  x = set()
  cliques = []
  for v in Degenerescence(graphe):
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


#in this function, we create a dictionary
#where the key is the degree and the value is the nodes
def get_degree_list(graphe):
    """create degree distribution"""
    
    D={}
    
    #if the current degree hasnt been checked
    #we create a new key under the current degree
    #otherwise we append the new node into the list
    for i in graphe.keys():
        try:
            D[len(graphe[i])].append(i)

        except KeyError:
            D[len(graphe[i])]=[i]
    
    #dictionary is sorted by key instead of value in ascending order
    D=dict(sorted(D.items()))
    
    return D

# -----------

def Degenerescence(graphe,ordering=False,degeneracy=False):
    """ ".
    """
    
    subset=copy.deepcopy(graphe)
    
    #k is the ultimate degeneracy
    k=0
    
    #denote L as the checked list
    L=[]
    
    #denote output as the storage of vertices in 1-core to k-core
    output={}

    #degree distribution
    # print("subset =",subset,"et son type =",type(subset))
    D=get_degree_list(subset)
    # print("D =",D,"et son type =",type(D))
    
    #initialize
    for i in range(1,max(D.keys())+1):
        output[i]=[]
    # print("outpout =",output)
    #we initialize the current degree i to 0
    #because we want to keep track of 1-core to k-core
    i=0

    while D:
                
        #denote i as the minimum degree in the current graph
        i=list(D.keys())[0]
                        
        #k denotes the degeneracy
        k=max(k,i)
        
        #pick a random vertex with the minimum degree
        v=D[i].pop(0)
        # print("v iteration=",v)
        #checked and removed
        L.append(v)
        del subset[v]
        # print("subset iteration=",subset)
        # subset.remove(v)
        output[k].append(v)
        # print("output iteration=",output)
        
        #update the degree list
        D=get_degree_list(subset)   
    
    #start from -2 to 0
    for ind in sorted(output.keys(),reverse=True)[1:]:

        #remove empty k-core
        if not output[ind+1]:
            del output[ind+1]

        #add vertices from high order core to low order core
        else:
            output[ind]+=output[ind+1]
    
    #output depends on the requirement
    if ordering:
        return L
    elif degeneracy:
        return k
    else:
        return output


G = {
        1: [2,3,4],
        2: [1,3,4,5],
        3: [1,2,4],
        4: [1,2,3,5,6],
        5: [2,4,7],
        6: [4],
        7: [5]
    }

G2 = {
        "A": ["B"],
        "B": ["A","C","E","D","G"],
        "C": ["B","E","F","I"],
        "D": ["B","E","H","I"],
        "E": ["B","C","D","F","G","H","I"],
        "F": ["B","C","E"],
        "G": ["B","E","I"]
    }
G3 = {
        1: [2,3],
        2: [1,3,4],
        3: [1,2],
        4: [2]
    }
print(version_ameliore(G))

#print(version_ameliore(G2))

# test = Degenerescence(G)
# print(test)
# print(version_ameliore(G2))

