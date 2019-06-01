""" classe : Hypothese
    Attributs :
        - signature : un dictionnaire caractèristique de l'hypothèse permettant de la tester et de l'identifier
        - credibilite : credibilite de l'hypothese, represente si l'hypothese est plutot vraie ou plutot fausse
        - seuilFaux : seuil au dela duquel l'hypothèse est considérée comme fausse
        - seuilLois : seuil au dela duquel l'hypothèse est considérée comme juste
"""
class Hypothese:
    def __init__(self):
        self.signature = {}
        self.seuilFaux = 2
        self.seuilLois = 8
        self.credibilite = 5

    """ Méthode : ChangerCredibilite
        Paramètres:
            res : un booleen representant si l'hypothèse à été confirmée ou infirmée
        Objectifs:
            Mettre à jour la crédibilité d'une hypothèse
    """
    def ChangerCredibilite(self,res):
        if res == 1:
            self.credibilite += 1
        else :
            self.credibilite -= 1
