import sys
from Graphe import Graphe

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <chemin_vers_fichier>")
        print("Or: py main.py <chemin_vers_fichier>")
        sys.exit(1)

    nom_fichier = sys.argv[1]
    graphe = Graphe()
    graphe.lire_fichier(nom_fichier)
    graphe.afficher_reseau()
    graphe.afficher_graphe()
    graphe.afficher_graphe_matplotlib()
