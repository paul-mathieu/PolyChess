# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 08:28:34 2020

@author: gourets
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 13:41:49 2020

@author: ragueney
"""

"""


"""



from functools import reduce
from rules import Piece
import copy 



class Echiquier:
        
    
    def __init__(self):
        
        self.estEchec = {"blanc" : False, "noir" : False}
         
        self.positions = \
            [Piece('Tour', 'noir'), 
             Piece('Cavalier', 'noir'), 
             Piece('Fou','noir'),
             Piece('Dame', 'noir'), 
             Piece('Roi','noir'),
             Piece('Fou', 'noir'), 
             Piece('Cavalier', 'noir'), 
             Piece('Tour', 'noir')] + \
                \
            [Piece('Pion', 'noir')] * 8 + \
                \
            [Piece()] * 8 * 4 + \
                \
            [Piece('Pion', 'blanc')] * 8 + \
                \
            [Piece('Tour', 'blanc'), 
             Piece('Cavalier', 'blanc'), 
             Piece('Fou','blanc'),
             Piece('Dame', 'blanc'), 
             Piece('Roi', 'blanc'),
             Piece('Fou', 'blanc'),
             Piece('Cavalier', 'blanc'), 
             Piece('Tour', 'blanc')]
            
#        self.positions = \
#            [Piece()] * 8 +  \
#                \
#            [Piece('Tour', 'noir'), Piece('Cavalier', 'noir'), 
#             Piece('Fou','noir'),
#             Piece('Dame', 'noir'), Piece('Roi','noir'),
#             Piece('Fou', 'noir'), 
#             Piece('Cavalier', 'noir'), Piece('Tour', 'noir')] + \
#                \
#            [Piece()] * 8 * 4 + \
#                \
#            [Piece('Tour', 'blanc'), Piece('Cavalier', 'blanc'), 
#             Piece('Fou','blanc'),
#             Piece('Dame', 'blanc'), Piece('Roi', 'blanc'),
#             Piece('Fou', 'blanc'),
#             Piece('Cavalier', 'blanc'), Piece('Tour', 'blanc')] + \
#                \
#            [Piece()] * 8
#            
    def get_piece(self, index):
        return self.positions[index]
                 
  #  def testCouleur(self, index):
 #       index = self.nomCaseToIndex(position)
   #     piece = self.get_piece(index)
    
    #    return  piece.couleur  
#==============================================================================
# Construction de l'échiquier
#==============================================================================
    
    def coordonnees():
        return [lettre + str(chiffre) for chiffre in range(1,9) for lettre in ['A','B','C','D','E','F','G','H']]
    
    
#==============================================================================
# Affichage
#==============================================================================
 #Methode qui affiche une representation schematique d'un echiquier dans la console.   
    
    def afficher(self):
    
        lettres = reduce(lambda ele1, ele2 : ele1 + ele2, ["  " + element + "  " for element in ['A','B','C','D','E','F','G','H']])
        interlignes = "    " + reduce(lambda ele1, ele2 : ele1 + ele2, ["-" * 4 + " "] * 8)
        
        print(" " * 60 + "/")
        print(" ".join(["—","-"] * 15))        
        print(" " * 60 + "\\")
        
        print("   " + lettres)
        print(interlignes)
        
        numLigne = 8
        indexPosition = 0
        
        for piece in self.positions:
            
#            print(ligne)
            
            if indexPosition % 8 == 0:
                print(str(numLigne), end = "  |")
            
            if piece.nom != piece.pieceVide:
                
                print(" " + piece.nomAffichage + " ", end = "|")
        
            else:
                
                print("    ", end = "|")
            
            
            if (indexPosition + 1) % 8 == 0:
                
                print("  " + str(numLigne))
            
                print(interlignes)
            
                numLigne -= 1
                
            indexPosition += 1
            
        print("   " + lettres)
    
        
    
#         A    B    C    D    E    F    G    H  
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    8  | Tn | Cn | Fn | Dn | Rn | Fn | Cn | Tn |  8
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    7  | in | in | in | in | in | in | in | in |  7
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    6  |    |    |    |    |    |    |    |    |  6
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    5  |    |    |    |    |    |    |    |    |  5
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    4  |    |    |    |    |    |    |    |    |  4
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    3  |    |    |    |    |    |    |    |    |  3
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    2  | ib | ib | ib | ib | ib | ib | ib | ib |  2
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    1  | Tb | Cb | Fb | Db | Rb | Fb | Cb | Tb |  1
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#         A    B    C    D    E    F    G    H  
    


#Permet de montrer les coups possibles au joueur.

    def afficherCoupsPossibles(self, nomCase):
    
        lettres = reduce(lambda ele1, ele2 : ele1 + ele2, ["  " + element + "  " for element in ['A','B','C','D','E','F','G','H']])
        interlignes = "    " + reduce(lambda ele1, ele2 : ele1 + ele2, ["-" * 4 + " "] * 8)
        
        coupsPossibles = self.listeCoupsPossibles(nomCase)
        
        couleur = self.positions[self.nomCaseToIndex(nomCase)].couleur
        couleurOpposee = 'noir' if couleur == 'blanc' else 'blanc'
        
        print(" " * 60 + "/")
        print(" ".join(["—","-"] * 15))        
        print(" " * 60 + "\\")

        print("   " + lettres)
        print(interlignes)
        
        numLigne = 8
        indexPosition = 0
        
        for piece in self.positions:
            
#            print(ligne)
            
            if indexPosition % 8 == 0:
                print(str(numLigne), end = "  |")
                
            
            if indexPosition == self.nomCaseToIndex(nomCase):
                
                print("#" + piece.nomAffichage + "#", end = "|")
                
            elif indexPosition in coupsPossibles:
                
                if  piece.couleur == couleurOpposee:
                    
                    print("<" + piece.nomAffichage + ">", end = "|")
                
                else:
                    
                    print(" <> ", end = "|")
            
            elif piece.nom != piece.pieceVide:
                
                print(" " + piece.nomAffichage + " ", end = "|")
        
            else:
                
                print("    ", end = "|")
                
            
            
            if (indexPosition + 1) % 8 == 0:
                
                print("  " + str(numLigne))
            
                print(interlignes)
            
                numLigne -= 1
                
            indexPosition += 1
            
        print("   " + lettres)
    

 
 
    
#==============================================================================
# Déplacement
#==============================================================================
    
    def deplacerPiece(self, nomCaseDepart, nomCaseArrivee):
        indexDep = self.nomCaseToIndex(nomCaseDepart)
        indexArr = self.nomCaseToIndex(nomCaseArrivee)
       
        # Petit roque noir
        if indexDep == 4 and indexArr == 6 and self.positions[4].nom == 'Roi' and indexArr in self.listeDesCoupsAvecEchecNoir(4) :
            self.positions[indexArr] = self.positions[indexDep]
            self.positions[indexDep] = Piece()
            self.positions[5] = self.positions[7]
            self.positions[7] = Piece()
        
        # Petit roque blanc
        if indexDep == 60 and indexArr == 62 and self.positions[60].nom == 'Roi' and indexArr in self.listeDesCoupsAvecEchecBlanc(60) :
            self.positions[indexArr] = self.positions[indexDep]
            self.positions[indexDep] = Piece()
            self.positions[61] = self.positions[63]
            self.positions[63] = Piece()
            
        # Grand roque noir
        if indexDep == 4 and indexArr == 2 and self.positions[4].nom == 'Roi' and indexArr in self.listeDesCoupsAvecEchecNoir(4) :
            self.positions[indexArr] = self.positions[indexDep]
            self.positions[indexDep] = Piece()
            self.positions[3] = self.positions[0]
            self.positions[0] = Piece()
            
        # Grand roque blanc
        if indexDep == 60 and indexArr == 58 and self.positions[60].nom == 'Roi' and indexArr in self.listeDesCoupsAvecEchecBlanc(60) :
            self.positions[indexArr] = self.positions[indexDep]
            self.positions[indexDep] = Piece()
            self.positions[59] = self.positions[56]
            self.positions[56] = Piece()
        
        if not self.positions[indexDep].pieceABouge:
            self.positions[indexDep].pieceABouge = True
        
            
        
        
        if indexArr in self.listeDesCoupsAvecEchecBlanc(indexDep) and self.get_piece(indexDep).couleur == 'blanc': 
            self.positions[indexArr] = self.positions[indexDep]
            self.positions[indexDep] = Piece()  
        
        
        if indexArr in self.listeDesCoupsAvecEchecNoir(indexDep) and self.get_piece(indexDep).couleur == 'noir':
            self.positions[indexArr] = self.positions[indexDep]
            self.positions[indexDep] = Piece()
            
        
        
    def deplacerPieceEnIndex(self, indexDepart, indexArrivee):
        if not self.positions[indexDepart].pieceABouge:
            self.positions[indexDepart].pieceABouge = True        
        if indexArrivee in self.listeCoupsPossibles(self.indexToNomCase(indexDepart)):
            
            if not self.positions[indexDepart]:
                self.positions[indexDepart] = True 
            
            self.positions[indexArrivee] = self.positions[indexDepart]
            self.positions[indexDepart] = Piece()  
        
    def deplacementForce(self, indexDepart, indexArrivee):
        if not self.positions[indexDepart].pieceABouge:
            self.positions[indexDepart].pieceABouge = True
        self.positions[indexArrivee] = self.positions[indexDepart]
        self.positions[indexDepart] = Piece()         
        
        
    def listeDesCoupsAvecEchecBlanc(self, index):
        
        listeDesCoupsPossibles = self.listeCoupsPossiblesEntreeIndex(index)
        listeDesCoupsAEnlever = []
        
        echiquierTemporaire = self
        
        positionsPrecedentes = copy.copy(self.positions)
        positionsPrecedentes_liste = list(map(lambda x : (x.nom, x.couleur, x.pieceABouge), positionsPrecedentes))
       
        
        
        for mouvement in listeDesCoupsPossibles:
            
            echiquierTemporaire.deplacementForce(index, mouvement)            
#            if not echiquierTemporaire.isEchecBlanc():
#                return listeDesCoupsPossibles
            
            if echiquierTemporaire.isEchecBlanc():
#                echiquierTemporaire.afficher()
                listeDesCoupsAEnlever.append(mouvement)
                print(listeDesCoupsAEnlever)
             
                
            self.positions = [Piece(element[0], element[1], element[2]) for element in positionsPrecedentes_liste]
       

        return [index for index in listeDesCoupsPossibles if not index in listeDesCoupsAEnlever]
    
    def listeDesCoupsAvecEchecNoir(self, index):
        
        listeDesCoupsPossibles = self.listeCoupsPossiblesEntreeIndex(index)
        listeDesCoupsAEnlever = [] 
        echiquierTemporaire = self
        positionsPrecedentes = copy.copy(self.positions)
        positionsPrecedentes_liste = list(map(lambda x : (x.nom, x.couleur, x.pieceABouge), positionsPrecedentes))
        
#        if not self.isEchecNoir():
#            return listeDesCoupsPossibles
        
        for mouvement in listeDesCoupsPossibles:
            
            echiquierTemporaire.deplacementForce(index, mouvement)
            if echiquierTemporaire.isEchecNoir():
                listeDesCoupsAEnlever.append(mouvement)
            
            self.positions = [Piece(element[0], element[1], element[2]) for element in positionsPrecedentes_liste]
        
        return [index for index in listeDesCoupsPossibles if not index in listeDesCoupsAEnlever]
    
    def listeDesCoupsAvecVerif(self, index, couleur):
        if couleur == 'noir' :
            L = []
            for k in self.listeDesCoupsAvecEchecNoir(index) :
                L.append(self.indexToNomCase(k))
            return L
        else:
            L=[]
            for k in self.listeDesCoupsAvecEchecBlanc(index):
                L.append(self.indexToNomCase(k))
            return L

        
    def listePiecesPouvantEtreDeplaceesFormatCaseAvecVerif(self, couleur):
        listCoupsPouvantEtreDeplacees=[]
        for element in self.listePiecesPouvantEtreDeplaceesFormatCase(couleur):
            if not self.listeDesCoupsAvecVerif(self.nomCaseToIndex(element),couleur) == []:
                listCoupsPouvantEtreDeplacees.append(element)
        return listCoupsPouvantEtreDeplacees
#==============================================================================
# Vérification déplacement dans la zone
#==============================================================================

    def listeCoupsPossibles(self, nomCase):
        
        indexCase = self.nomCaseToIndex(nomCase)
        
        return self.listeCoupsPossiblesEntreeIndex(indexCase)

    
    def listeCoupsPossiblesEntreeIndex(self, indexCase):
        
        if self.positions[indexCase].nom == self.positions[indexCase].pieceVide:
            return []
        
        if self.positions[indexCase].nom == 'Pion':
            return self.positions[indexCase].listeCoupsPossiblesPion(indexCase, self)
            
        if self.positions[indexCase].nom == 'Tour':
            return self.positions[indexCase].listeCoupsPossiblesTour(indexCase, self)
        
        if self.positions[indexCase].nom == 'Fou':
            return self.positions[indexCase].listeCoupsPossiblesFou(indexCase, self)
        
        if self.positions[indexCase].nom == 'Cavalier':
            return self.positions[indexCase].listeCoupsPossiblesCavalier(indexCase, self)
        
        if self.positions[indexCase].nom == 'Dame':
            return self.positions[indexCase].listeCoupsPossiblesDame(indexCase, self)
        
        if self.positions[indexCase].nom == 'Roi':
            return self.positions[indexCase].listeCoupsPossiblesRoi(indexCase, self)  
        

    def listeCoupsPossiblesFormatCase(self, nomCase):
        
        return [self.indexToNomCase(index) for index in self.listeCoupsPossibles(nomCase)]


    def listePiecesPouvantEtreDeplacees(self, couleur):
        
        liste = []
        
        for index in range(64):
            
            if self.positions[index].couleur == couleur:
                
                if len(self.listeCoupsPossibles(self.indexToNomCase(index))) > 0:
                    
                    liste.append(index)
        
        return liste
        
    def listePiecesPouvantEtreDeplaceesFormatCase(self, nomCase):
        
        return [self.indexToNomCase(index) for index in self.listePiecesPouvantEtreDeplacees(nomCase)]



#==============================================================================
# Fin du jeu
#==============================================================================

    def isEchecBlanc(self):
        
        #on recupere la podsiton du roi blanc
        
        listePositionsRoi1 = []
        index = 0
        for piece in self.positions:
            if piece.nom == 'Roi' and piece.couleur=='blanc':
                listePositionsRoi1.append(index)    
            index += 1
          #si la liste des pieces menancant le roi n'est pas vide, alors il y a echec.   
        if self.nombreDePiecesAdversesPouvantMangerLaPiece(listePositionsRoi1[0])!=0:
            return True
        else :
            return False
        
        
    def isEchecNoir(self):
        
        
        listePositionsRoi2 = []
        index = 0
        for piece in self.positions:
            if piece.nom == 'Roi' and piece.couleur=='noir':
                listePositionsRoi2.append(index)    
            index += 1
            
        if self.nombreDePiecesAdversesPouvantMangerLaPiece(listePositionsRoi2[0])!=0:
            return True  
        else :
            return False
            
            
     
        

# Si la piece est le roi blanc, qu'il est en echec et qu'il n'a plus de coup disponible, alors il y a echec et mat.
    def isEchecEtMatBlanc(self):
        for i in range(0,63):
            if self.get_piece(i).couleur == 'blanc' and self.listeDesCoupsAvecEchecBlanc(i) != []:
                return False
        return True
                
    def isEchecEtMatNoir(self):
        for i in range(0,63):
            if self.get_piece(i).couleur == 'noir' and self.listeDesCoupsAvecEchecNoir(i) != []:
                return False
        return True
                
                
        
    
    
    def couleurEchecEtMat(self):
        
        if not self.isEchecEtMat():
            return None
        
        return 'blanc' if list(filter(lambda piece : piece.nom == 'Roi', self.positions))[0].couleur == 'noir' else 'noir'


#==============================================================================
# Autres fonctions
#==============================================================================
    
    def nomCaseToIndex(self, nomCase):
        
        if not type(nomCase) is str:
            return 'erreur saisie'
        
        lettres = ['A','B','C','D','E','F','G','H']
        lig, col = 8 - int(nomCase[1]), lettres.index(nomCase[0]) + 1
        
        return lig * 8 + col - 1
    
    def indexToNomCase(self, indexCase):
        
        return ['A','B','C','D','E','F','G','H'][indexCase % 8] + str(8 - indexCase // 8)
    
    #print("‎• or <>")
    
    def listeIndexMangeantLaPiece(self, indexPiece):
        listeIndex = []
        
        for indexDepart in self.listePiecesPouvantEtreDeplacees(self.positions[indexPiece].couleurOpposee):
            
            for indexArrivee in self.listeCoupsPossiblesEntreeIndex(indexDepart):
                
                if indexArrivee == indexPiece:
                    
                    listeIndex.append(indexDepart)
                    break
                
        
        return listeIndex

    
    def leDeplacementMangeUnePiece(self, indexArrivee):
        return self.positions[indexArrivee].couleur != self.positions[0].pieceVide
    


    def nombreDePiecesAdversesPouvantMangerLaPiece(self, index):
        return len(self.listeIndexMangeantLaPiece(index))
    
    def petitRoqueNoirPossible(self):
        return self.positions[7].pieceABouge == False and self.positions[4].pieceABouge == False and self.positions[6].nom == self.positions[6].pieceVide and self.positions[5].nom == self.positions[5].pieceVide 
       
    def grandRoqueNoirPossible(self):
        return self.positions[0].pieceABouge == False and self.positions[4].pieceABouge == False and self.positions[1].nom == self.positions[1].pieceVide and self.positions[2].nom == self.positions[2].pieceVide and self.positions[3].nom == self.positions[3].pieceVide
       
    def petitRoqueBlancPossible(self):
        return self.positions[60].pieceABouge == False and self.positions[63].pieceABouge == False and self.positions[61].nom == self.positions[61].pieceVide and self.positions[62].nom == self.positions[62].pieceVide 
      
        
    def grandRoqueBlancPossible(self):
        return self.positions[60].pieceABouge == False and self.positions[56].pieceABouge == False and self.positions[59].nom == self.positions[59].pieceVide and self.positions[58].nom == self.positions[58].pieceVide and self.positions[57].nom == self.positions[57].pieceVide  
        
        
        
   # def roiOuTourNoireABouge(self, indexCase):
    #    if (self.positions[60].nom == 'Roi' and self.aBouge(60) == 0) or ((indexCase == 56 or indexCase== 63) and self.positions[indexCase].nom == 'Tour' and self.aBouge(56) == 0 and self.aBouge(63) == 0):
     #       return 0
      #  else: 
       #     return 1
        
  #  def petitRoqueBlanc(self, indexPiece):
     #   if self.positions[1].nom == self.positions[1].pieceVide and 
        
        
# =============================================================================
# fonction pour les calculs de points de l'IA
# =============================================================================
    
     #moins de points si la piece peut se faire manger
    def coefficientPointsSiPeutEtreMangee(self, indexArrivee):
        
        nbPiecePouvantManger = self.nombreDePiecesAdversesPouvantMangerLaPiece(indexArrivee)
        
        #si len = 0
        if nbPiecePouvantManger == 0:
            return 1
        
        #si len = 1
        if nbPiecePouvantManger == 1:
            return 1.5
        
        #si len > 1
        if nbPiecePouvantManger > 1 :
            return 1.5 + .2 * (nbPiecePouvantManger - 1)
            
        
        
        
        
    
    #moins de points si elle n'a aucune piece de la meme couleur autour
    def coefficientPointsSiPieceMemeCouleurProche(self, indexArrivee, couleur):
            
        pass
    
