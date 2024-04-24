import sys
import time
from Graphe import Graphe
from Algorithmes import a_star
from random import random
import math
from Voyage import Voyage


if __name__ == "__main__":
    voyage = Voyage()

    # Générer un graphe aléatoire avec 20 sommets et une probabilité de connexion de 0.5
    # n = 10
    # p = 0.5
    # voyage.create_random_graphe(n, n, n, p)

    # Écrire le voyage dans un fichier texte
    # voyage.write_reseau_in_file()
    # voyage.ecrire_graphe_fichier("exos/default_graphe.txt")
    # voyage2 = Voyage()
    voyage.lire_graphe_fichier("exos/default_graphe.txt")
    voyage.write_data_2_in_file()
    
    voyage.afficher_graphe_matplotlib()
    str(input("Appuyez sur une touche pour continuer..."))
    chemin = voyage.lire_tableau_aretes_fichier("exos/default_graphe_chemin.txt")
    voyage.plot_chemin(chemin)
    
    # if len(sys.argv) < 2:
    #     print("Usage: python.exe main.py <chemin_vers_fichier>")
    #     print("Or: py main.py <chemin_vers_fichier>")
    #     sys.exit(1)

    # nom_fichier = sys.argv[1]
    # graphe = Graphe(nom_fichier)
    # # graphe.lire_fichier(nom_fichier)
    # graphe.afficher_reseau()
    # graphe.afficher_graphe()
    # graphe.afficher_graphe_matplotlib()
    # graphe.write_data_in_file()
    # graphe.write_reseau_in_file()
    
    
    # print("\nVous pouvez maintenant récupérer le fichier .dat pour le tester dans CPLEX.")
    # print("Lorsque vous avez le résultat, vous pouvez copier le fichier le résultat d dans le fichier avec le même "
    #       "nom de réseau_chemin dans le dossier exos.\n")
    # input("Appuyez sur une touche pour continuer...")
    # rep = str(input("Avez-vous créé le fichier avec le résultat ? (Oui/Non) : "))
    # while rep != "Oui" and rep !="OUI" and rep != "oui" and rep != "O" and rep != "o":
    #     rep = str(input("Avez-vous créé le fichier avec le résultat ? (Oui/Non) : "))

    # # Heuristic choice input
    # he = 0  
    # while he < 1 or he > 3:
    #     he = int(input("Choisissez une heuristique (zero (1), ligne droite (2) ou ou la distance euclidienne (3)) : "))
    # print("Vous avez choisi l'heuristique", he)

    # # Récupérer et afficher les résultats
    # debut = time.time()
    # chemin1, total_cost = a_star(graphe, graphe.depart, graphe.arrivee, he)    
    # fin = time.time()
    # print(f"Temps d'exécution : {fin - debut} secondes")
    # print("Chemin trouvé:", chemin1)
    # print("Coût total du chemin:", total_cost)  
    # graphe.write_chemin_astar(chemin1)
    # graphe.plot_chemin(chemin1)

    # chemin2 = graphe.get_chemin()
    # graphe.write_chemin(chemin2)
    # print("Deuxième chemin trouvé:", chemin2)
    # graphe.plot_chemin(chemin2)
