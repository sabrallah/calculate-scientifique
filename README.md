# Calculatrice Scientifique

Une calculatrice scientifique complète développée en Python avec interface graphique Tkinter.

## Fonctionnalités

- Opérations arithmétiques de base (addition, soustraction, multiplication, division)
- Fonctions trigonométriques (sin, cos, tan)
- Fonctions logarithmiques (log, ln)
- Constantes mathématiques (π, e)
- Racine carrée, puissances, valeur absolue
- Mode d'angle: radians (RAD) ou degrés (DEG)
- Interface utilisateur intuitive avec code couleur
- Support des raccourcis clavier

## Comment exécuter la calculatrice

### Prérequis
- Python 3.x installé sur votre ordinateur
- Module Tkinter (généralement inclus avec Python)

### Étapes pour lancer la calculatrice
1. Ouvrez un terminal ou une invite de commande
2. Naviguez jusqu'au répertoire contenant le fichier `calculatrice.py`
   ```
   cd chemin/vers/calculatrice_scientifique
   ```
3. Exécutez le programme Python
   ```
   python calculatrice.py
   ```

## Guide d'utilisation

### Interface
- L'écran en haut affiche l'entrée et le résultat des calculs
- L'indicateur "RAD" ou "DEG" indique le mode d'angle actuel (radians ou degrés)
- Les boutons sont organisés par catégorie avec un code couleur:
  - Gris: chiffres et point décimal
  - Jaune: opérateurs arithmétiques
  - Bleu: fonctions scientifiques
  - Rouge: effacement (C et ⌫)
  - Vert: touche égal (=)
  - Violet: bouton de basculement RAD/DEG

### Modes d'angle
- **RAD** (Radians): Utilisé pour les calculs où les angles sont exprimés en radians (mode par défaut)
- **DEG** (Degrés): Utilisé pour les calculs où les angles sont exprimés en degrés
- Basculez entre les deux modes en cliquant sur le bouton "RAD/DEG"

### Fonctions clés
- **sin, cos, tan**: Fonctions trigonométriques (tiennent compte du mode RAD/DEG)
- **log**: Logarithme décimal (base 10)
- **ln**: Logarithme naturel (base e)
- **√**: Racine carrée
- **x²**: Élévation au carré
- **π**: Constante Pi (3.14159...)
- **e**: Constante d'Euler (2.71828...)
- **|x|**: Valeur absolue
- **C**: Effacer tout le calcul
- **⌫**: Effacer le dernier caractère

### Raccourcis clavier
- Chiffres et opérateurs: touches correspondantes du clavier
- Calcul: Touche Entrée ou =
- Effacer: Touche c (pour tout effacer) ou Retour arrière (pour le dernier caractère)
- Fonctions scientifiques:
  - s: sin
  - o: cos
  - t: tan
  - l: log
  - n: ln
  - r: racine carrée
  - p: pi
  - e: e
  - a: valeur absolue
  - ^: puissance 2
  - d: basculer entre radians et degrés