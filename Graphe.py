import math

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
                        self.sommets[(i, j)] = valeur
                        if valeur == 2:
                            self.depart = (i, j)
                        elif valeur == 3:
                            self.arrivee = (i, j)

        # Construire les arêtes pour les sommets accessibles, incluant les diagonales
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for i in range(n):
            for j in range(m):
                if (i, j) in self.sommets:  # Si le sommet est accessible
                    for di, dj in directions:  # Adjacents et diagonales
                        if 0 <= i + di < n and 0 <= j + dj < m and (i + di, j + dj) in self.sommets:
                            cout = math.sqrt(di**2 + dj**2)
                            self.ajouter_arete((i, j), (i + di, j + dj), cout)

    def ajouter_arete(self, sommet1, sommet2, cout):
        self.aretes.append(((sommet1, sommet2), cout))

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

