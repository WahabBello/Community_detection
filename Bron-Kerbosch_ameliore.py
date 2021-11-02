# Trouver toutes les cliques maximales dans un graphe en utilisant l'algorithme de Bron-Kerbosch. Le graphe d'entrée est ici
# au format liste d'adjacence, un dict avec des sommets comme clés et des listes de leurs voisins comme valeurs.

from collections import defaultdict

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

def Degenerescence(graphe):
  ordre = []
  ordre_set = set()
  degrees = defaultdict(lambda : 0)
  degen = defaultdict(list)
  deg_max = -1

  for v in graphe:
    deg = len(graphe[v])
    degen[deg].append(v)
    degrees[v] = deg
    if deg > deg_max:
      deg_max = deg

  while True:
    i = 0
    while i <= deg_max:
      if len(degen[i]) != 0:
        break
      i += 1
    else:
      break
    v = degen[i].pop()
    ordre.append(v)
    ordre_set.add(v)
    for w in graphe[v]:
      if w not in ordre_set:
        deg = degrees[w]
        degen[deg].remove(w)
        if deg > 0:
          degrees[w] -= 1
          degen[deg - 1].append(w)

  ordre.reverse()
  return ordre

G = {
        1: [2,3,4],
        2: [1,3,4,5],
        3: [1,2,4],
        4: [1,2,3,6],
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