# Trouver toutes les cliques maximales dans un graphe en utilisant l'algorithme de Bron-Kerbosch. Le graphe d'entrée est ici 
# au format liste d'adjacence, un dict avec des sommets comme clés et des listes de leurs voisins comme valeurs.
# https://en.wikipedia.org/wiki/Bron-Kerbosch_algorithm

# from collections import defaultdict

# Ici p = set(graphe.keys())
def version_standard(graphe, p, r= set(), x = set(), cliques = []):
  p = p
  r = r
  x = x
  cliques = cliques
  if len(p) == 0 and len(x) == 0:
    cliques.append(r)
  else:
    for v in p:
      sommet = graphe[v]
      cliques = version_standard(graphe, r.union([v]), p.intersection(sommet), x.intersection(sommet), cliques)
      p.remove(v)
      x.add(v)
  return sorted(cliques)

def version_standard_avec_pivot(graphe, r, p, x, cliques):
  if len(p) == 0 and len(x) == 0:
    cliques.append(r)
  else:
    u = next(iter(p.union(x)))
    for v in p.difference(graphe[u]):
      sommet = graphe[v]
      cliques = version_standard_avec_pivot(graphe, r.union([v]), p.intersection(sommet), x.intersection(sommet), cliques)
      p.remove(v)
      x.add(v)
  return sorted(cliques)


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
    
# test = version_standard(G, set(G.keys()))
test_pivot = version_standard_avec_pivot(G, set(G.keys()), set(), set(), [])
print(test_pivot)
# print(version_standard(G2))


# def version_standard_aux(graphe, r, p, x, cliques):
#   p = p
#   r = r
#   x = x
#   cliques = cliques
#   if len(p) == 0 and len(x) == 0:
#     cliques.append(r)
#   else:
#     for v in p:
#       sommet = graphe[v]
#       version_standard_aux(graphe, r.union([v]), p.intersection(sommet), x.intersection(sommet), cliques)
#       p.remove(v)
#       x.add(v)
#   return sorted(cliques)

# def version_standard(graphe):
#   p = set(graphe.keys())
#   r = set()
#   x = set()
#   cliques = []
#   for v in p:
#     sommet = graphe[v]
#     cliques = version_standard_aux(graphe, r.union([v]), p.intersection(sommet), x.intersection(sommet), cliques)
#     p.remove(v)
#     x.add(v)
#   return sorted(cliques)