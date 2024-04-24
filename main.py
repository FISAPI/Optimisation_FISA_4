import sys
import time
from Graphe import Graphe
from Algorithmes import a_star
from random import random
import math
from Voyage import Voyage


if __name__ == "__main__":
    entry = str(input("Bienvenue dans le menu, souhaitez-vous résoudre un problème de plus court chemin(1) ou un problème de voyageur de commerce(2) ?"))
    while entry != "1" and entry != "2":
        entry = str(input("Bienvenue dans le menu, souhaitez-vous résoudre un problème de plus court chemin(1) ou un problème de voyageur de commerce(2) ?"))
    if entry == "1":
        file = str(input("Indiquez le chemin vers le fichier de graphe (par exemple: exos/reseau_5_10_1.txt) : "))
        graphe = Graphe(file)
        graphe.afficher_reseau()
        graphe.afficher_graphe()
        graphe.afficher_graphe_matplotlib()
        graphe.write_data_in_file()
        graphe.write_reseau_in_file()
        print("\nVous pouvez maintenant récupérer le fichier .dat pour le tester dans CPLEX.")
        print("Lorsque vous avez le résultat, vous pouvez copier le fichier le résultat d dans le fichier avec le même "
              "nom de réseau_chemin dans le dossier exos.\n")
        input("Appuyez sur une touche pour continuer...")
        rep = str(input("Avez-vous créé le fichier avec le résultat ? (Oui/Non) : "))
        while rep != "Oui" and rep !="OUI" and rep != "oui" and rep != "O" and rep != "o":
            rep = str(input("Avez-vous créé le fichier avec le résultat ? (Oui/Non) : "))

        # Heuristic choice input
        he = 0  
        while he < 1 or he > 3:
            he = int(input("Choisissez une heuristique (zero (1), ligne droite (2) ou ou la distance euclidienne (3)) : "))
        print("Vous avez choisi l'heuristique", he)

        # Récupérer et afficher les résultats
        debut = time.time()
        chemin1, total_cost = a_star(graphe, graphe.depart, graphe.arrivee, he)    
        fin = time.time()
        print("Solution de l'algorithme A* :")
        print(f"Temps d'exécution : {fin - debut} secondes")
        print("Chemin trouvé:", chemin1)
        print("Coût total du chemin:", total_cost)  
        graphe.write_chemin_astar(chemin1)
        graphe.plot_chemin(chemin1)
        
        
        print("\nRésolution du problème avec CPLEX :")
        chemin2 = graphe.get_chemin()
        graphe.write_chemin(chemin2)
        print("Deuxième chemin trouvé:", chemin2)
        graphe.plot_chemin(chemin2)

    elif entry == "2":
        choix = str(input("Voulez-vous générer un graphe aléatoire (1) ou lire un graphe à partir d'un fichier (2) ?"))
        while choix != "1" and choix != "2":
            choix = str(input("Voulez-vous générer un graphe aléatoire (1) ou lire un graphe à partir d'un fichier (2) ?"))
        if choix == "1":
            n = int(input("Entrez le nombre de sommets : "))
            p = float(input("Entrez la probabilité de connexion : "))
            voyage = Voyage()
            voyage.create_random_graphe(n, n, n, p)
        if choix == "2":
            file = str(input("Indiquez le chemin vers le fichier de graphe (par exemple: exos/default_graphe.txt) : "))
            voyage = Voyage()
            voyage.lire_graphe_fichier(file)
        print("lancement de l'algorithme...")
        voyage.write_data_2_in_file()
        print("\nVous pouvez maintenant récupérer le fichier .dat pour le tester dans CPLEX.")
        print("Lorsque vous avez le résultat, vous pouvez copier le fichier le résultat d dans le fichier avec le même "
              "nom de réseau_chemin dans le dossier exos.\n")
        str(input("Appuyez sur une touche pour continuer..."))
        rep = str(input("Avez-vous créé le fichier avec le résultat ? (Oui/Non) : "))
        while rep != "Oui" and rep !="OUI" and rep != "oui" and rep != "O" and rep != "o":
            rep = str(input("Avez-vous créé le fichier avec le résultat ? (Oui/Non) : "))
        voyage.afficher_graphe_matplotlib()
        chemin = voyage.lire_tableau_aretes_fichier("exos/default_graphe_chemin.txt")
        voyage.plot_chemin(chemin)
        voyage.write_chemin(chemin)
    
    print("Fin du programme")