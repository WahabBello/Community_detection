""" Trouver toutes les cliques maximales dans un graphe en utilisant l'algorithme de Bron-Kerbosch. 
    Le graphe d'entrée est ici au format liste d'adjacence, 
    un dict avec des sommets comme clés et des listes de leurs voisins comme valeurs.
"""

def version_standard_sans_pivot(graphe, p, r= set(), x = set(), cliques = []):
  """ Dans cette fonction, nous avons implémenté l'algorithme l'algorithme de Bron-Kerbosch sans un pivot.
        L'implémentation est basée sur leur pseudocode proposé dans le document du papier [1]. 
      
      Paramètres
          - pamam1: Une graphe au format liste d'adjacence. 
          - pamam2: Une ensemble tel que "set(graphe.keys())"
          - params(optionel) Il faut rien mettre

      Renvoyer
          Une liste contenant tous les cliques maximales
  """
  
  if len(p) == 0 and len(x) == 0:
    cliques.append(r)

  for v in list(p):
    sommet = set(graphe[v])
    version_standard_sans_pivot(graphe, p.intersection(sommet), r.union([v]), x.intersection(sommet), cliques)
    p.remove(v)
    x.add(v)
  return cliques


def version_standard_avec_pivot(graphe, p, r= set(), x = set(), cliques = []):
  """ Dans cette fonction, nous avons implémenté l'algorithme l'algorithme de Bron-Kerbosch avec un pivot.
      L'implémentation est basée sur leur pseudocode proposé dans le document du papier [1].
      L'ajout du pivot, nous permet de faire moins d'itérations dans la récursion.
      
      Paramètres
          - param1: Une graphe G au format liste d'adjacence. 
          - param2: Une ensemble contenant tous les sommets dans G tel que "p = set(G.keys())"
          - params(optionel) Il faut rien mettre

      Renvoyer
          Une liste contenant tous les cliques maximales
  """
  if len(p) == 0 and len(x) == 0:
    cliques.append(r)

  pivot = next(iter(p.union(x))) if p else next(iter(r))
  for v in p.difference(graphe[pivot]):
    sommet = graphe[v]
    version_standard_avec_pivot(graphe, p.intersection(sommet), r.union([v]), x.intersection(sommet), cliques)
    p.remove(v)
    x.add(v)
  return cliques



