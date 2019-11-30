
from functools import reduce


class Piece:

    pieceVide=' ' 
    
    nomPiece = (pieceVide,'ROI','DAME','TOUR','CAVALIER','FOU','PION')
    
    valeurPiece=(0,0,9,5,3,3,1)
    
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

    

    tblPlacement = [21 + ligne + colonne for colonne in range(0,71,10) for ligne in range(8)]

#    [21, 22, 23, 24, 25, 26, 27, 28, 
#     31, 32, 33, 34, 35, 36, 37, 38, 
#     41, 42, 43, 44, 45, 46, 47, 48, 
#     51, 52, 53, 54, 55, 56, 57, 58, 
#     61, 62, 63, 64, 65, 66, 67, 68, 
#     71, 72, 73, 74, 75, 76, 77, 78, 
#     81, 82, 83, 84, 85, 86, 87, 88, 
#     91, 92, 93, 94, 95, 96, 97, 98]




    def __init__(self, nom = pieceVide, couleur = ''):
        
        self.nom=nom
        self.couleur=couleur        
        self.valeur=self.valeurPiece[self.nomPiece.index(nom)]
        



    def deplacementsTour():
        return -10, 10, -1, 1
    
    def deplacementsFou(): 
        return -11, -9, 11, 9
    
    def deplacementsCavalier():
        return -12, -21, -19, -8, 12, 21, 19, 8

        
        

    def listeDesPieces(couleur):
        
        """
        
        Cette fonction prend en paramètre "B" pour les pions blancs 
        et "N" pour les pions noirs
        
        Elle génere la liste des pieces d'une couleur tel que :
            - i     pour un Pion
            - T     pour une Tour
            - C     pour un cavalier
            - F     pour un fou
            - +     pour un roi
            - -     pour une reine
            
        Chaque valeur est suivie de sa couleur
        
        La fonction renvoie deux listes :
            - la liste des pions
            - la liste des autres pieces
    
        """
        
        lignePions = ['i' + couleur] * 8
        ligneAutresPieces = [element + couleur for element in ['T', 'C', 'F', '+', '-', 'F', 'C', 'T']]
        
        return [lignePions, ligneAutresPieces]
    
    
    #fonction qui vérifie si la case est valide
