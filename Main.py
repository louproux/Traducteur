import Langue as l
import CoupleLangue as cl
import SetEntrainement as s

japonais = l.Langue("japonais",'/')
francais = l.Langue("francais",' ')
jpfr = cl.CoupleLangue(japonais,francais)

testSet = []
testSet.append(s.SetEntrainement("その箱の右の茶碗はいくらですか","japonais","la tasse là à droite de cette boite combien vaut-elle ?","francais"))
testSet.append(s.SetEntrainement("今晩中華料理を食べましょうか","japonais","on vas au restaurant chinois ce soir","francais"))
testSet.append(s.SetEntrainement("中華料理が大好きです","japonais","j'adore la cuisine chinoise","francais"))

for i in testSet:
    jpfr.Entrainement(i)

jpfr.AfficherHypothese()
