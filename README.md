# bad_calculator
Nuit de l'informatique Worst Code Ever submission

prérequis: python3, [turtle](https://docs.python.org/3/library/turtle.html)

## Concept:
Une des premières choses qu'on nous a apprises en informatique à l'ESIROI est: ne réinventez pas la roue. Alors nous avons décidé pour ce challenge de faire exactement l'inverse: redéfinir les opérateurs basiques. Par exemple, refaire la fonction diviser en évitant les erreurs liées à la division par 0 ou par des mauvais types de variables... au prix de performances désastreuses. Après avoir fait de même pour l'addition et la multiplication, il ne nous restait plus qu'à faire une calculatrice simple, permettant de montrer l'inefficacité exceptionelle de notre programme. Mais ce n'était que la première étape. Il nous fallait renier toutes les bonnes habitudes apprises, et complètement mutiler notre code.

## Procédés utilisés:
- Utilisation du moins de fonctions possible
- Toutes les variables et les fonctions nommées avec des noms similaires
- Définition de fonctions remplaçant les opérateurs mathématiques de base avec une efficacité médiocre, et une complexité inutilement élevée
- Utlisation du plus de one-liners possibles: fonctions lambdas, point-virgule...
- Boucles ne s'éxecutant qu'une fois
- commentaires irréguliers et inutiles (sauf un, ligne 21)
- distances d'indentation irrégulières