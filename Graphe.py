import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class Graphe:
    def __init__(self):
        self.reseau = []  # Représentation du réseau (matrice)
        self.sommets = {}  # Informations sur les sommets (uniquement ceux accessibles)
        self.aretes = []  # Liste des arêtes (sommets connectés et leur coût)
        self.depart = None
        self.arrivee = None

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

