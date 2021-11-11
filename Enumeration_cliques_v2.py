from Bron_Kerbosch_ameliore import  *

def enumerer_cliques(G):

    n = len(list(G.keys()))
    
    #2 : Calculer la liste d'adjacente générée par G
    L = degenerescence(G,True)
    print("L=",L)


    for j in range(1, n+1):

        #Calcul toutes les cliques
        Nb_Cliques = version_ameliore(G)
        
        # print("Nb_Cliques=",Nb_Cliques)

        for K in Nb_Cliques:
            # print("K",K)
            for x in K:
                # print("x dans k=",x)
                for voisin_g in G[x]:
                # for voisin_g in K:
                    # print("voisin de x dans K=",voisin_g)
                    if voisin_g in K:
                    # if voisin_g != x:
                        # print("voisin de x=",x," dans G est voisin de x dans K, voisin_g=",voisin_g)
                        if(L.index(voisin_g) <= L.index(x)):
                            # print("Oui on est voisin dans k et il est inferieur sur le rang de L")
                            break
                        # else:
                        #     print(K)
                else:
                    print(K)
                    continue
                break

# G = {
#         1: [2,3,4],
#         2: [1,3,4,5],
#         3: [1,2,4],
#         4: [1,2,3,5,6],
#         5: [2,4,7],
#         6: [4],
#         7: [5]
#     }


# enumerer_cliques(G)