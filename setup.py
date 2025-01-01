from setuptools import setup, find_packages

# Obtenir le contenu du fichier README pour l'utiliser dans la description
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="math_module",  # Nom du module
    version="0.1",  # Version initiale
    author="Abiye Enzo",  
    author_email="abiyeenzo@gmail.com",
    description="Un module mathématique Python étendu avec des fonctionnalités supplémentaires",
    long_description=long_description,  # Description longue tirée du README
    long_description_content_type="text/markdown",  # Format du fichier README
    url="https://github.com/abiyeenzo/math_module",  # Lien vers le dépôt GitHub
    packages=find_packages(),  # Trouve automatiquement les paquets dans le dossier
    classifiers=[
        "Programming Language :: Python :: 3",  # Spécifie que ça fonctionne avec Python 3
        "Programming Language :: Python :: 3.8",  # Exemple avec Python 3.8, tu peux ajouter d'autres versions si nécessaire
        "License :: OSI Approved :: MIT License",  # Type de licence
        "Operating System :: OS Independent",  # Le module est indépendant du système d'exploitation
    ],
    python_requires='>=3.6',  # Version minimum de Python requise
    #install_requires=[ 
    #],
    test_suite='tests',  # Spécifie le répertoire de tests
    tests_require=[  # Dépendances nécessaires pour les tests
        "unittest", 
    ],
)
