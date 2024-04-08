import sys
from Graphe import Graphe
from Algorithmes import a_star

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
    graphe.write_data_in_file()
    graphe.write_reseau_in_file()
    # print("Vous pouvez maintenant récupérer le fichier .dat pour le tester dans CPLEX.")
    # print("Lorsque vous avez le résultat, vous pouvez copier le fichier .sol dans le dossier exos.")
    # input("Appuyez sur une touche pour continuer...")

    # Récupérer et afficher les résultats

    # # Create an OPL model from a .mod file
    # with create_opl_model(model="zootupleset.mod",data="zootupleset.dat") as opl:

    #     # Generate the problem and solve it.
    #     opl.run()

    #     # Get the names of post processing tables
    #     print("Table names are: "+ str(opl.output_table_names))

    #     # Get all the post processing tables as dataframes.
    #     for name, table in iteritems(opl.report):
    #         print("Table : " + name)
    #     for t in table.itertuples(index=False):
    #             print(t)

    #     # nicer display
    #     for t in table.itertuples(index=False):
    #         print(t[0]," buses ",t[1], "seats")



    chemin = a_star(graphe, graphe.depart, graphe.arrivee)
    print("Chemin trouvé:", chemin)

    graphe.plot_chemin(chemin)
