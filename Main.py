import os
os.chdir("/home/isko/Bureau/IATIC 4/iatic s7/Outils Algo/Community_detection")

import Proba_graph_1
import Proba_graph_2
import Barabàsi_Albert_graph
import Ordre_Dégénéréscence
import Bron_Kerbosch_standard
import Bron_Kerbosch_ameliore



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

    Acceuil = print(" \t 1 : Générer des graphes avec proba 0<p<1 en console \n \t 2 : Générer des graphes avec proba 0<p<1 avec graphique \n \t 3 : Générer un graphe avec Barabassi-Albert \n \t 4 : k dégénéré et l'ordre des sommets \n \t 5 : Ennumération des cliques avec Bron-Kerbosh Standard \n \t 6 : Ennumeration des cliques avec Bron-Kerbosh Amélioré \n \t 7 : Ennumération du cliques maximun avec Algo 1 \n \t 8 : Ennumeration du clique maximun avec Algo 2 \n")

    #choix doit etre un chiffre
    choix = int(input("choix : "))


    if(choix == 1):
        G1 = Proba_graph_2.Generate_Graph()             #Graphe de l'algo 1
        print(G1)

    elif(choix == 2):
        # donner n et p en paramètre
        n = int(input("Saisir nombre de sommet : "))
        p = float(input("Entrer une proba entre 0 et 1 : "))
        G2 = Proba_graph_1.Generate_Graph2(n,p)         #Graphe de l'algo 2 avec dessin
        Proba_graph_1.Dessiner_Graphe(G2)

    elif(choix == 3):
        G3 = Barabàsi_Albert_graph.Generate_Graph()     #Graphe de l'algo 3
        print(G3)

    elif(choix == 4):

        choix_graphe = int(input("Choisi un graphe qui été généré : 1-> G1 | 2-> G2 | 3-> G3 [ Autre -> G0 : "))

        if(choix_graphe == 1):

            k = Ordre_Dégénéréscence.Degenerescence(G1,False,True)   #k : nombre dégénéré
            print("k = " + str(k))
            L = Ordre_Dégénéréscence.Degenerescence(G1,True,False)   #L : liste d'ordre des sommets
            print("L = " + str(L))

        elif(choix_graphe == 2):

            k = Ordre_Dégénéréscence.Degenerescence(G2,False,True)
            print("k = " + str(k))
            L = Ordre_Dégénéréscence.Degenerescence(G2,True,False)
            print("L = " + str(L))

        elif(choix_graphe == 3):

            k = Ordre_Dégénéréscence.Degenerescence(G3,False,True)
            print("k = " + str(k))
            L = Ordre_Dégénéréscence.Degenerescence(G3,True,False)
            print("L = " + str(L))

        else:
            k = Ordre_Dégénéréscence.Degenerescence(G0,False,True)   #Le graphe G0 par défaut
            print("k = " + str(k))
            L = Ordre_Dégénéréscence.Degenerescence(G0,True,False)
            print("L = " + str(L))


    elif(choix == 5):

        choix_graphe = int(input("Choisi un graphe qui été généré : 1-> G1 | 2-> G2 | 3-> G3 [ Autre -> G0 : "))

        if(choix_graphe == 1):

            Cliques = Bron_Kerbosch_standard.version_standard_Sans_pivot(G1,set(G1.keys()))
            print(Cliques)

        elif(choix_graphe == 2):

            Cliques = Bron_Kerbosch_standard.version_standard_Sans_pivot(G2,set(G2.keys()))
            print(Cliques)

        elif(choix_graphe == 3):

            Cliques = Bron_Kerbosch_standard.version_standard_Sans_pivot(G3,set(G3.keys()))
            print(Cliques)

        else:

            Cliques = Bron_Kerbosch_standard.version_standard_Sans_pivot(G0,set(G0.keys()))
            print(Cliques)


    elif(choix == 6):

        choix_graphe = int(input("Choisi un graphe qui été généré : 1-> G1 | 2-> G2 | 3-> G3 [ Autre -> G0 : "))
        if(choix_graphe == 1):

            Cliques = Bron_Kerbosch_ameliore.version_ameliore(G1)
            print(Cliques)

        elif(choix_graphe == 2):

            Cliques = Bron_Kerbosch_ameliore.version_ameliore(G2)
            print(Cliques)

        elif(choix_graphe ==3):

            Cliques = Bron_Kerbosch_ameliore.version_ameliore(G3)
            print(Cliques)

        else :

            Cliques = Bron_Kerbosch_ameliore.version_ameliore(G0)
            print(Cliques)

    elif(choix == 7):

        choix_graphe = int(input("Choisi un graphe qui été généré : 1-> G1 | 2-> G2 | 3-> G3 [ Autre -> G0 : "))

        if(choix_graphe == 1):

            Clique = Find_Cliques(G1)
            print(Clique)

        elif(choix_graphe == 2):

            Clique = Find_Cliques(G2)
            print(Clique)

        elif(choix_graphe ==3):

            Clique = Find_Cliques(G3)
            print(Clique)

        else :
            Clique = Find_Cliques(G0)
            print(Clique)

    elif(choix == 8):

        choix_graphe = int(input("Choisi un graphe qui été généré : 1-> G1 | 2-> G2 | 3-> G3 [ Autre -> G0 : "))

        if(choix_graphe == 1):

            Clique = Find_Cliques(G1)
            print(Clique)

        elif(cgoix_graphe == 2):

            Clique = Find_Cliques(G2)
            print(Clique)

        elif(choix_graphe ==3):

            Clique = Find_Cliques(G3)
            print(Clique)

        else:

            Clique = Find_Cliques(G0)
            print(Clique)

    else:
        print("Vous avez Quitté le programme")




