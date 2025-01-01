# Math Module

Bienvenue dans le projet **Math Module**, une bibliothèque Python qui étend les fonctionnalités du module `math` standard avec des outils et fonctions supplémentaires. Cette bibliothèque est conçue pour offrir des calculs avancés en mathématiques, y compris des fonctions statistiques, trigonométriques, combinatoires, et bien plus encore.

## Fonctionnalités

Ce module ajoute de nombreuses fonctionnalités que le module `math` de Python ne couvre pas directement :

### 1. **Fonctions combinatoires avancées**
   - **Combinaisons et permutations avec validation des entrées**.
   - Gestion des erreurs pour des entrées invalides (par exemple, nombre négatif).

### 2. **Calculs trigonométriques**
   - Fonctions trigonométriques standard comme `sin`, `cos`, `tan`.
   - Calcul des valeurs trigonométriques en degrés, radians et autres systèmes d'unités.
   - **Séries de Taylor** pour approximations avancées.

### 3. **Fonctions statistiques**
   - Calcul de la moyenne, de la variance, et d'autres mesures statistiques.
   - Fonctions pour les moyennes mobiles, les séries statistiques, et plus encore.

### 4. **Gestion des matrices et des vecteurs**
   - Fonctions pour la multiplication de matrices, inversion de matrices, et calcul de déterminants.

### 5. **Calculs avancés sur les nombres complexes**
   - Fonctions pour travailler avec des nombres complexes en utilisant des transformations avancées (par exemple, transformées de Fourier).

### 6. **Précision et nombres rationnels**
   - Manipulation des nombres avec une précision arbitraire grâce au module `decimal`.

### 7. **Autres outils mathématiques**
   - Résolution d'équations et calculs symboliques.
   - Fonctions pour des calculs géométriques et topologiques.

## Installation

Tu peux installer ce module en clonant le projet directement depuis GitHub :

```bash
git clone https://github.com/abiyeenzo/math_module.git
cd math_module
python setup.py install
```

Ou tu peux utiliser directement le fichier math_module.py dans ton projet.
Exemple d'utilisation

Voici quelques exemples de code pour utiliser les fonctions du module :
1. Calcul de la combinaison et permutation avec validation des entrées :

```bash
from math_module import comb, perm

# Exemple de combinaison
print(comb(5, 3))  # Affiche 10

# Exemple de permutation
print(perm(5, 3))  # Affiche 60
```

2. Calcul trigonométrique avec approximations par série de Taylor :

```bash
from math_module import taylor_sin

# Approximation de sin(x) avec 10 termes de la série de Taylor
print(taylor_sin(45))
```

3. Calcul statistique de moyenne et variance :

```bash
from math_module import moyenne, variance

data = [1, 2, 3, 4, 5]
print(moyenne(data))  # Affiche 3.0
print(variance(data))  # Affiche 2.0
```

## Tests

Le module est couvert par un ensemble de tests unitaires pour garantir son bon fonctionnement. Pour exécuter les tests, utilise la commande suivante :

```bash
python -m unittest test_math.py
```

Les tests vérifient la fonctionnalité de toutes les fonctions importantes, y compris les tests de validation des entrées et de calculs sur les matrices et vecteurs.
Contribuer

Les contributions sont les bienvenues ! Si tu souhaites ajouter de nouvelles fonctionnalités ou améliorer le module, voici comment contribuer :

    Fork ce dépôt.
    Crée une branche pour ta fonctionnalité (git checkout -b feature/nouvelle-fonction).
    Commit tes modifications (git commit -am 'Ajout de nouvelles fonctionnalités').
    Pousse ta branche (git push origin feature/nouvelle-fonction).
    Ouvre une Pull Request pour que nous puissions examiner ta contribution.

## Licence

Ce projet est sous la licence MIT. Voir le fichier LICENSE pour plus de détails.
Auteurs

    Abiye Enzo - Développeur principal
    


### Ce que ce `README.md` inclut :
- **Introduction et fonctionnalités** : Une explication des ajouts importants de ce module, ce qu'il couvre, et ce que `math` standard ne fait pas.
- **Instructions d'installation** : Comment installer et utiliser le module.
- **Exemples de code** : Montrant comment utiliser différentes fonctions du module.
- **Tests** : Indications sur la façon de tester le module.
- **Contribuer** : Comment les autres développeurs peuvent contribuer au projet.

