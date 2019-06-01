""" Class : Langue
    Paramètres : 
        - nom : le nom de la langue qui lui servira d'identificateur, type : String
        - separateur : indique le separateur entre chaque mots de la langue,si il n'y à pas de séparateur dans la langue alors séparateur = /, type : String/Char
"""

class Langue:
    def __init__(self,_nom,_separateur):
        self.nom = _nom
        self.separateur = _separateur


    """ Méthode : CreationSetMots
        Paramètres : 
            - phrase : phrase sur laquelle appliqué le séparateur
        Objectifs :
            Creer une liste avec les mots suceptible d'être traduit
        Retour :
            liste contenant tout les mots possiblement traductible
    """
    def CreationSetMots(self,phrase):
        res = []
        if(self.separateur != '/'):
            lPhrase = phrase.split()
            for mot in lPhrase:
                res.append(mot)
        else:
            for i in range(len(phrase)) :
                for j in range(i+1,len(phrase)):
                    res.append(phrase[i:j])
        return res



