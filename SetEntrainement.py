""" class : SetEntrainement
    Paramètre : 
        - phraseA : première phrase servant à l'entrainement, type : String
        - langueA : noms de la langue A, type : String
        - phraseB : seoncde phrase servant à l'entrainement, type : String
        - langueB : identifiant de la langue B, type : String
    Attribut :
        - setMotsA : dictionnaire des mots après application du séparateur dans la langue A
        - setMotsB : dictionnaire des mots apès application du séparateur dans la langue B
"""

class SetEntrainement :
    def __init__(self,_phraseA,_langueA,_phraseB,_langueB):
        self.phraseA = _phraseA
        self.langueA = _langueA
        self.phraseB = _phraseB
        self.langueB = _langueB
        self.setMotsA = {}
        self.setMotsB = {}
