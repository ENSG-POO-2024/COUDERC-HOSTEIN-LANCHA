import numpy as np

'''
Ce fichier gère les types ainsi que leurs interactions

Il contient un tableau numpy "efficiencies" qui donne le multiplicateur à appliquer en combat
Les lignes correspondent au type offensif, les colonnes au type défensif

Le dictionnaire "dic" permet une correspondance entre le nom des types et l'indice de la  colonne ou ligne associée dans le tableau

En pratique, les types "steel", "dark" et "fairy" n'étant pas implantés dans la première génération des jeux pokémon, on ne les utilise pas ici

Le type "neutral" n'existe pas réellement, il sert à gérer les doubles types (si le pokémon n'a qu'un seul type, il se voit attribuer 'neutral' en second type)
ainsi que la capacité lutte, qui a toujours la même efficacité quel que soit le type (en pratique cette capacité est correctement implantée mais pas utilisée)
'''

efficiencies = np.array([
    [0.5,1  ,1  ,0.5,0.5,0.5,2  ,2  ,1  ,1  ,1  ,1  ,1  ,2  ,1  ,1  ,1  ,1  ,1  ],
    [2  ,1  ,1  ,1  ,1  ,1  ,0.5,2  ,0.5,2  ,1  ,0.5,0.5,2  ,1  ,0  ,2  ,0.5,1  ],
    [0.5,1  ,2  ,1  ,1  ,1  ,0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ],
    [1  ,1  ,0.5,0.5,1  ,2  ,1  ,1  ,1  ,1  ,0.5,1  ,1  ,2  ,2  ,1  ,1  ,1  ,1  ],
    [1  ,1  ,0.5,2  ,0.5,1  ,1  ,1  ,1  ,1  ,0.5,1  ,1  ,1  ,0  ,1  ,1  ,2  ,1  ],
    [2  ,1  ,0.5,0.5,1  ,0.5,1  ,2  ,2  ,1  ,2  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ,1  ],
    [0.5,2  ,2  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ,2  ,1  ,1  ],
    [0.5,1  ,2  ,0.5,1  ,0.5,1  ,0.5,1  ,1  ,2  ,1  ,1  ,1  ,2  ,1  ,1  ,2  ,1  ],
    [0.5,0.5,1  ,1  ,1  ,0.5,0.5,1  ,1  ,1  ,2  ,0.5,2  ,1  ,1  ,0.5,2  ,0.5,1  ],
    [0.5,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,0.5,1  ,0  ,1  ,1  ,1  ],
    [0.5,1  ,0.5,2  ,1  ,0.5,1  ,1  ,0.5,1  ,0.5,0.5,1  ,2  ,2  ,1  ,1  ,0.5,1  ],
    [0  ,1  ,1  ,1  ,1  ,1  ,2  ,1  ,1  ,1  ,2  ,0.5,1  ,0.5,0.5,0.5,1  ,1  ,1  ],
    [0.5,2  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,2  ,0.5,1  ,1  ,1  ,0  ,1  ,1  ],
    [0.5,0.5,1  ,1  ,1  ,2  ,1  ,2  ,2  ,1  ,1  ,1  ,1  ,1  ,0.5,1  ,1  ,2  ,1  ],
    [2  ,1  ,1  ,1  ,2  ,2  ,1  ,1  ,0.5,1  ,0.5,2  ,1  ,2  ,1  ,1  ,1  ,0  ,1  ],
    [1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,0  ,1  ,1  ,2  ,1  ,1  ,2  ,0.5,1  ,1  ],
    [1  ,0.5,1  ,1  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ,1  ,2  ,1  ,1  ,2  ,0.5,1  ,1  ],
    [0.5,2  ,1  ,1  ,0.5,1  ,1  ,1  ,2  ,1  ,2  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ,1  ],
    [1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ]
    ])

dic = {"steel":0,"fighting":1,"dragon":2,"water":3,"electric":4,"fire":5,"fairy":6,"ice":7,"bug":8,"normal":9,"grass":10,"poison":11,"psychic":12,"rock":13,"ground":14,"ghost":15,"dark":16,"flying":17,"neutral":18}
