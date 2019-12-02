

class MeilleurMouvement:
    
    def __init__(self, echiquier, couleur):
        
        self.echiquier = echiquier
        
        self.couleur = couleur
        self.couleurOpposee = 'noir' if couleur == 'blanc' else 'noir'
        
        
        self.valeurPions = {
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
    
    
    def mouvementsInterressantsCeTour(self):
        
        liste = 
        return self.echiquier.
    
    def mouvement(self, indexDeplacement, valerDeplacement):
        
        pass















