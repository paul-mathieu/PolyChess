"""
#ia
"""


class IA:

    def __init__(self, echiquier, couleur):

        self.echiquier = echiquier

        self.couleur = couleur
        self.couleurOpposee = 'noir' if couleur == 'blanc' else 'blanc'

        self.valeurPieces = {
            ('Pion', self.couleur): -10,
            ('Tour', self.couleur): -50,
            ('Cavalier', self.couleur): -30,
            ('Fou', self.couleur): -30,
            ('Dame', self.couleur): -90,
            ('Roi', self.couleur): -900,
            ('Pion', self.couleurOpposee): 10,
            ('Tour', self.couleurOpposee): 50,
            ('Cavalier', self.couleurOpposee): 30,
            ('Fou', self.couleurOpposee): 30,
            ('Dame', self.couleurOpposee): 90,
            ('Roi', self.couleurOpposee): 900
        }

    def arbre_nFils_pProfondeur(self, n=5, echiquier=None,
                                p=3, niveauActuel=0):

        """
        Cette fonction permet d'optenir un TREE par recursivite.
        
        Elle renvoie les n meilleurs mouvements à realiser à partir 
        d'un nombre de points.
        
        Le nombre de points est definit en fonction d'une valeur affectee 
        à la piece ainsi qu'avec des points en moins si elle peut être 
        mangée après le déplacement.
        
        Chaque mouvement contient une liste des n meilleurs mouvements
        suivants, si l'adversaire aurait joue le coups suivant rapportant
        le plus grand nombre de points.
        """

        if echiquier == None:
            echiquier = self.echiquier

        listeMouvements = []
        niveauActuel += 1

        # si le niveau actuel est le maximum souhaité (ici 5), on ne va pas plus profondement
        if not niveauActuel > 3:

            # =================================================================
            # récupération des meilleurs mouvements
            # =================================================================

            listeMouvements = self.listeTousMeilleursMouvements(echiquier, niveauActuel)

            # on garde les meilleures valeurs
            listeMouvements = listeMouvements[0:n]

            # =================================================================
            # pour tous les n meilleurs mouvements
            # =================================================================

            # ~~ (ajout pour chaque mouvements des n meilleurs                ~~
            # ~~ mouvements suivants)                                         ~~

            for mouvement in listeMouvements:
                if niveauActuel == 1:
                    print((
                        echiquier.indexToNomCase(mouvement.indexDepart),
                        echiquier.indexToNomCase(mouvement.indexArrivee)
                    ))
                # le nouvel echiquier qui contiendra la piece deplacee
                echiquierTemp = echiquier

                # =============================================================
                # l'IA joue
                # =============================================================

                echiquierTemp.deplacerPieceEnIndex(mouvement.indexDepart,
                                                   mouvement.indexArrivee)

                # =============================================================
                # l'adversaire joue (théorie)
                # =============================================================

                # le nouvel echiquier doit contenir le meilleur coup de l'adversaire
                meilleurCoupAdversaire = self.listeTousMeilleursMouvements(echiquierTemp,
                                                                           niveauActuel)
                # meilleur mouvement sans profondeur
                meilleurCoupAdversaire = meilleurCoupAdversaire[0]

                # modification de l'échiquier
                echiquierTemp.deplacerPieceEnIndex(meilleurCoupAdversaire.indexDepart,
                                                   meilleurCoupAdversaire.indexArrivee)

                # =============================================================
                # mouvements possibles ensuite (recursivite)
                # =============================================================

                # variable avec les mouvements suivants 
                listeMouvementsSuivants = self.arbre_nFils_pProfondeur(n, echiquierTemp,
                                                                       p, niveauActuel)

                # ajout des mouvements suivant le mouvement actuel
                mouvement.set_listeMouvementsSuivants(listeMouvementsSuivants)

            #                print("_|_|_|_|_|_")
            #                print(index)
            #                print(echiquier.positions[0:3])
            #                print(echiquier.get_piece(index).nom)
            #                print(echiquier.positions[index].couleur)
            #

            return listeMouvements

    def listeTousMeilleursMouvements(self, echiquier, niveauProfondeur):

        """
        Cette fonction renvoie tous les déplacements possibles triés
        d'une couleur avec un obejet de la classe mouvement contenant :
            - l'index de la piece a deplacer
            - l'index d'arrivee de la piece a deplacer
            - les points affectes a la piece
            - le niveau de la profondeur du mouvement
            
        Cette fonction renvoie des objets Mouvement
        """

        listeMouvements = []

        # ~~~~ pour tous les mouvements de toutes les pieces ~~~~~~~~~~~~~~~

        # ~~ (calcul des points pour chaque piece)                        ~~

        # =====================================================================
        # pour toutes les pieces de la couleur pouvant être déplacées
        # =====================================================================

        #        print(echiquier.listePiecesPouvantEtreDeplacees(couleur))

        for index in echiquier.listePiecesPouvantEtreDeplacees(self.couleur):

            piece = echiquier.positions[index]

            #            print(echiquier.listeDesCoupsAvecVerif(index, self.couleur))

            #            if self.couleur == 'noir':
            #                listeCoupsPossibles = echiquier.listePiecesPouvantEtreDeplacees()
            #            elif self.couleur == 'blanc':
            #                listeCoupsPossibles = echiquier.listePiecesPouvantEtreDeplacees()
            #
            listeCoupsPossibles = echiquier.listePiecesPouvantEtreDeplacees(self.couleur)

            # pour tous les déplacements de la piece
            for indexArrivee in listeCoupsPossibles:
                valeurPiece = self.valeurPieces[(piece.nom, piece.couleur)]

                # moins de points si la piece peut se faire manger
                valeurPiece *= echiquier.coefficientPointsSiPeutEtreMangee(indexArrivee)

                # ou plus de points si la piece peut manger

                # moins de points si elle n'a aucune piece de la meme couleur autour
                #                valeurPiece *= echiquier.coefficientPointsSiPieceMemeCouleurProche(indexArrivee, self.couleur)

                # ajout d'un nouveau mouvement à la liste
                listeMouvements.append(Mouvement(index, indexArrivee, valeurPiece, niveauProfondeur))

        # ~~~~ Optimisation ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # ~~ (tri en gardant les n avec les plus de                           ~~
        # ~~ points                                                           ~~

        # on trie les elements par points
        listeMouvements = self.trierMouvements(listeMouvements)

        return listeMouvements

    def meilleurMouvement(self, listeMouvements=None, niveau=0, niveauMax=None):

        """
        Cette fonction retourne le meilleur mouvement a realiser d'apres
        le nombre de points qu'il rapporte
        
        Les points sont calcules de la maniere suivante :
            - points de chaque mouvement (niveau == 1)
            - points de chaque mouvement + moyenne des autres (niveau > 1)
        
        Le mouvement retourne est celui du niveau 1 donc le chemmin rapporte 
        le plus de points
        """

        #        print(listeMouvements)
        # à l'initialisation
        if niveau == 0:
            listeMouvements = self.arbre_nFils_pProfondeur()
        #            print('=====')

        #        print(listeMouvements)

        if niveauMax is None:
            niveauMax = 0
            premier_fils = listeMouvements[0]
            while not premier_fils.listeMouvementsSuivants == None:
                premier_fils = premier_fils.listeMouvementsSuivants[0]
                niveauMax += 1

        multiplicateur_de_niveau = dict(map(lambda x: (x, 1 - (x / niveauMax + 1)), range(niveauMax + 1)))
        #        print(multiplicateur_de_niveau)
        # ex pour niveauMax = 5 : {0: 1., 1: .8, 2: .6, 3: .4, 4: .2}

        maxPoints = 0

        for mouvement in listeMouvements:

            # si le meilleur chemin est sup à la valeur max

            # calcul des points pour ce mouvement avec le meilleur chemin
            # parmi ses enfants
            pointsNiveauActuel = mouvement.valeurPiece * multiplicateur_de_niveau[niveau]

            if not mouvement.listeMouvementsSuivants is None:
                #                print('niveau actuel : ' + str(niveau))
                pointsSuivants = self.meilleurMouvement(
                    listeMouvements=mouvement.listeMouvementsSuivants,
                    niveau=niveau + 1,
                    niveauMax=niveauMax
                ).valeurPiece * multiplicateur_de_niveau[niveau + 1]
            else:
                pointsSuivants = 0

            calculPointsMouvement = pointsNiveauActuel + pointsSuivants

            if calculPointsMouvement >= maxPoints:
                meilleurMouvementTrouve = mouvement
                maxPoints = calculPointsMouvement

        return meilleurMouvementTrouve

    def trierMouvements(self, liste):

        if liste == []:
            return []

        pivot = liste[0]
        liste1 = []
        liste2 = []

        for x in liste[1:]:

            if x.valeurPiece > pivot.valeurPiece:
                liste1.append(x)
            else:
                liste2.append(x)

        return self.trierMouvements(liste1) + [pivot] + self.trierMouvements(liste2)


class Mouvement:
    """
    une liste de mouvements est composee de :
        - un index de piece a deplacer
        - une valeur de déplacement
        - le numero de tour dans lequel le deplacement pourrait être réalise
        - le nombre de pieces adverses pouvant manger la piece actuelle
        - les mouvements suivant si il y en a
    """

    def __init__(self, indexDepart, indexArrivee, valeurPiece, numeroDuTour):
        self.indexDepart = indexDepart
        self.indexArrivee = indexArrivee
        self.valeurPiece = valeurPiece
        self.numeroDuTour = numeroDuTour
        self.listeMouvementsSuivants = None

    def set_listeMouvementsSuivants(self, liste):
        self.listeMouvementsSuivants = liste

    def get_valeurPiece(self):
        return self.valeurPiece
