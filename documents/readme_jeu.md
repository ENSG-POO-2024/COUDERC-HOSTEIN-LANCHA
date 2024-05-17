Couderc-Lacour Philémon, Hostein Augustin-Pierre, Lancha Mélanie 


## README


# Utilisation de notre code : 

Pour lancer notre jeu, il faut ouvrir le dossier "code" puis le fichier "main.py".

En lançant le code, une fenêtre s’ouvre, demandant de choisir trois Pokémon. Il faut cliquer sur les trois Pokémon que l’on souhaite choisir pour commencer, puis fermer la fenêtre. Ce seront les trois Pokémon dont on disposera pour commencer. Une nouvelle fenêtre s’ouvre, il faut alors appuyer sur une flèche du clavier (n’importe laquelle) pour que le jeu se lance. Une fois le jeu lancé, on voit notre personnage sur une carte, et on peut le déplacer à l’aide des flèches du clavier. On peut également ouvrir le sac pour voir les Pokémon présents appuyant sur la touche S. Lorsque l’on se déplace sur la carte, on peut voir deux types de paysages : un paysage avec de la prairie, des hautes herbes et des arbres, et un paysage avec de la neige, de la glace et des cristaux. Il y a également un chemin, présent sur les deux types de paysages.  Le personnage ne peut pas se déplacer sur un arbre ou sur des cristaux, ce sont des obstacles. Lorsque le personnage se trouve dans les hautes herbes ou bien sur de la glace, il peut se faire attaquer par un Pokémon sauvage. 

Lors d’une attaque d’un Pokémon sauvage, un combat commence. L’interface de combat se lance et on a alors quatre choix possibles : 
    
* La fuite : lorsqu’on ne souhaite pas combattre, on peut choisir de fuir. Si la fuite réussit, l’interface de combat va se fermer et on se retrouve sur la carte de jeu à l’endroit où l’on s’est fait attaquer. Le succès ou non de la fuite est aléatoire, elle est plus probable si le Pokémon utilisé a une vitesse plus élevée que le Pokémon sauvage rencontré, et avec le nombre de tentatives de fuite. 

* Le changement de Pokémon : le Pokémon que l’on va faire combattre contre le Pokémon sauvage est celui qui est en premier dans le sac. Or, on peut vouloir faire combattre un autre Pokémon, pour changer de type de Pokémon par exemple. Ainsi, cette fonctionnalité permet d’ouvrir le sac de Pokémon, puis on peut changer l’ordre des Pokémon du sac afin de mettre en première position celui que l’on souhaite utiliser pour le combat.

* L’attaque : si on choisit d’attaquer, on a alors le choix parmi les quatre attaques que notre Pokémon possède. Chaque Pokémon possède quatre attaques, qui dépendent de son type entre autres. Lorsque l’on attaque, le Pokémon adverse va perdre ou non des pv, puis c’est cet adversaire qui va à son tour nous attaquer et nous infliger des dégâts. Si le Pokémon utilisé n’a plus de pv, le combat se termine. Certaines attaques sont plus efficaces selon le type du Pokémon qui les utilise et le type du Pokémon adverse. Certaines attaques permettent d’infliger un effet de statut au Pokémon adverse pour l’affaiblir. De plus, certaines attaques ne réussissent pas à tous les coups ! Les plus puissantes n’ont que 30% de réussite par exemple.

* La capture : on peut choisir de vouloir capturer le Pokémon sauvage, afin de l’ajouter dans notre sac. Tout comme la fuite, la réussite ou non de la capture dépend d’une probabilité, la capture n’est donc pas toujours une réussite. Cette probabilité dépend du nombre de pv restants au Pokémon adverse : moins il a de pv, plus la capture a de chances de réussir. Cependant, si le Pokémon adverse a 0 pv, le combat se termine et on ne peut pas le capturer. Un Pokémon capturé sera présent dans notre sac pour la suite de l’aventure. 
