import random

def Generate_Graph():
    Vertex = input("Chose numbers of vertex to add : ")
    V = int(Vertex) #Nombre de sommets
    G = {   1: [2,3],
            2: [1,3],
            3: [1,2]
        }

    m = 2                        #Nombre d'arrete à ajouter pour un sommet donné

    Degre_Init = 6               #Dégré initial

    List_Degre = [Degre_Init]    #Liste des dégre après ajouté d'un nouveau sommet

    for i in range(1, V+1):
        List_Des_Sommet = list(G.keys())    #liste des sommets
        G_temp = {}                         #Graphé_tempo créé après ajouté de sommet
        Sommet_Choisi = []                  #Liste des sommet choisr pour construire le graphe tem

        k = len(List_Degre)-1

        for j in range(m):

            choix_sommet = random.choice(List_Des_Sommet)   #Les voisins candidats du nouveau sommet
            print("Sommet choisi : " + str(choix_sommet))
            print("Liason  : " + str(i+3) + "--" + str(choix_sommet))

            va = (m)/(List_Degre[k])       #Probabilité de l'apparution de l'arrete

            Sommet_Choisi.append(choix_sommet)

            List_Des_Sommet.remove(choix_sommet)

            print("les arrets du sommets " + str(i+3) + " Sont ajoutées avec proba : " + str(va))
            print("****************************************************")

        #Mettre à jours la liste des degrés
        List_Degre.append(List_Degre[k]+4)
        G_temp[i+3] = Sommet_Choisi

        G.update(G_temp)
        print("Liste des Sommets : " + str(list(G.keys())))
        print("Liste des dégrés : " + str(List_Degre))



        #Mettre à jour le graphe avec le nouveau sommet
        Nvoisin = []
        for k in Sommet_Choisi:
            for A in range(0, len(list(G.values()))):
                if k==A:
                    print( list(G.values())[k-1] )
                    Nvoisin = list (G.values())[k-1]

            Nvoisin.append(i+3)

        print("*******************************************************")
        print("LE GRAPHE FINAL")

    return G


#Complexité : T(n) = n*n