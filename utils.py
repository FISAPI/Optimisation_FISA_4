import math
from Graphe import Graphe


def creer_graphe_depuis_fichier(nom_fichier):
    graphe = Graphe()
    with open(nom_fichier, 'r') as fichier:
        n, m = map(int, fichier.readline().split())  # dimensions du réseau
        reseau = [fichier.readline().split() for _ in range(n)]  # Lecture du réseau

        for y in range(n):
            for x in range(m):
                graphe.ajouter_sommet(x, y)
                if reseau[y][x] in ['1', '2', '3']:
                    # Vérifier et ajouter des arêtes pour tous les voisins possibles
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and reseau[ny][nx] in ['1', '2', '3']:
                            distance = 1 if dx == 0 or dy == 0 else 2**0.5
                            graphe.ajouter_arete((x, y), (nx, ny), distance)
    return graphe, n, m