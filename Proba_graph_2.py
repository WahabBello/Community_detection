import random


def Generate_Graph():

    Vertex = input("Entrer un nombre de sommets supérieur ou égal à 3 : ")


    #Nombre de sommets
    V = int(Vertex)

    #Dictionnaire pour stocker le graphe {sommet ->[voisin] } sous forme de liste d'adjacente
    Dico = {}

    for i in range(1,V+1):
        #List des voisins d'un sommet
        List_Voisin = []

        for j in range(1,V+1):
            print("\n"+str(i) + ":")

            #Nombre entre  0 et 1 et on conservons que le premier chiffre après la virgule
            P = round(random.uniform(0, 1), 1)

            if (i==j):
                print("pas de lien -> " + str(j) + " on ne veut pas de boucle")

            #Nous conservons de facons arbritraire les arretes dont l'appariition est compris entre 0.3 et 0.8 inclus
            elif(P<0.3 or P>0.8):
                print("pas de lien -> " + str(j) + " Avec proba : " + str(P))

            else:
                print("lien -> " + str(j) + " Avec probabilité : " + str(P))
                List_Voisin.append(j)
        print("**************************************************")
        Dico[i] = List_Voisin

    return Dico



"""
G = Generate_Graph()
print(G)
"""

