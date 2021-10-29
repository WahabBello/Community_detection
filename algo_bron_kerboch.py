def ordre_degenere():

    G = {
            0: [1],
            1: [0,2,3,4],
            2: [1,4,5],
            3: [1,4,8],
            4: [1,2,3,5,6,7,8],
            5: [2,4,7],
            6: [1,4,7],
            7: [3,4,5,8],
            8: [2,3,4,6,7]
        }


    A = list(G.values())    #Liste des voisins
    B = list(G.keys())      #Listes sommets

    Liste_Degre = []    #Liste des dégrés de sommet à partir de 0
    Liste_des_min = []  #Liste des dégrés min

    n = len(B)
    while(n>1):

        B = list(G.keys())
        A = list(G.values())
        Liste_Degre = []

        for i in range(len(B)):

            Liste_Degre.append(len(A[i]))

        print("Liste des dégrés du graphe : " + str(Liste_Degre))

        d = min(Liste_Degre)
        som_su = Liste_Degre.index(d)
        print(d)
        print(som_su)

        G.pop((Liste_Degre.index(d)), None)

        Liste_des_min.append(d)

        if(n==0):
            break;
        n = n-1

    print("Lites de sommets min : " + str(Liste_des_min))

    return max(Liste_des_min)