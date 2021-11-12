# CONTEXTE : Détection de communautés dans des réseaux sociaux

## Introduction :

La problématique principale du projet est d’énumérer certaines structures dans des graphes modélisant théoriquement certains réseaux sociaux. Et Le but du projet est d’implémenter deux algorithmes d’énumération de cliques maximales dans des graphes générés aléatoirement

## Ce projet est réalisé par :
- DIALLO Abdou
- KOUASSI Kofié
- ROUGUI Rania
- SATOURI Maha

## Implémentations :

- Générerer des graphes aléatoires avec :

	- la probabilité p choisie aléatoirement telle que 0<p<1      	(  [Proba_graph_1.py](https://github.com/WahabBello/Community_detection/blob/main/Proba_graph_1.py) et [Proba_graph_2.py](https://github.com/WahabBello/Community_detection/blob/main/Proba_graph_2.py) )
	- les graphes de Barabàsi-Albert (Barabàsi_Albert_graph.py)	    
- L’algorithme de Bron Kerbosch version standard ( [Bron_Kerbosch_standard.py](https://github.com/WahabBello/Community_detection/blob/main/Bron_Kerbosch_standard.py) ) : 

	- version sans pivot  
	- version avec pivot    

- L’algorithme de Bron Kerbosch version amélioré ( [Bron_Kerbosch_ameliore.py](https://github.com/WahabBello/Community_detection/blob/main/Bron_Kerbosch_ameliore.py) ):

	- version sans pivot  
	- version avec pivot
	- ordre de dégénérescence du graphe  

- Les algorithmes de la nouvelle technique de décomposition pour l'énumération des cliques maximale :

	- version 1 ( [Enumeration_cliques_v1.py](https://github.com/WahabBello/Community_detection/blob/main/Enumeration_cliques_v1.py) )
	- version 2 ( [Enumeration_cliques_v2.py](https://github.com/WahabBello/Community_detection/blob/main/Enumeration_cliques_v2.py) )



### Ce travail a été implementé en langage Python et comprend 3 parties :

### PARTIE I

	1. Proba_graph_1.py
	2. Proba_graph_2.py
	3. Barabàsi_Albert_graph.py	
	
### PARTIE II

	1. Bron_Kerbosch_standard.py
    2. Bron_Kerbosch_ameliore.py
	
### PARTIE III

	1. Enumeration_cliques_v1.py
	2. Enumeration_cliques_v2.py
	
### LE MAIN PRINCIPAL
	
	Main_Princpal.py


### LES RESSOURCES

	1. Un ReadMe.txt
	2. Ressources.txt
	3. Dossier images qui contient des exemples d'exécutions
	4. Un lien Github
		* Le code source du projet
		* Le ReadMe.md
### PRÉ-REQUIS :   

Veuillez éxécutez ces commandes :  
  
	python -m pip install -U pip   
	python -m pip install -U matplotlib  
	python -m pip install -U networkx   	

Nous avons 2 modes d'éxécutions :

###	I. PREMIER MODE

	> Vous devez lancer le programme "Main_Principal"
	
	> Vous verrez ensuite un menu qui s'affiche avec les différentes options 
	
	> Il vous sera demandé ensuite de faire un choix afin de l'exécution du programme souhaité
	
	> Vous avez également la possibilité d'utiliser le graphe généré dans le programme **Barabasi** ou celui de par défaut pour exécuter les programme **Bron_Kerborsh_standard et ameliorer** et aussi **Ennumeration_Clique_V1 et V2**
	
	> Sinon l'exécution de ces programmes utilisera le graphe par défaut G0
	
###	II. DEUXIEME MODE
	
	> Vous avez la possibilité d'éxécuter chaque programme indépendammant  en décommentant le test que nous avions réalisé
	
	> Pour le programme **Proba_graph_1**, vous devez installer d'abord les bibliothèques matplotlib et networkx pour l'affichage du
	graphe
	
	> Pour le programme **Ennumeration_Clique_V1 et V2**, vous devez egalement importer le programme **Bron_Kerborsh_ameliorer** afin  
	d'utiliser  le module qui calcule l'ordre de **degenerescence**
		

	
### Test :  

	python Main_Principal.py
 