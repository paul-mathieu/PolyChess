"""
#ia
"""

class MeilleurMouvement:
    
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

    
    def nMeilleursMouvementsPoints(self, n = 5, echiquier = None, niveauActuel = 0):
        
        if echiquier == None:
            echiquier = self.echiquier
        
        listeMouvements = []
        niveauActuel += 1
        
        #si le niveau actuel est le maximum souhaité (ici 5), on ne va pas plus profondement
        if not niveauActuel > 3:


            #~~ pour tous les mouvements de toutes les pieces ~~

            #pour toutes les pieces de la couleur pouvant être déplacées
#            print(echiquier.listePiecesPouvantEtreDeplacees(self.couleur))
            for index in echiquier.listePiecesPouvantEtreDeplacees(self.couleur):
                
                #pour tous les déplacements de la piece
                for indexArr in self.echiquier.listeCoupsPossibles(echiquier.indexToNomCase(index)):
                    
                    valeurPiece = self.valeurPieces[(echiquier.positions[index].nom, echiquier.positions[index].couleur)]
                    
                    #ajout d'un nouveau mouvement à la liste
                    listeMouvements.append(Mouvement(index, indexArr, valeurPiece, niveauActuel))
                
                
            #pour optimiser, tri en gardant les n premiers   
                
            #on trie les elements par points                
            listeMouvements = self.trierMouvements(listeMouvements)
            
            #on garde les meilleures valeurs
            listeMouvements = listeMouvements[0:n]                
                
                
            for mouvement in listeMouvements:
                
                # le nouvel echiquier contient la piece deplacee
                echiquierTemp = echiquier
                echiquierTemp.deplacerPieceEnIndex(mouvement.indexDepart, mouvement.indexArrivee)
                
                
                listeMouvementsSuivants = self.nMeilleursMouvementsPoints(n, echiquierTemp, niveauActuel)
            
                mouvement.ajouterListeMouvementsSuivants(listeMouvementsSuivants)
#                    print("_|_|_|_|_|_")
#                    print(index)
#                    print(echiquier.positions[0:3])
#                    print(echiquier.get_piece(index).nom)
#                    print(echiquier.positions[index].couleur)
#                                            
            
            return listeMouvements
    
    
    def meilleurMouvement(self, liste = None):
        
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
        
            
            










