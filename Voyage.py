import math
import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

import random
import numpy as np

class Voyage:
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
            self.file_name = "default_graphe"
            self.extension = ".txt"
            self.path = "exos"
            
    def lire_graphe_fichier(self, nom_fichier):
        self.reseau = []
        self.sommets = {}
        self.aretes = []

        with open(nom_fichier, 'r') as fichier:
            lignes = fichier.readlines()

        # Parcourir les lignes du fichier
        for ligne in lignes:
            # Ignorer les lignes vides ou les lignes de commentaire
            if not ligne.strip() or ligne.strip().startswith('//'):
                continue

            # Extraire les informations sur les sommets
            sommet_match = re.match(r'<(\d+),(\d+)>', ligne.strip())
            if sommet_match:
                i, j = map(int, sommet_match.groups())
                self.sommets[(i, j)] = 1
                continue

            # Extraire les informations sur les arcs
            arc_match = re.match(r'<<(\d+),(\d+)>, <<(\d+),(\d+)>, (-?\d*\.?\d+)>', ligne.strip())
            # <<0,8>, <<9,0>, 13.0000000000>
            print("arc_match: ", arc_match)
            if arc_match:
                print("arc_match: ", arc_match)
                i1, j1, i2, j2, cout = map(float, arc_match.groups())
                sommet1 = (int(i1), int(j1))
                sommet2 = (int(i2), int(j2))
                self.ajouter_arete(sommet1, sommet2, cout)
            
        print("Sommets: ", self.sommets)
        print("Aretes: ", self.aretes)
        # Créer la matrice d'adjacence
        n = max(max(i, j) for i, j in self.sommets) + 1
        self.reseau = [[0] * n for _ in range(n)]
        for (sommet1, sommet2), cout in self.aretes:
            i1, j1 = sommet1
            i2, j2 = sommet2
            self.reseau[i1][j1] = 1
            self.reseau[i2][j2] = 1
    
    def ecrire_graphe_fichier(self, nom_fichier):
        with open(nom_fichier, 'w') as fichier:
            # Écrire le nombre de sommets
            n = len(self.sommets)
            fichier.write(f"nbNodes = {n};\n")

            # Écrire les sommets
            fichier.write("Nodes = {\n")
            for sommet in self.sommets:
                i, j = sommet
                fichier.write(f"\t<{i},{j}> // Sommet au point ({i},{j})\n")
            fichier.write("};\n\n")

            # Écrire les arcs
            fichier.write("Arcs = {\n")
            for (sommet1, sommet2), cout in self.aretes:
                i1, j1 = sommet1
                i2, j2 = sommet2
                fichier.write(f"\t<<{i1},{j1}>, <<{i2},{j2}>, {cout:.10f}>\n")
            fichier.write("};\n")

    def ajouter_arete(self, sommet1, sommet2, cout):
        # vérification que l'arete n'existe pas déjà peut importe le coût : 
        for arete in self.aretes:
            if arete[0] == (sommet1, sommet2) or arete[0] == (sommet2, sommet1):
                return
        
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
        
        
        # Dessiner les arêtes avec les couts
        for arete, cout in self.aretes:
            x1, y1 = arete[0]
            x2, y2 = arete[1]
            ax.plot([x1, x2], [y1, y2], 'gray')  # Arêtes en gris
            ax.text((x1 + x2) / 2, (y1 + y2) / 2, f"{cout:.2f}", color='gray')
            
        
        ax.invert_yaxis()  # Inverser l'axe Y pour correspondre à la disposition matricielle
        plt.axis('equal')  # Garder les proportions égales
        
        # Légende
        sommet_patch = mpatches.Patch(color='blue', label='Sommet')
        plt.legend(handles=[sommet_patch])
        
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
    
    def write_data_2_in_file(self):
        with open(self.path + '/' + 'data_'+self.file_name+".dat", 'w') as fichier:
            fichier.write(f"n = {len(self.sommets)};\n")
            fichier.write(f"cout=[")
            for sommetdep in self.sommets:
                fichier.write(f"[")
                for sommetarr in self.sommets:
                    cout = self.get_cout(sommetdep, sommetarr)
                    if cout is None:
                        cout = 10000
                    if sommetarr == sommetdep:
                        cout = 20000
                    fichier.write(f"{cout},")
                fichier.write(f"],\n")
            fichier.write(f"];\n")

    def write_chemin(self, chemin):
        with open(self.path + '/' + "sol_" + self.file_name +self.extension, 'w') as file:
            file.write(f"{chemin}")

    def trier_chemin(self, pre_chemin):
        chemin = []
        if self.depart is not None:
            sommet_depart = self.depart
        else:
            sommet_depart = pre_chemin[0][0][0]
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
    
    def get_chemin_voyageur(self):
         with open(self.path + '/' +self.file_name+ "_chemin" +self.extension, 'r') as fichier:
            lines = fichier.readlines()

            d = []
            for i, line in enumerate(lines):
                pass
                
    def lire_tableau_aretes_fichier(self, nom_fichier):
        with open(nom_fichier, 'r') as fichier:
            lignes = fichier.readlines()

        tableau = []
        for ligne in lignes:
            row = list(map(int, ligne.strip().split()))
            tableau.append(row)

        tableau = np.array(tableau)

        pre_chemin = []

        n = len(tableau)
        for i, sommet1 in enumerate(self.sommets):
            for j, sommet2 in enumerate(self.sommets):
                if tableau[i][j] == 1:
                    pre_chemin.append(((sommet1, sommet2), self.get_cout(sommet1, sommet2)))
        pre_chemin2 = self.trier_chemin(pre_chemin)
        chemin = self.calc_chemin(pre_chemin2)
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

        if self.depart:
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
        sommet_patch = mpatches.Patch(color='blue', label='Sommet')
        chemin_patch = mpatches.Patch(color='red', label='Chemin')
        plt.legend(handles=[sommet_patch, chemin_patch])
        
        plt.show()
    
    def create_random_graphe(self, n, m, s, p):

        self.reseau = [[0 for _ in range(m)] for _ in range(n)]
        
        # Créer s sommets et les répartir dans le réseau
        for _ in range(s):
            x = random.randint(0, m-1)
            y = random.randint(0, n-1)
            while (x, y) in self.sommets:
                x = random.randint(0, m-1)
                y = random.randint(0, n-1)
            self.reseau[y][x] = 1
            self.ajouter_sommet((x, y), self.reseau[y][x])

        for sommet1 in self.sommets:
            for sommet2 in self.sommets:
                if sommet1 != sommet2 and ((sommet1, sommet2),_) not in self.aretes and ((sommet2, sommet1),_) not in self.aretes:
                    if random.random() < p:
                            cout = random.randint(10,50)
                            self.ajouter_arete(sommet1, sommet2, cout)
