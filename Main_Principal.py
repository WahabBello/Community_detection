from Proba_graph_1 import Generate_Graph2, Dessiner_Graphe
from Proba_graph_2 import Generate_Graph
from Barabàsi_Albert_graph import Generate_graph_barasi_albert
from Bron_Kerbosch_standard import version_standard_sans_pivot
from Bron_Kerbosch_ameliore import version_ameliore, degenerescence
from Enumeration_cliques_v1 import enumerer_cliques_v1
from Enumeration_cliques_v2 import enumerer_cliques_v2


#Graphe par défaut
G0 = {
        1: [2,3,4],
        2: [1,3,4,5],
        3: [1,2,4],
        4: [1,2,3,5,6],
        5: [2,4,7],
        6: [4],
        7: [5]
    }

print("***********************Choisir un programme ***********************\n")
choix = 0
while(choix != 10):

    Acceuil = print(" \t 1 : Générer des graphes avec proba 0<p<1 en console \n \t 2 : Générer des graphes avec proba 0<p<1 avec graphique \n \t 3 : Générer un graphe avec Barabassi-Albert \n \t 4 : Le k de dégénérécense et L l'ordre des sommets \n \t 5 : Ennumération des cliques avec Bron-Kerbosh Standard \n \t 6 : Ennumeration des cliques avec Bron-Kerbosh Amélioré \n \t 7 : Ennumération du cliques maximun avec Algo 1 \n \t 8 : Ennumeration du clique maximun avec Algo 2 \n")

    #choix doit etre un chiffre
    try:
        choix = int(input("Faites votre choix : "))
    except ValueError:
        choix = int(input("Faites votre choix en saisissant un entier: "))

    if(choix == 1):
        #Graphe de l'algo 1
        G1 = Generate_Graph()
        print("Graphe = ",G1,"\n")

    elif(choix == 2):
        # donner n et p en paramètre
        n = int(input("Saisir nombre de sommet : "))
        p = float(input("Entrer une proba entre 0 et 1 : "))

        #Graphe de l'algo 2 avec dessin
        G2 = Generate_Graph2(n,p)
        Dessiner_Graphe(G2)

    elif(choix == 3):
        #Graphe de l'algo 3
        G3 = Generate_graph_barasi_albert()
        print("Graphe = ",G3,"\n")


    elif(choix == 4):
        try:
            choix_graphe = int(input("Choisissez un graphe qui a été généré : 3-> G3 | Autre -> G0 : "))
        except ValueError:
            choix_graphe = int(input("Choisissez un graphe entre 3 ou un entier quelconque (graphe par défaut) : 3-> G3 | Autre -> G0 : "))
            choix = int(input("Faites votre choix en saisissant un entier: "))

        if(choix_graphe == 3):
            k = degenerescence(G3,False,True)
            print("k = " + str(k))
            L = degenerescence(G3,True,False)
            print("L = " + str(L),"\n")
        else:
            k = degenerescence(G0,False,True)
            print("k = " + str(k))
            L = degenerescence(G0,True,False)
            print("L = " + str(L),"\n")


    elif(choix == 5):
        try:
            choix_graphe = int(input("Choisissez un graphe qui a été généré : 3-> G3 | Autre -> G0 : "))
        except ValueError:
            choix_graphe = int(input("Choisissez un graphe entre 3 ou un entier quelconque (graphe par défaut) : 3-> G3 | Autre -> G0 : "))
            choix = int(input("Faites votre choix en saisissant un entier: "))


        if(choix_graphe == 3):
            Cliques = version_standard_sans_pivot(G3,set(G3.keys()))
            print(Cliques,"\n")
        else:
            Cliques = version_standard_sans_pivot(G0,set(G0.keys()))
            print(Cliques,"\n")


    elif(choix == 6):
        try:
            choix_graphe = int(input("Choisissez un graphe qui a été généré : 3-> G3 | Autre -> G0 : "))
        except ValueError:
            choix_graphe = int(input("Choisissez un graphe entre 3 ou un entier quelconque (graphe par défaut) : 3-> G3 | Autre -> G0 : "))
            choix = int(input("Faites votre choix en saisissant un entier: "))

        if(choix_graphe == 3):
            Cliques = version_ameliore(G3)
            print(Cliques,"\n")
        else :
            Cliques = version_ameliore(G0)
            print(Cliques,"\n")


    elif(choix == 7):
        try:
            choix_graphe = int(input("Choisissez un graphe qui a été généré : 3-> G3 | Autre -> G0 : "))
        except ValueError:
            choix_graphe = int(input("Choisissez un graphe entre 3 ou un entier quelconque (graphe par défaut) : 3-> G3 | Autre -> G0 : "))
            choix = int(input("Faites votre choix en saisissant un entier: "))

        if(choix_graphe ==3):
            enumerer_cliques_v1(G3)
        else :
            enumerer_cliques_v1(G0)


    elif(choix == 8):
        try:
            choix_graphe = int(input("Choisissez un graphe qui a été généré : 3-> G3 | Autre -> G0 : "))
        except ValueError:
            choix_graphe = int(input("Choisissez un graphe entre 1, 3 et 0(par défaut) : 3-> G3 | Autre -> G0 : "))
            choix = int(input("Faites votre choix en saisissant un entier: "))

        if(choix_graphe ==3):
            enumerer_cliques_v2(G3)
        else:
            enumerer_cliques_v2(G0)

    else:
        print("Vous avez Quitté le programme \n")