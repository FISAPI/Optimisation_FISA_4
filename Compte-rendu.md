# Plus court chemin
Pour modéliser le problème du plus court chemin sous la forme d'un programme linéaire, nous pouvons utiliser les variables suivantes :

x(i,j) = 1 si l'arc (i,j) fait partie du chemin le plus court, 0 sinon<br>
Nous pouvons alors écrire le programme linéaire suivant :

Minimiser :<br>
∑{(i,j) ∈ A} c(i,j) * x(i,j) -> coût total du chemin le plus court<br>

Sous les contraintes :

- ∑{j : (i,j) ∈ A} x(i,j) - ∑{j : (j,i) ∈ A} x(j,i) = 0 pour tout sommet i différent de s et t (contrainte de flux)<br>
- ∑{j : (s,j) ∈ A} x(s,j) = 1 (contrainte de sortie de la source)<br>
- ∑{j : (j,t) ∈ A} x(j,t) = 1 (contrainte d'entrée dans la destination)<br>
- x(i,j) ∈ {0, 1} pour tout arc (i,j) (contrainte de binarité)<br>

où :

- A est l'ensemble des arcs du graphe<br>
- c(i,j) est le coût de l'arc (i,j)<br>
- s est la source<br>
- t est la destination<br>

La fonction objectif minimise le coût total du chemin le plus court. Les contraintes de flux garantissent que le chemin est continu et que chaque sommet a un flux entrant et sortant égal à zéro, sauf pour la source et la destination. Les contraintes de sortie de la source et d'entrée dans la destination garantissent que le chemin commence à la source et se termine à la destination. Les contraintes de distance garantissent que la distance du sommet t au sommet s est inférieure ou égale au coût total du chemin le plus court. Enfin, les contraintes de binarité garantissent que les variables x(i,j) ne prennent que des valeurs binaires.<br>

Cette modélisation permet de résoudre le problème du plus court chemin en utilisant un solveur de programme linéaire en nombres entiers, tel que GLPK, CPLEX ou Gurobi.

|   Reseau   |   CPLEX time  |   CPLEX fonction objective  |  Algo A* time |  Algo A* fonvtion objective |
|---    |:-:    |:-:    |:-:    |--:    |
|   5_10_1   |   11 secondes  |  11.8994949366117  |  0.38 secondes  |  11.8994949366117  |
|   5_10_2   |   10 secondes  |  11.6568542494924  |  3.11 secondes  |  11.6568542494924  |
|   10_10_1   |   09 secondes  |  8.65685424949238  |  0.20 secondes  |  8.65685424949238  |
|   10_10_2   |   10 secondes  |  13.4852813742386  |  44.31 secondes  |  13.4852813742386  |
|   20_20_1   |   13 secondes  |  26.9705627484771  |  trop long  |     |

# Le voyageur de commerce
### Enoncé du problème

Soit G = (S, A, D) un graphe non orienté complet, où S est l'ensemble des sommets, A est l'ensemble des arêtes et D est la matrice des coûts. On note n = |S| le nombre de sommets et m = |A| le nombre d'arêtes.

On définit les variables binaires x_ij pour chaque arête (i, j) ∈ A, telles que :

x_ij = 1 si l'arête (i, j) est dans le cycle hamiltonien,
x_ij = 0 sinon.
Le problème du voyageur de commerce peut alors être formulé sous forme d'un programme linéaire en nombres entiers (PLNE) comme suit :

### Minimiser : 
$∑_{(i, j) ∈ A} d(i, j) * x_{ij}$

### Sous les contraintes :

Degré des sommets :

$∑_{j ≠ i} x_{ij} = 2, ∀i ∈ S$ <br>

Élimination des sous-cycles :

$∑_{(i, j) ∈ A(W)} x_{ij} ≤ |W| - 1, ∀W ⊆ S, 2 ≤ |W| ≤ n - 2$
où $A(W)$ est l'ensemble des arêtes dont les deux sommets sont dans W.

Contrainte de binarité :

$x_{ij} ∈ {0, 1}, ∀(i, j) ∈ A$