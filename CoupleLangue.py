""" class : CoupleLangue
    Paramètre : 
        - LangueA : définit la langue A du couple , type : Langue
        - LangueB : définit la langue B du couple , type : Langue
    Attributs :
        - hypotheses : une liste des hypothèses encore à vérifier
        - lois : une liste des hypothèses vérifier et qui sont maintenant tenues pour acquises
"""
import Signification as s

class CoupleLangue:
    def __init__(self,langueA,langueB):
        self.a = langueA
        self.b = langueB
        self.hypotheses = []
        self.lois = []

    """ méthode : Entrainement
        Paramètre : 
            - setEntr : le set d'entrainement, type : SetEntrainement
        Objectif : 
            Entraine la traduction entre les deux langues du couple
    """
    def Entrainement(self,setEntr):
        lA = []
        lB = []
        if(setEntr.langueA == self.a.nom) :
            lA = self.a.CreationSetMots(setEntr.phraseA)
            lB = self.b.CreationSetMots(setEntr.phraseB)
        else:
            lA = self.a.CreationSetMots(setEntr.phraseB)
            lB = self.b.CreationSetMots(setEntr.phraseA)
        self.TestHypothese(setEntr.phraseA,setEntr.phraseB)
        self.CreerHypothese(lA,lB)
        self.DetruireHypotheseFausse()
        
        
    """ méthode : TestHypothese
        Paramètres : 
            - phraseA : phrase dans laquelle on vas tester l'hypothèse
            - phraseB : phrase dans laquelle on vas tester l'hypothèse
        Objectifs :
            Tests toutes les hypothèses
    """
    def TestHypothese(self,phraseA,phraseB):
        for hypothese in self.hypotheses:
            if(hypothese.signature["Type"] == 'signification'):
                res = hypothese.Test(phraseA,self.a.nom,phraseB,self.b.nom)
                hypothese.ChangerCredibilite(res)

    """ Méthode : CreerHypothese
        Paramètres : 
            - lA : la liste comprennant les mots de la phrase A
            - lB : la liste comprennant les mots de la phrase B
        Objectifs : 
            Creer des hypothèses à partir du set d'entrainement
    """
    def CreerHypothese(self,lA,lB):
        for motA in lA:
            for motB in lB:
                temp = s.Signification()
                temp.InitSignature(motA,motB,self.a.nom,self.b.nom)
                self.hypotheses.append(temp)

    """ Méthode :  DetruireHypothese
        Objectifs : 
            Détruire les hypothèses fausses
    """
    def DetruireHypotheseFausse(self):
        for hypothese in self.hypotheses:
            if hypothese.credibilite < hypothese.seuilFaux :
                self.hypotheses.remove(hypothese)

    def AfficherHypothese(self):
        for i in self.hypotheses:
            print(i.signature["motA"] + " = " + i.signature["motB"] + " credibilite : "+str(i.credibilite))