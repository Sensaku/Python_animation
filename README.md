# Python_animation
Petits animations faites en Python

## 1. Utilisation:
Les animations sont faites en MVC via tkInter: [base script](https://github.com/Sensaku/Python_animation/blob/main/Base%20script/animation.py)

Le script fournis la base suffisante pour lancer l'animation.

*Attention* : certaines méthodes du canvas de tkinter nécessite une version Python **3.8 ou supérieur** pour être présente.

## 2. Les méthodes
La méthode **animation** est le contrôleur de l'animation qui déclenchera frame par frame les fonctions nécessaire à l'animation.

La méthode **dessiner** est la fonction qui permettra de présenter notre vue, c'est à dire, placer dans le monde nos objets simulé.

La méthode **suivant** s'occupe de mettre à jour les données du *monde* de l'animation.

Les données du monde sont déclarées dans le constructeur.
