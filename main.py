import sys
from Graphe import Graphe
from Algorithmes import a_star

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python.exe main.py <chemin_vers_fichier>")
        print("Or: py main.py <chemin_vers_fichier>")
        sys.exit(1)

    nom_fichier = sys.argv[1]
    graphe = Graphe(nom_fichier)
    # graphe.lire_fichier(nom_fichier)
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

    # Récupérer et afficher les résultats

    chemin1 = a_star(graphe, graphe.depart, graphe.arrivee)
    print("Chemin trouvé:", chemin1)
    graphe.write_chemin_astar(chemin1)
    graphe.plot_chemin(chemin1)

    chemin2 = graphe.get_chemin()
    graphe.write_chemin(chemin2)
    print("Deuxième chemin trouvé:", chemin2)
    graphe.plot_chemin(chemin2)
