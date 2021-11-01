import random

def Generate_Graph():
    Vertex = input("Chose numbers of vertex : ")
    V = int(Vertex) #Nombre de sommets

    Dico = {}       #Dictionnaire pour stocker le graphe {sommet ->[voisin] }

    for i in range(1,V+1):
        List_Voisin = []    #List des voisins d'un sommet
        for j in range(1,V+1):
            print("\n"+str(i) + ":")
            P = round(random.uniform(0, 1), 1) #Nombre entre  0 et 1

            if (i==j):
                print("pas de lien -> " + str(j) + " on ne veut pas de boucle")

            elif(P<0.3 or P>0.8):
                print("pas de lien -> " + str(j) + " Avec proba : " + str(P))

            else:
                print("lien -> " + str(j) + " Avec probabilité : " + str(P))
                List_Voisin.append(j)
        print("**************************************************")
        Dico[i] = List_Voisin

    return Dico
