# PolyChess
Projet de création d'un jeu d'échec en Python

# Objectif
Ce dépot à pour but de créer un jeu d'échec.
Le programme permet de jouer aux échecs et peut déplacer les pièces selon leur mouvements officels, dans un échiquier de 8x8 cases. Le programme permet de faire des parties entre 2 joueurs ou avec un joueur et une IA.

`Voici la représentation de l'échiquier de base :`

<img class="ChessBoard" src="https://user-images.githubusercontent.com/56953297/71244403-b74ece00-2312-11ea-83d9-d85f36f7e0e5.png" width="340px">

Avec des chiffres pour la hauteur et des lettres pour la largeur.

On ne peut jouer qu'à la version standard des échecs, il n'y a pas de variantes possible.

Pour ceux qui ne connaissent pas le fonctionnement des échecs voici un rappel.
Le jeu oppose un joueur blanc contre un joueur noir. Le but est de mettre en échec et mat le roi adverse (c'est à dire dans l'impossibilité de se déplacer sans être menacé), à l'aide de ses propres pièces. Les pièces peuvent se déplacer dans l'échiquier selon différentes règles.
* Le Pion : il peut se déplacer uniquement en avant dans le sens des chriffres (vers le 8 si le joueur est blanc et vers le 1 si le joueur est noir). Le pion a trois déplacements possible. Classique, il avance d'une case vers une case vide. Premier déplacement, si le pion ne s'est pas encore déplacer il peut avancer de 2 cases en passant par deux cases vides. Prise, le pion peut prendre une pièce adverse située en diagonale vers l'avant (exemple : un pion blanc en b2 peut prendre en a3 ou c3). À part pour le pion, toute les pièce on un déplacement et une prise identique.
* La Tour : elle n'a qu'un seul déplacement, en ligne droite jusqu'à une case vide, ou jusqu'à une pièce adverse dont elle prendra la position. Sans limite de nombre de cases.
* Le Roi : c'est la pièce a protéger, elle peut se déplacer ou prendre sur toute ses cases adjacentes (jusqu'à 8 cases autour d'elle).
* Le Fou : Il se déplace en diagonale, sans limite de case.
* Le Cavalier : C'est la seule pièce qui peut passer par dessus les pièces (adverses comme alliées). Son déplacement s'effectue en "L", soit de deux cases en ligne droite dans n'importe quel direction et d'une case dans une direction parallèle à cette dernière. Le cavalier peut avoir jusqu'à 8 choix possible.
* La Dame : C'est la pièce la plus puissante, elle dispose des déplacements de la tour et du fou.

Il existe des déplacements spéciaux que le programme permet : 
* Le roque : il existe deux types de roque, le petit et le grand roque. Le petit roque consiste a déplacer le roi de deux cases vers la tour, et la tour de deux cases vers le roi, ce qui a pour conséquence de faire passer la tour par dessus le roi. Le grand roque est comme le petit, sauf que la tour se déplace de 3 cases. Il est possible d'effectuer un roque qu'une seule fois par partie. Un joueur peut roquer uniquement si la tour et le roi n'ont pas quitter leur position initial, de plus, les cases entre la tour et le roi doivent être inocupées. Le roi peut cependant avoir subis des échecs au préalable, du moment qu'il n'a pas bougé.
* Prise en passant : elle concerne les pions. Si un pion adverse est situé sur la 5e rangée (ligne n4 ou n5 si le joueur est blanc ou noir) et qu'on avance un pion allié d'une colonne adjacente de 2 cases, jusqu'à rejoindre la rangée du pion adverse, ce dernier peut alors manger le pion adverse en se déplaçant en diagonale et ainsi se situer sur la case de même colonne que le pion allié et sur la rangée inférieur au pion allié. Cette action n'est possible que le coup immédiatement suivant le déplacement du pion allié. 
* Pion à l'arrivée (promotion) : Lorsqu'un pion rejoint la dernière rangée (la 8e pour les blancs et la 1ere pour les noirs) il se transforme en n'importe quel autre pièce alliée, sauf le roi, et dispose de toutes les propriétés de la pièce transformée.


Le programme permet donc aux pièces de se déplacer uniquement selon leur déplacements expliqués précédemment.
Pendant la partie, le programme permet le déplacement de pièces de manière classique mais est aussi capable de reconnaitre certaines situations et ainsi modifier les coups possibles.
* Il peut détecter lorsque qu'un roi est en échec. Le programme empèche un joueur de se mettre en échec pendant son propre tour, ce qui a pour conséquence d'obliger un joueur à ne plus être en échec si son adversaire l'a mis en échec. Le déplacement d'une pièce doit donc remplir les conditions de déplacements classique ainsi que la non-mise en échec de son propre roi.
* Le programme est capable de reconnaitre un échec et mat, ce qui signifie que le roi est mis en échec et que le joueur ne dispose d'aucun coup pour ne plus être en échec, il a donc perdu, le programme termine la partie

* Cas où le programme annonce une partie nulle :
  * Le Pat : c'est lorsqu'un joueur n'est pas en échec mais il ne peut plus rien jouer, sans se mettre en échec par lui même. Le programme arrête alors aussi la partie : il n'y a pas de vainqueur.
  * Absence de matériel : les deux joueurs n'ont plus de pièces à part leur roi respectif. Cela fonctionne aussi si un joueur n'a plus qu'un roi et que l'autre n'a qu'un roi et un seul fou, ou un seul cavalier. En effet, il est impossible de mettre en échec et mat sans matériel, ou avec un seul fou ou cavalier.
  * Répétition : si une postition est répétée trois fois, la partie s'arrête.
  * Les 50 coups : si les joueurs jouent 50 coups sans déplacer un pion ou prendre une pièce adverse, la partie s'arrête.

