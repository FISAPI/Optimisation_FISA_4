import math


class Noeud:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f


def heuristique(a, b, heuristique_choice=1):
def heuristique(a, b, heuristique_choice=1):
    (x1, y1) = a
    (x2, y2) = b
    # Dans notre cas, on peut aussi utiliser la distance de Manhattan
    # return abs(x1 - x2) + abs(y1 - y2)
    # Ou a distance en ligne droite
    # return max(abs(x1 - x2), abs(y1 - y2))
    if heuristique_choice == 1 :
        return 0
    elif heuristique_choice == 2:
        return max(abs(x1 - x2), abs(y1 - y2))
    else:
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    # Pour le réseau_5_10_1, le même chemin est trouvé avec les 2 heuristiques : [(2, 0), (3, 1), (4, 2), (5, 3), (6, 2), (7, 2), (8, 3), (9, 2), (9, 1), (8, 0)]
    # Pour le réseau_5_10_2, le même chemin est trouvé avec les 2 heuristiques : [(2, 1), (2, 2), (3, 3), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 3), (8, 2), (7, 2)]
    # Pour le réseau_10_10_1, le même chemin est trouvé avec les 2 heuristiques : [(3, 1), (4, 2), (5, 2), (6, 3), (7, 3), (8, 3), (9, 4), (8, 5)]
    # Pour le réseau_10_10_2, le même chemin est trouvé avec les 2 heuristiques : [(6, 2), (5, 1), (4, 0), (3, 0), (2, 1), (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (2, 7), (1, 8)]


def a_star(graphe, depart, arrivee, heuristique_choisie=1):
    noeud_depart = Noeud(depart)
    noeud_arrivee = Noeud(arrivee)
    noeud_depart.h = heuristique(noeud_depart.position, noeud_arrivee.position, heuristique_choice)
    noeud_depart.f = noeud_depart.h

    open_set = [noeud_depart]
    closed_set = set()

    while open_set:
        # Trouver le noeud dans open_set avec la plus petite valeur de f
        noeud_courant = min(open_set, key=lambda o: o.f)
        open_set.remove(noeud_courant)

        if noeud_courant.position == noeud_arrivee.position:
            chemin = []
            while noeud_courant:
                chemin.append(noeud_courant.position)
                noeud_courant = noeud_courant.parent
            return chemin[::-1]  # Retourner le chemin en partant du départ

        closed_set.add(noeud_courant.position)

        voisins = graphe.get_voisins(noeud_courant.position)
        for (voisin_position, cout) in voisins:
            if voisin_position in closed_set:
                continue
            
            noeud_voisin = Noeud(voisin_position, noeud_courant)

            tentative_g_score = noeud_courant.g + cout
            if tentative_g_score >= noeud_voisin.g and noeud_voisin in open_set:
                continue

            noeud_voisin.g = tentative_g_score
            noeud_voisin.h = heuristique(noeud_voisin.position, noeud_arrivee.position, heuristique_choisie)
            # noeud_voisin.h = heuristique(noeud_voisin.position, noeud_arrivee.position)
            noeud_voisin.f = noeud_voisin.g + noeud_voisin.h

            if noeud_voisin not in open_set:
                open_set.append(noeud_voisin)

    return None  # Aucun chemin trouvé