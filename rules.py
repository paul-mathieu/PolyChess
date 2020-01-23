from functools import reduce


class Piece:

    pieceVide = '  ' 
    
    nomPiece = (pieceVide, 'Roi', 'Dame', 'Tour', 'Cavalier', 'Fou', 'Pion')
    
    valeurPiece = (0, 0, 9, 5, 3, 3, 1)
    
    tblDebordement = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                      -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                      -1,  0,  1,  2,  3,  4,  5,  6,  7, -1,
                      -1,  8,  9, 10, 11, 12, 13, 14, 15, -1,
                      -1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
                      -1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
                      -1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
                      -1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
                      -1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
                      -1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
                      -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                      -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    
    
    #1  On donne un nom a chaque position de l'echiquier (de 0 a 63)
    
    
#    [-1]*10*2 + reduce(lambda ele1, ele2 : ele1 + ele2, [[-1] + [valeur for valeur in range(0 + ligne, 8 + ligne)] + [-1] for ligne in range(0,57, 8)]) + [-1]*10*2 



# => on utilise la valeur comme index de l'échiquier

    tblPlacement = [21, 22, 23, 24, 25, 26, 27, 28, 
                    31, 32, 33, 34, 35, 36, 37, 38, 
                    41, 42, 43, 44, 45, 46, 47, 48, 
                    51, 52, 53, 54, 55, 56, 57, 58, 
                    61, 62, 63, 64, 65, 66, 67, 68, 
                    71, 72, 73, 74, 75, 76, 77, 78, 
                    81, 82, 83, 84, 85, 86, 87, 88, 
                    91, 92, 93, 94, 95, 96, 97, 98]
    
    #[21 + ligne + colonne for colonne in range(0, 71, 10) for ligne in range(8)]
    #Pour les noirs:
    #Pour avancer tout droit en avant on ajoute 10 par case (-10 en arriere)
    #Pour aller en diagonale a droite on ajoute 11 (-11 en arriere)
    #Pour aller en diagonale a gauche on ajoute 9 (-9 en arriere)
    
    #L'inverse pour les blancs.
    
    




# => on utilise la valeur comme position de tblDebordement


    def __init__(self, nom = pieceVide, couleur = '', pieceABouge = False):
        
        self.nom = nom
        self.couleur = couleur
        self.couleurOpposee = 'noir' if self.couleur == 'blanc' else 'blanc'
        self.valeur = self.valeurPiece[self.nomPiece.index(nom)]
        
        self.setNomPiece()
        
        self.pieceABouge = pieceABouge
        
     
       #2   Constructeur de l'objet. Il correspond a une piece qui n'a pas encore de nom.
       #    On appelera la fonction ci-dessous pour lui en atribuer un.



    
    def setNomPiece(self):
        
        """
        
        Cette fonction utilise les attributs de la couleur du nom de la piece
        
        Elle créé un nouvel attribut pour l'affichage tel que :
            - i[col]     pour un Pion
            - T[col]     pour une Tour
            - C[col]     pour un Cavalier
            - F[col]     pour un Fou
            - R[col]     pour un Roi
            - D[col]     pour une Dame
            
        Chaque valeur est suivie de sa couleur
        
        """

        
        if self.nom == self.pieceVide:
            self.nomAffichage = self.pieceVide
        
        elif self.nom == 'Pion':
            self.nomAffichage = 'i' + self.couleur[0].lower()
            
        else:
            self.nomAffichage = self.nom[0].upper() + self.couleur[0].lower()
        

        
#==============================================================================
# Coups possibles
#==============================================================================





                       #===========================
                                  # Pion
                       #===========================

    def listeCoupsPossiblesPion(self, position, echiquier):
        #position va de 0 à 63
        
        
        listePossibilites = []
        
        
        if self.couleur == 'blanc':
                        
            #deplacement de 2 si il se trouve sur la ligne 1 --> -10 par case d'où -20 ici.
            #On utilise les deux listes definies au debut.
            
            if 48 <= position <= 55:
                positionE = self.tblDebordement[self.tblPlacement[position] - 20]
#                print(positionE)
                if echiquier.positions[positionE].nom == echiquier.positions[positionE].pieceVide:
#                    print('---')
                    listePossibilites.append(positionE)
            
            #manger haut droite. 
            positionE = self.tblDebordement[self.tblPlacement[position] - 9]
            #Dans toutes les methodes, on va s'assurer que le deplacement ne va pas faire sortir la piece de l'echiquier
            if not positionE == -1:   
                if echiquier.positions[positionE].couleur == 'noir':
                    listePossibilites.append(positionE)
            
            #manger haut gauche
            positionE = self.tblDebordement[self.tblPlacement[position] - 11]
            if not positionE == -1:
                if echiquier.positions[positionE].couleur == 'noir':
                    listePossibilites.append(positionE)
                
            positionE = self.tblDebordement[self.tblPlacement[position] - 10]
            if not positionE == -1 and echiquier.positions[positionE].nom == echiquier.positions[positionE].pieceVide:
                listePossibilites.append(positionE)
                        


        else:
            
            
            #deplacement de 2 si il se trouve sur la ligne 6
            if 8 <= position <= 15:
                positionE = self.tblDebordement[self.tblPlacement[position] + 20]
                if echiquier.positions[positionE].nom == echiquier.positions[positionE].pieceVide:
                    listePossibilites.append(positionE)
            
            #manger bas gauche
            positionE = self.tblDebordement[self.tblPlacement[position] + 9]
            if not positionE == -1:
                if echiquier.positions[positionE].couleur == 'blanc':
                    listePossibilites.append(positionE)
            
            #manger bas droite
            positionE = self.tblDebordement[self.tblPlacement[position] + 11]
            if not positionE == -1:
                if echiquier.positions[positionE].couleur == 'blanc':
                    listePossibilites.append(positionE)
            #deplacement classique du pion    
            positionE = self.tblDebordement[self.tblPlacement[position] + 10]
            if not positionE == -1 and echiquier.positions[positionE].nom == echiquier.positions[positionE].pieceVide:
                listePossibilites.append(positionE)
        
        return listePossibilites
    
    
    
                       #===========================
                                  # Tour
                       #===========================
        

        
    def listeCoupsPossiblesTour(self, position, echiquier):
        deplacements = (-10, 10, -1, 1) #Deplacements horizontaux et verticaux dans les deux directions.
        couleurCaseOpposee = 'noir' if self.couleur == 'blanc' else 'blanc'

        
        listePossibilites = []
        for deplacement in deplacements:
            
            multiplicateur = 1
            positionE = self.tblDebordement[self.tblPlacement[position] + deplacement]
            #Ici on utilise une boucle car la tour peut se deplacer d'autant de case qu'elle veut tant qu'elle n'arrive pas sur 
            #une piece ou le bord de l'échiquier. Si c'est une piece adverse elle prend sa place, si c'est une pièce alliee 
            #elle s'arrête devant.
            while not positionE == -1:
                
                if echiquier.positions[positionE].couleur == self.couleur:
                    break
            
                if echiquier.positions[positionE].couleur == couleurCaseOpposee:
                    
                    listePossibilites.append(positionE)
                    
                    break

                elif echiquier.positions[positionE].nom == self.pieceVide:
                    
                    listePossibilites.append(positionE)

                
                multiplicateur += 1
                positionE = self.tblDebordement[self.tblPlacement[position] + deplacement * multiplicateur]

        
        return listePossibilites  







                       #===========================
                                  # Fou
                       #===========================       
    
        
    def listeCoupsPossiblesFou(self, position, echiquier):
        deplacements = (-11, -9, 11, 9) #deplacements dans les deux diagonales, vers l'avant et vers l'arriere.
        
        couleurCaseOpposee = 'noir' if self.couleur == 'blanc' else 'blanc'
        listePossibilites = []
        
        for deplacement in deplacements:
            
            multiplicateur = 1
            positionE = self.tblDebordement[self.tblPlacement[position] + deplacement]
            
            while not positionE == -1:
                
                if echiquier.positions[positionE].couleur == self.couleur:
                    break

                if echiquier.positions[positionE].couleur == couleurCaseOpposee:
                    
                    listePossibilites.append(positionE)
                    
                    break

                elif echiquier.positions[positionE].nom == self.pieceVide:
                    
                    listePossibilites.append(positionE)

                
                multiplicateur += 1
                positionE = self.tblDebordement[self.tblPlacement[position] + deplacement * multiplicateur]

        
        return listePossibilites
    
    
    
    
    
                       #===========================
                                # Cavalier
                       #===========================



       
    def listeCoupsPossiblesCavalier(self, position, echiquier):
        deplacements = (-12, -21, -19, -8, 12, 21, 19, 8)  #Les differents types de "L".
        
        listePossibilites = []
        
        for deplacement in deplacements:
            
            positionE = self.tblDebordement[self.tblPlacement[position] + deplacement]
            
            if not positionE == -1:
                if not echiquier.positions[positionE].couleur == self.couleur:
                    
                    listePossibilites.append(positionE)
        
        return listePossibilites
    
    
    
    
    
                       #===========================
                                  # Roi
                       #===========================
        
        
    def listeCoupsPossiblesRoi(self, position, echiquier):
        deplacements = (-11, -10, -9, -1, 1, 9, 10, 11)   #deplacements dans toutes les directions
        
        listePossibilites = []

        for deplacement in deplacements:
            
            positionE = self.tblDebordement[self.tblPlacement[position] + deplacement]
            
            if not positionE == -1:
                if not echiquier.positions[positionE].couleur == self.couleur:
                    
                    listePossibilites.append(positionE)
        
        if self.couleur == 'blanc' and position == 60 and echiquier.petitRoqueBlancPossible():
            listePossibilites.append(62)
            
        if self.couleur == 'blanc' and position == 60 and echiquier.grandRoqueBlancPossible():
            listePossibilites.append(58)
        
        if self.couleur == 'noir' and position == 4 and echiquier.petitRoqueNoirPossible():
            listePossibilites.append(6)
            
        if self.couleur == 'noir' and position == 4 and echiquier.grandRoqueNoirPossible():
            listePossibilites.append(2)    
            
        return listePossibilites
    
    
    
    
                       #===========================
                                  # Dame
                       #===========================

        
        #La dame est la combinaison d'un fou et d'une tour.
    def listeCoupsPossiblesDame(self, position, echiquier):
        return self.listeCoupsPossiblesFou(position, echiquier) + self.listeCoupsPossiblesTour(position, echiquier)
        
        
        
        
#==============================================================================
# Fonction annexes
#==============================================================================
            
            
    def isEmpty(self):
        
        """Returns TRUE or FALSE if this piece object is defined, 
        As any square on board can have a piece on it, or not,
        we can set a null piece on a square."""
        
        return self.nom == self.pieceVide
