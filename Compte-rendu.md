Pour modéliser le problème du plus court chemin sous la forme d'un programme linéaire, nous pouvons utiliser les variables suivantes :

x(i,j) = 1 si l'arc (i,j) fait partie du chemin le plus court, 0 sinon<br>
d(i) = distance du sommet i au sommet s (la source) (comprendre la somme des coûts entre des sommets parcourus)<br>
Nous pouvons alors écrire le programme linéaire suivant :

Minimiser :<br>
∑{(i,j) ∈ A} c(i,j) * x(i,j)

Sous les contraintes :

- ∑{j : (i,j) ∈ A} x(i,j) - ∑{j : (j,i) ∈ A} x(j,i) = 0 pour tout sommet i différent de s et t (contrainte de flux)<br>
- ∑{j : (s,j) ∈ A} x(s,j) = 1 (contrainte de sortie de la source)<br>
- ∑{j : (j,t) ∈ A} x(j,t) = 1 (contrainte d'entrée dans la destination)<br>
- d(t) - d(i) + M * x(i,j) <= c(i,j) pour tout arc (i,j) (contrainte de distance)<br>
- x(i,j) ∈ {0, 1} pour tout arc (i,j) (contrainte de binarité)<br>

où :

- A est l'ensemble des arcs du graphe<br>
- c(i,j) est le coût de l'arc (i,j)<br>
- M est une constante suffisamment grande pour garantir que la contrainte de distance soit satisfaite si x(i,j) = 0<br><br>

La fonction objectif minimise le coût total du chemin le plus court. Les contraintes de flux garantissent que le chemin est continu et que chaque sommet a un flux entrant et sortant égal à zéro, sauf pour la source et la destination. Les contraintes de sortie de la source et d'entrée dans la destination garantissent que le chemin commence à la source et se termine à la destination. Les contraintes de distance garantissent que la distance du sommet t au sommet s est inférieure ou égale au coût total du chemin le plus court. Enfin, les contraintes de binarité garantissent que les variables x(i,j) ne prennent que des valeurs binaires.<br>

Cette modélisation permet de résoudre le problème du plus court chemin en utilisant un solveur de programme linéaire en nombres entiers, tel que GLPK, CPLEX ou Gurobi.