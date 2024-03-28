import sys
from Graphe import Graphe
import cplex

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <chemin_vers_fichier>")
        print("Or: py main.py <chemin_vers_fichier>")
        sys.exit(1)

    nom_fichier = sys.argv[1]
    graphe = Graphe(nom_fichier)
    # graphe.lire_fichier(nom_fichier)
    graphe.afficher_reseau()
    graphe.afficher_graphe()
    graphe.afficher_graphe_matplotlib()
    graphe.write_reseau_in_file()

    # Créer une instance de CPLEX
    cpx = cplex.Cplex()

    # Charger le modèle à partir d'un fichier MOD
    cpx.read("TP_Optimisation_1_2.mod")

    # Charger les données à partir d'un fichier DAT
    cpx.read_data("TP_Optimisation_1_2.dat")

    # Résoudre le modèle avec CPLEX
    cpx.solve()

    # Récupérer et afficher les résultats
    print("Valeur de la fonction objectif : ", cpx.solution.get_objective_value())
    print("Valeur de x : ", cpx.solution.get_values("x"))  # Remplacez "x" par le nom de votre variable



