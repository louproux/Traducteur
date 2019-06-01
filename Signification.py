""" classe : Signification
    
    Objectifs: 
        Type d'hypothese de la forme motA = motB
"""

import Hypothese as h
class Signification(h.Hypothese):
    def __init__(self):
        h.Hypothese.__init__(self)
    """ Méthode : initSignature
        Paramètre : 
            - motA : équivalent du motB dans la langue A
            - motB : équivalent du motA dans la langue B
            - langueA : langue à laquelle appartient le mot A
            - langueB : langue à laquelle appartient le mot B
    """
    def InitSignature(self,motA,motB,langueA,langueB):
        self.signature["Type"] = 'signification'
        self.signature["motA"] = motA
        self.signature["motB"] = motB
        self.signature["langueA"] = langueA
        self.signature["langueB"] = langueB

    """ Méthode : Test
        Paramètres :
            - phraseA : phrase dans laquelle on vas chercher le motA
            - langueA : langue dans laquelle est écrite la phrase A
            - phraseB : phrase dans laquelle on vas chercher le motB
            - langueB : langue dans laquelle est écrite la phrase B
        Objectifs:
            Tester l'hypothèse
        Retour:
            - 1 si l'hypothèse est confirmer
            - 0 sinon
    """
    def Test(self,phraseA,langueA,phraseB,langueB):
        if langueA == self.signature["langueA"] :
            if self.signature["motA"]  in phraseA and self.signature["motB"]  in phraseB:
                return 1
            else :
                return 0
        else:
            if self.signature["motB"] in phraseA and self.signature["motA"]  in phraseB:
                return 1
            else :
                return 0    
