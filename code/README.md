# Pokémon: projet informatique

## répertoire "data"

* Ce répertoire contient les fichiers d'origine, tous modifiés, ainsi que de nouveaux fichiers

* Le fichier "pokemon_first_gen.csv" contient :
  1. Toutes les données précédentes traduites en français
  2. `Catchrate` : Le taux de capture du pokémon, utilisé dans le calcul de capture
  3. `Move1`, `Move2`, `Move3`, `Move4` : L'indice des capacités par défaut du pokémon dans abilities.csv

* Le fichier "abilities.csv" contient toutes les capacités de la première génération, ainsi que leurs attributs :
  1. `Name` : le nom de la capacité
  2. `Type` : le type de la capacité
  3. `Nature` : la nature de la capacité (physique, spéciale ou de statut), qui indique notamment quels coefficients utiliser dans le calcul des dégâts
  4. `Power` : la puissance de la capacité qui intervient dans le calcul des dégâts (0 indique une capacité non offensive, 90000 un KO systématique)
  5. `Precision` : la précision de la capacité, qui indique la probabilité de réussite (en pourcentage) de celle-ci
  6. `PP` : (Power Point) le nombre maximal d'utilisations de la capacité (non utilisé)
  7. `LS` : (Lifesteal) indique si la capacité réalise un vol de vie (0 indique aucun vol de vie, 1 indique la moitié des dégâts infligés)
  8. `SD` : (Self-Damage) indique si le pokémon se blesse en utilisant cette capacité, c'est un coefficient qui indique la proportion de dégâts subis par rapport aux points de vie totaux du lanceur (1 signifie un quart, 4 la totalité)
  9. `newstatus` : indique une attaque tentant de changer le statut du pokémon adverse, "normal" indique aucun changement de statut
  10. `precision_status` : indique la probabilité de réussite (en pourcentage) du changement de statut. Si le changement de statut est le seul effet de la capacité, cette valeur est fixée à 100
  11. `seed` : indique si la capacité infecte le pokémon adverse (vampigraine), le cas échéant 1/8 de ses pv lui sont volés chaque tour
  12. `condition` : indique si la capacité requiert un statut spécifique du pokémon adverse pour réussir, "normal" signifie qu'il n'y a pas de prérequis
  13. `repeat` : indique si la capacité effectue plusieurs lancers en une seule fois, si oui le nombre de lancers est calculé aléatoirement entre 2 et 5 selon une formule indiquée dans pokemon.py
  14. `fixed` : nombre de dégâts fixes infligés par la capacité (0 si elle n'inflige pas de dégâts fixes)
  15. `heal` : indique si la capacité soigne le lanceur (toujours de la moitié de ses pv maximum)
  16. `functional` : indique si la capacité est correctement implantée dans le jeu

* Le fichier "pokemon_coordinates.csv" n'est pas utilisé, on a préféré un système de rencontres aléatoires

* Le fichier "terrain.csv" donne la disposition de la carte, chaque nombre indiquant un type de terrain

* Plusieurs images servant à initialiser la carte et le jeu

### Dans le répertoire "img" on trouve

* Des images correspondant aux sprites des différentes "tiles" de terrain

* Un dossier "combat" donnant les différents sprites utilisés pour initialiser l'écran de combat

### Dans le répertoire "sprites on trouve"

* Tous les sprites des pokémon de dos et de face, dans deux dossiers séparés, utilisés pour les combats

* Un fichier contenant tous les sprites et un script python permettant de les découper à partir de ce fichier


