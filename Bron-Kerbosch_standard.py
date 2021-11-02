# Trouver toutes les cliques maximales dans un graphe en utilisant l'algorithme de Bron-Kerbosch. Le graphe d'entrée est ici
# au format liste d'adjacence, un dict avec des sommets comme clés et des listes de leurs voisins comme valeurs.


def version_standard_Sans_pivot(graphe, p, r= set(), x = set(), cliques = []):

  if len(p) == 0 and len(x) == 0:
    cliques.append(r)

  for v in list(p):
    sommet = set(graphe[v])
    version_standard_Sans_pivot(graphe, p.intersection(sommet), r.union([v]), x.intersection(sommet), cliques)
    p.remove(v)
    x.add(v)
  return cliques


def version_standard_avec_pivot(graphe, p, r= set(), x = set(), cliques = []):
  if len(p) == 0 and len(x) == 0:
    cliques.append(r)

  pivot = next(iter(p.union(x))) if p else next(iter(r))
  for v in p.difference(graphe[pivot]):
    sommet = graphe[v]
    version_standard_avec_pivot(graphe, p.intersection(sommet), r.union([v]), x.intersection(sommet), cliques)
    p.remove(v)
    x.add(v)
  return cliques


G = {
        1: [2,3,4],
        2: [1,3,4,5],
        3: [1,2,4],
        4: [1,2,3,6],
        5: [2,4,7],
        6: [4],
        7: [5]
    }


G3 = {
        1: [2,3],
        2: [1,3,4],
        3: [1,2],
        4: [2]
    }



# version_standard_Sans_pivot
test = version_standard_Sans_pivot(G, set(G.keys()))
print(test)

print("*****************************************************")

# version_standard_Avec_pivot
test_pivot = version_standard_avec_pivot(G, set(G.keys()))
print(test_pivot)


