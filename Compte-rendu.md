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
|   20_20_1   |   13 secondes  |  26.9705627484771  |     |     |