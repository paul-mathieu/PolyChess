"""
#ia
"""

class IA:
    
    def __init__(self, echiquier, couleur):
        
        self.echiquier = echiquier
        
        self.couleur = couleur
        self.couleurOpposee = 'noir' if couleur == 'blanc' else 'blanc'
        
        
        self.valeurPieces = {
                ('Pion', self.couleur) : -10,
                ('Tour', self.couleur) : -50,
                ('Cavalier', self.couleur) : -30,
                ('Fou', self.couleur) : -30,
                ('Dame', self.couleur) : -90,
                ('Roi', self.couleur) : -900,
                ('Pion', self.couleurOpposee) : 10,
                ('Tour', self.couleurOpposee) : 50,
                ('Cavalier', self.couleurOpposee) : 30,
                ('Fou', self.couleurOpposee) : 30,
                ('Dame', self.couleurOpposee) : 90,
                ('Roi', self.couleurOpposee) : 900
                }

    
    def nMeilleursMouvementsParPoints(self, n = 5, echiquier = None, 
                                      profondeur = 3, niveauActuel = 0):
        
        """
        Cette fonction permet d'optenir un arbre par recursivite.
        
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
        
        #si le niveau actuel est le maximum souhaité (ici 5), on ne va pas plus profondement
        if not niveauActuel > 3:

            listeMouvements = self.listeTousMeilleursMouvements(echiquier, niveauActuel)
            
            #on garde les meilleures valeurs
            listeMouvements = listeMouvements[0:n]                



            #~~~~ pour tous les n meilleurs mouvements ~~~~~~~~~~~~~~~~~~~~~~~~
            
            #~~ (ajout pour chaque mouvements des n meilleurs                ~~
            #~~ mouvements suivants)                                         ~~   
                
                
            for mouvement in listeMouvements:
                
                # le nouvel echiquier contient la piece deplacee
                echiquierTemp = echiquier
                
                # le nouvel echiquier contient le meilleur 
                # déplacement de l'adversaire
                meilleurCoupAdversaire = self.listeTousMeilleursMouvements(echiquier, 
                                                                           niveauActuel, 
                                                                           self.couleurOpposee)
                meilleurCoupAdversaire = meilleurCoupAdversaire[0]
                echiquierTemp.deplacerPieceEnIndex(meilleurCoupAdversaire.indexDepart, 
                                                   meilleurCoupAdversaire.indexArrivee)
                
                echiquierTemp.deplacerPieceEnIndex(mouvement.indexDepart, 
                                                   mouvement.indexArrivee)
                
                
                listeMouvementsSuivants = self.nMeilleursMouvementsPoints(n, 
                                                                          echiquierTemp, 
                                                                          niveauActuel)
            
                mouvement.ajouterListeMouvementsSuivants(listeMouvementsSuivants)
#                    print("_|_|_|_|_|_")
#                    print(index)
#                    print(echiquier.positions[0:3])
#                    print(echiquier.get_piece(index).nom)
#                    print(echiquier.positions[index].couleur)
#                                            
            
            return listeMouvements
    
    
    
    
    def listeTousMeilleursMouvements(self, echiquier, niveauProfondeur, couleur):
        
        """
        Cette fonction renvoie tous les déplacements possibles triés
        d'une couleur avec un obejet de la classe mouvement contenant :
            - l'index de la piece a deplacer
            - l'index d'arrivee de la piece a deplacer
            - les points affectes a la piece
            - le niveau de la profondeur du mouvement
        """
        
        
        listeMouvements = []
            
        #~~~~ pour tous les mouvements de toutes les pieces ~~~~~~~~~~~~~~~
        
        #~~ (calcul des points pour chaque piece)                        ~~   


        #pour toutes les pieces de la couleur pouvant être déplacées
#            print(echiquier.listePiecesPouvantEtreDeplacees(couleur))
        
        for index in echiquier.listePiecesPouvantEtreDeplacees(couleur):
            
            piece = echiquier.positions[index]
            
            listeCoupsPossibles = echiquier.listeCoupsPossibles(echiquier.indexToNomCase(index))
            
            
            #pour tous les déplacements de la piece
            for indexArrivee in listeCoupsPossibles:
                
                valeurPiece = self.valeurPieces[(piece.nom, piece.couleur)]
                
                #ajout d'un nouveau mouvement à la liste
                listeMouvements.append(Mouvement(index, indexArrivee, valeurPiece, niveauProfondeur))

        #~~~~ Optimisation ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
        #~~ (tri en gardant les n avec les plus de                           ~~ 
        #~~ points                                                           ~~
        
        
        #on trie les elements par points                
        listeMouvements = self.trierMouvements(listeMouvements)
        
        return listeMouvements
    
    
    
    
    
    def meilleurMouvement(self, liste = None):
        
        """
        Cette fonction retour le meilleur mouvement a realiser d'apres
        le nombre de points qu'il rapporte
        """
        
        #à l'initialisation
        if liste == None:
            liste = self.nMeilleursMouvementsPoints()
        
        maxPoints = 0
        
        for mouvement in liste:
            
            #si le meilleur chemin est sup à la valeur max
            if mouvement.valeurPiece + mouvement.listeMouvementsSuivants.meilleurMouvement() >= maxPoints:
                
                pass
                
        
    
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


    def ajouterListeMouvementsSuivants(self, liste):
        self.listeMouvementsSuivants = liste
        
    def get_valeurPiece(self):
        return self.valeurPiece
        
            
            










