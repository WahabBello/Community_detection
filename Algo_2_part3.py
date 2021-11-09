from Bron_Kerbosch_ameliore import  *

def find_All_cliques_other(G):

    n = len(list(G.keys()))
    L = degenerescence(G,True)
    print("L=",L)


    # for j in range(1, n+1):
    Nb_Cliques = version_ameliore(G)    #Calcul toutes les cliques
    print("Nb_Cliques=",Nb_Cliques)

    for K in Nb_Cliques:
        print("K",K)
        for x in K:
            print("x dans k=",x)
            # for voisin_g in G[x]:
            for voisin_g in K:
                # print("voisin de x dans G=",voisin_g)
                # if voisin_g in K:
                if voisin_g != x:
                    # print("voisin de x=",x," dans G est voisin de x dans K, voisin_g=",voisin_g)
                    if(L.index(voisin_g) < L.index(x)):
                        print("Oui on est voisin dans k et il est inferieur sur le rang de L")
                        break
                    else:
                        print(K)
                    # return K       

                    # print("x = " + str(x))
                    # for voisin in K:
                    #     if voisin != x:
                    #         # print("voisin=",voisin)
                    #         # print("Index voisin =",L.index(voisin),"Index x=",L.index(x))
                    #         if(L.index(voisin) < L.index(x)):
                    #             print("Oui on est voisin et il est inferieur")
                    #             # break
                    #         else:
                    #             print(K)
                    #             return K

G = {
        1: [2,3,4],
        2: [1,3,4,5],
        3: [1,2,4],
        4: [1,2,3,5,6],
        5: [2,4,7],
        6: [4],
        7: [5]
    }

find_All_cliques_other(G)