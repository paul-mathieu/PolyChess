
from functools import reduce


class Piece:

    pieceVide = '  ' 
    
    nomPiece = (pieceVide,'Roi','Dame','Tour','Cavalier','Fou','Pion')
    
    valeurPiece = (0, 0, 9, 5, 3, 3, 1)
    
    tblDebordement = [-1]*10*2 + reduce(lambda ele1, ele2 : ele1 + ele2, [[-1] + [valeur for valeur in range(0 + ligne, 8 + ligne)] + [-1] for ligne in range(0,57, 8)]) + [-1]*10*2 

#    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
#     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
#     -1,  0,  1,  2,  3,  4,  5,  6,  7, -1,
#     -1,  8,  9, 10, 11, 12, 13, 14, 15, -1,
#     -1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
#     -1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
#     -1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
#     -1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
#     -1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
#     -1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
#     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
#     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

# => on utilise la valeur comme index de l'échiquier

    tblPlacement = [21 + ligne + colonne for colonne in range(0,71,10) for ligne in range(8)]

#    [21, 22, 23, 24, 25, 26, 27, 28, 
#     31, 32, 33, 34, 35, 36, 37, 38, 
#     41, 42, 43, 44, 45, 46, 47, 48, 
#     51, 52, 53, 54, 55, 56, 57, 58, 
#     61, 62, 63, 64, 65, 66, 67, 68, 
#     71, 72, 73, 74, 75, 76, 77, 78, 
#     81, 82, 83, 84, 85, 86, 87, 88, 
#     91, 92, 93, 94, 95, 96, 97, 98]

# => on utilise la valeur comme position de tblDebordement


    def __init__(self, nom = pieceVide, couleur = ''):
        
        self.nom = nom
        self.couleur = couleur        
        self.valeur = self.valeurPiece[self.nomPiece.index(nom)]
        
        self.setNomPiece()




    
    def setNomPiece(self):
        
        """
        
        Cette fonction utilise les attributs de la couleur du nom de la piece
        
        Elle créé un nouvel attribut pour l'affichage tel que :
            - i[col]     pour un Pion
            - T[col]     pour une Tour
            - C[col]     pour un cavalier
            - F[col]     pour un fou
            - +[col]     pour un roi
            - -[col]     pour une reine
            
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


    def listeCoupsPossiblesPion(self, position, echiquier):
        #position va de 0 à 63
        
        
        listePossibilites = []
        
        
        if self.couleur == 'blanc':
            

            #deplacement de 2
            if 48 <= position <= 55:
                positionE = self.tblDebordement[self.tblPlacement[position] - 20]
                listePossibilites.append(positionE)
            
            #manger haut droite
            positionE = self.tblDebordement[self.tblPlacement[position] - 9]
            if not positionE == -1:
                if echiquier.positions[positionE].couleur == 'noir':
                    listePossibilites.append(positionE)
            
            #manger haut gauche
            positionE = self.tblDebordement[self.tblPlacement[position] - 11]
            if not positionE == -1:
                if echiquier.positions[positionE].couleur == 'noir':
                    listePossibilites.append(positionE)
                
            positionE = self.tblDebordement[self.tblPlacement[position] - 10]
            if not positionE == -1:
                listePossibilites.append(positionE)
                        


        else:
            
            
            #deplacement de 2
            if 8 <= position <= 15:
                positionE = self.tblDebordement[self.tblPlacement[position] + 20]
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
                
            positionE = self.tblDebordement[self.tblPlacement[position] + 10]
            if not positionE == -1:
                listePossibilites.append(positionE)
        
        return listePossibilites
        

        
    def listeCoupsPossiblesTour(self, position, echiquier):
        deplacements = (-10, 10, -1, 1)
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
    
        
    def listeCoupsPossiblesFou(self, position, echiquier):
        deplacements = (-11, -9, 11, 9)
        
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



       
    def listeCoupsPossiblesCavalier(self, position, echiquier):
        deplacements = (-12, -21, -19, -8, 12, 21, 19, 8)
        
        listePossibilites = []
        
        for deplacement in deplacements:
            
            positionE = self.tblDebordement[self.tblPlacement[position] + deplacement]
            
            if not positionE == -1:
                if not echiquier.positions[positionE].couleur == self.couleur:
                    
                    listePossibilites.append(positionE)
        
        return listePossibilites
        
        
    
    def listeCoupsPossiblesRoi(self, position, echiquier):
        return []
        
        
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
    
    
        
        
