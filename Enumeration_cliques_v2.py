from Bron_Kerbosch_ameliore import  *

def enumerer_cliques_v2(G):

    n = len(list(G.keys()))

    #2 : Calculer la liste d'adjacente générée par G
    L = degenerescence(G,True)
    # print("L=",L)


    for j in range(1, n+1):

        #Calcul toutes les cliques
        Nb_Cliques = version_ameliore(G)


        for K in Nb_Cliques:
            for x in K:
                for voisin_g in G[x]:
                    if voisin_g in K:
                        if(L.index(voisin_g) < L.index(x)):
                            break

                else:
                    print(K)
                    continue
                break

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


enumerer_cliques_v2(G)
"""