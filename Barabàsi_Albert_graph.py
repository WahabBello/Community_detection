import random

def Generate_graph_barasi_albert():
    Vertex = input("Entrer le nombre de sommets à ajouter : ")

   #Nombre de sommets
    V = int(Vertex)
    G = {   1: [2,3],
            2: [1,3],
            3: [1,2]
        }

    #Nombre d'arrete à ajouter pour un sommet donné
    m = 2

    #Dégré initial
    Degre_Init = 6

    #Liste des dégres après ajouté d'un nouveau sommet
    List_Degre = [Degre_Init]

    for i in range(1, V+1):
        List_Des_Sommet = list(G.keys())

        #Graphe_tempo créé après ajouté de sommet
        G_temp = {}

        #Liste des sommet choisr pour construire le graphe
        Sommet_Choisi = []

        k = len(List_Degre)-1

        for j in range(m):
            #Les voisins candidats pour former les arretes
            choix_sommet = random.choice(List_Des_Sommet)
            print("Sommet choisi : " + str(choix_sommet))
            print("Liason  : " + str(i+3) + "--" + str(choix_sommet))

            #Probabilité de l'apparution de l'arrete
            va = (m)/(List_Degre[k])
            Sommet_Choisi.append(choix_sommet)
            List_Des_Sommet.remove(choix_sommet)
            print("arret  " + str(i+3) + " ajoutées avec proba : " + str(va))

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
                    Nvoisin = list (G.values())[k-1]
            Nvoisin.append(i+3)

        print("*******************************************************")
        print("LE GRAPHE FINAL")

    return G


"""
G = Generate_graph_barasi_albert()
print(G)

"""