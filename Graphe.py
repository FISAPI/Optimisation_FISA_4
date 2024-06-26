import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

import numpy as np


class Graphe:
    def __init__(self, file_path=None):
        self.reseau = []  # Représentation du réseau (matrice)
        self.sommets = {}  # Informations sur les sommets (uniquement ceux accessibles)
        self.aretes = []  # Liste des arêtes (sommets connectés et leur coût)
        self.depart = None
        self.arrivee = None
        if file_path is not None:
            # Utilisez os.path pour diviser le chemin en répertoire et nom de fichier
            self.path, file_name_with_ext = os.path.split(file_path)
            # Divisez le nom de fichier avec extension en nom de fichier et extension
            self.file_name, self.extension = os.path.splitext(file_name_with_ext)
            if self.file_name is not None and self.extension is not None:
                print(f"Chargement du fichier {self.path + '/' + self.file_name + self.extension}...")
                print("path : ", self.path)
                print("file_name : ", self.file_name)
                print("extension : ", self.extension)
                self.lire_fichier(self.path + '/' + self.file_name + self.extension)
        else:
            print("Chargement du fichier par défaut...")

    def lire_fichier(self, nom_fichier):
        with open(nom_fichier, 'r') as fichier:
            n, m = map(int, fichier.readline().split())  # Dimensions du réseau
            for i in range(n):
                ligne = list(map(int, fichier.readline().split()))
                self.reseau.append(ligne)
                for j, valeur in enumerate(ligne):
                    if valeur != 0:  # Exclut les obstacles
                        # self.sommets[(i, j)] = valeur
                        self.ajouter_sommet((j, i), valeur)
                        if valeur == 2:
                            self.depart = (j, i)
                        elif valeur == 3:
                            self.arrivee = (j, i)

        # Construire les arêtes pour les sommets accessibles, incluant les diagonales
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for i in range(m):
            for j in range(n):
                if (i, j) in self.sommets:  # Si le sommet est accessible
                    for di, dj in directions:  # Adjacents et diagonales
                        if 0 <= i + di < m and 0 <= j + dj < n and (i + di, j + dj) in self.sommets:
                            cout = math.sqrt(di**2 + dj**2)
                            self.ajouter_arete((i, j), (i + di, j + dj), cout)

    def ajouter_arete(self, sommet1, sommet2, cout):
        self.aretes.append(((sommet1, sommet2), cout))

    def ajouter_sommet(self, sommet, valeur):
        self.sommets[sommet] = valeur

    def remove_arete(self, sommet1, sommet2):
        for i, (arete, cout) in enumerate(self.aretes):
            if arete == (sommet1, sommet2) or arete == (sommet2, sommet1):
                self.aretes.remove(((sommet1, sommet2), cout))
                break

    def remove_sommet(self, sommet):
        self.sommets.pop(sommet)
        aretes = self.aretes.copy()
        for (s1, s2), _ in aretes:
            if s1 == sommet or s2 == sommet:
                self.remove_arete(s1, s2)

    def get_voisins(self, sommet):
        voisins = []
        for (autre_sommet, cout) in self.aretes:
            if sommet == autre_sommet[0]:
                voisins.append((autre_sommet[1], cout))
            elif sommet == autre_sommet[1]:
                voisins.append((autre_sommet[0], cout))
        return voisins

    def afficher_reseau(self):
        # Création d'une grille vide
        grille = [[' ' for _ in range(len(self.reseau[0]))] for _ in range(len(self.reseau))]

        # Marquage des sommets et des obstacles
        for i in range(len(self.reseau)):
            for j in range(len(self.reseau[i])):
                if self.reseau[i][j] == 0:
                    grille[i][j] = '■'  # Obstacle
                elif (i, j) == self.depart:
                    grille[i][j] = 'D'  # Départ
                elif (i, j) == self.arrivee:
                    grille[i][j] = 'A'  # Arrivée
                elif (i, j) in self.sommets:
                    grille[i][j] = 'O'  # Sommet accessible

        # Affichage de la grille
        for ligne in grille:
            print(' '.join(ligne))

    def get_aretes(self):
        return self.aretes

    def get_sommets(self):
        return self.sommets

    def get_depart(self):
        return self.depart

    def get_arrivee(self):
        return self.arrivee

    def get_nb_sommets(self):
        return len(self.sommets)

    def get_nb_aretes(self):
        return len(self.aretes)

    def afficher_graphe(self):
        # Afficher chaque sommet et ses arêtes
        for sommet, valeur in self.sommets.items():
            print(f"Sommet {sommet} ({'Départ' if valeur == 2 else 'Arrivée' if valeur == 3 else 'Traversable'}):")
            for (s1, s2), cout in self.aretes:
                if sommet == s1:  # Assure que l'arête est traitée une seule fois
                    print(f"  -> {s2} (coût: {cout})")

    def afficher_sommets(self):
        print("Sommets accessibles:")
        for sommet, valeur in self.sommets.items():
            print(f"  {sommet} ({valeur})")

    def afficher_graphe_matplotlib(self):
        fig, ax = plt.subplots()
        
        # Dessiner les sommets et les arêtes
        for sommet, valeur in self.sommets.items():
            x, y = sommet
            if sommet == self.depart:
                ax.plot(x, y, 'go', markersize=10)  # Départ en vert
            elif sommet == self.arrivee:
                ax.plot(x, y, 'ro', markersize=10)  # Arrivée en rouge
            else:
                ax.plot(x, y, 'bo')  # Sommets en bleu
        
        # Dessiner les obstacles
        for i, ligne in enumerate(self.reseau):
            for j, cellule in enumerate(ligne):
                if cellule == 0:  # Obstacle
                    ax.plot(j, i, 'ks')  # Obstacles en noir
        
        # Dessiner les arêtes
        for arete, cout in self.aretes:
            x1, y1 = arete[0]
            x2, y2 = arete[1]
            ax.plot([x1, x2], [y1, y2], 'gray')  # Arêtes en gris
        
        ax.invert_yaxis()  # Inverser l'axe Y pour correspondre à la disposition matricielle
        plt.axis('equal')  # Garder les proportions égales
        
        # Légende
        depart_patch = mpatches.Patch(color='green', label='Départ')
        arrivee_patch = mpatches.Patch(color='red', label='Arrivée')
        sommet_patch = mpatches.Patch(color='blue', label='Sommet')
        obstacle_patch = mpatches.Patch(color='black', label='Obstacle')
        plt.legend(handles=[depart_patch, arrivee_patch, sommet_patch, obstacle_patch])
        
        plt.show()

    def get_voisins(self, sommet):
        voisins = []
        for (autre_sommet, cout) in self.aretes:
            if sommet == autre_sommet[0]:
                voisins.append((autre_sommet[1], cout))
            elif sommet == autre_sommet[1]:
                voisins.append((autre_sommet[0], cout))
        return voisins

    def get_cout(self, sommet1, sommet2):
        for (s1, s2), cout in self.aretes:
            if (s1 == sommet1 and s2 == sommet2) or (s1 == sommet2 and s2 == sommet1):
                return cout
        return None

    def get_valeur(self, sommet):
        return self.sommets[sommet]

    def write_reseau_in_file(self):
        with open(self.path + '/' + self.file_name+'_rewrite'+self.extension, 'w') as fichier:
            fichier.write(f"{len(self.reseau)} {len(self.reseau[0])}\n")
            for i in range(len(self.reseau)):
                fichier.write(' '.join(map(str, self.reseau[i])))
                fichier.write('\n')

    def write_data_in_file(self):
        with open(self.path + '/' + 'data_'+self.file_name+".dat", 'w') as fichier:
            fichier.write(f"nbNodes = {len(self.sommets)};\n")
            dep = str(self.depart).replace("(", "<").replace(")", ">")
            fichier.write(f"s = {dep};\n")
            arr = str(self.arrivee).replace("(", "<").replace(")", ">")
            fichier.write(f"t = {arr};\n\n")

            fichier.write("Nodes = {\n")
            for sommet in self.sommets:
                fichier.write(f"\t<{sommet[0]},{sommet[1]}> // Sommet au point ({sommet[0]},{sommet[1]})\n")

            fichier.write("};\n\n")
            fichier.write("Arcs = {\n")
            for arc in self.aretes:
                arc = str(arc)
                arc2 = arc.replace("(", "<").replace(")", ">")
                arc2 = arc2.replace("<<", "<").replace(">>", ">")
                fichier.write(f"\t{arc2}\n")
            fichier.write("};\n")

    # def write_solution_in_file(self):
    #     # Voir comment s'écrit la solution
    #     with open(self.path + '/' + 'sol_'+self.file_name+self.extension, 'w') as fichier:
    #         fichier.write(f"{len(self.reseau)} {len(self.reseau[0])}\n")
    #         for i in range(len(self.reseau)):
    #             ligne = []
    #             for j in range(len(self.reseau[i])):
    #                 if (j, i) == self.depart:
    #                     ligne.append(2)
    #                 elif (j, i) == self.arrivee:
    #                     ligne.append(3)
    #                 elif (j, i) in self.sommets:
    #                     ligne.append(1)
    #                 else:
    #                     ligne.append(0)
    #             fichier.write(' '.join(map(str, ligne)))
    #             fichier.write('\n')

    def get_chemin(self):
        with open(self.path + '/' +self.file_name+ "_chemin" +self.extension, 'r') as fichier:
            lines = fichier.readlines()

            d = []
            for i, line in enumerate(lines):
                if line == "d = []":
                    return []
                if i == 0:
                    continue
                line = line.strip()
                elements = line.split(' ')
                for j, element in enumerate(elements):
                    if element == '[1':
                        d.append(j - 2)
                    if element == '1':
                        d.append(j - 2)
        print(d)
        pre_chemin = []
        for i, arc in enumerate(self.aretes):
            for j in d:
                if i == j:
                    pre_chemin.append(arc)

        # pre_chemin = [(((2, 0), (3, 0)), 1.0), (((5, 2), (6, 3)), 1.4142135623730951), (((1, 0), (2, 0)), 1.0), (((4, 1), (5, 2)), 1.4142135623730951), (((3, 0), (4, 1)), 1.4142135623730951)]
        pre_chemin2 = self.trier_chemin(pre_chemin)
        chemin = self.calc_chemin(pre_chemin2)
        return chemin

    def write_chemin(self, chemin):
        with open(self.path + '/' + "sol_" + self.file_name +self.extension, 'w') as file:
            file.write(f"{chemin}")

    def write_chemin_astar(self, chemin):
        with open(self.path + '/' + "sol_a_" + self.file_name + self.extension, 'w') as file:
            file.write(f"{chemin}")

    def trier_chemin(self, pre_chemin):
        chemin = []
        sommet_depart = self.depart
        while pre_chemin:
            arc = next((a for a in pre_chemin if a[0][0] == sommet_depart), None)
            if arc is None:
                break
            chemin.append(arc)
            sommet_depart = arc[0][1]
            pre_chemin.remove(arc)
        return chemin

    def calc_chemin(self, pre_chemin):
        chemin = []
        for arc in pre_chemin:
            sommet1, sommet2 = arc[0][0], arc[0][1]
            if not chemin:
                chemin.append(sommet1)
                chemin.append(sommet2)
            else:
                if sommet1 in chemin:
                    chemin.append(sommet2)
        return chemin

    def plot_chemin(self, chemin):
        if chemin == []:
            print("Pas de chemin trouvé")
            self.afficher_graphe_matplotlib()
            return 0
        fig, ax = plt.subplots()
        
        # Dessiner les arêtes
        for (s1, s2), cout in self.aretes:
            x1, y1 = s1
            x2, y2 = s2
            ax.plot([x1, x2], [y1, y2], 'gray')  # Arêtes en gris

        # Dessiner les sommets
        for sommet, valeur in self.sommets.items():
            x, y = sommet
            ax.plot(x, y, 'bo')  # Sommets en bleu

        # Dessiner les obstacles
        for i, row in enumerate(self.reseau):
            for j, val in enumerate(row):
                if val == 0:  # Obstacle
                    ax.plot(j, i, 'ks')  # Obstacles en noir

        # Dessiner le chemin de la solution
        if chemin is not None:
            chemin_np = np.array(chemin)
            ax.plot(chemin_np[:, 0], chemin_np[:, 1], 'r-', linewidth=2)  # Chemin en rouge

        # Marquer le départ et l'arrivée
        if self.depart:
            ax.plot(self.depart[0], self.depart[1], 'go', markersize=10)  # Départ en vert
        if self.arrivee:
            ax.plot(self.arrivee[0], self.arrivee[1], 'ro', markersize=10)  # Arrivée en rouge

        ax.invert_yaxis()  # Inverser l'axe Y pour correspondre à la disposition matricielle
        plt.axis('equal')  # Garder les proportions égales
        
        # Légende
        depart_patch = mpatches.Patch(color='green', label='Départ')
        arrivee_patch = mpatches.Patch(color='red', label='Arrivée')
        sommet_patch = mpatches.Patch(color='blue', label='Sommet')
        obstacle_patch = mpatches.Patch(color='black', label='Obstacle')
        chemin_patch = mpatches.Patch(color='red', label='Chemin')
        plt.legend(handles=[depart_patch, arrivee_patch, sommet_patch, obstacle_patch, chemin_patch])
        
        plt.show()
