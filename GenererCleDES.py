# -*- coding: utf-8 -*-

from Fonctions import *

def GenererCles(cle, fonctionPermutation):
    clePermute = permutation(cle, fonctionPermutation)
    k1_ = clePermute[0:len(clePermute)//2]
    k2_ = clePermute[len(clePermute)//2:len(clePermute)]
    
    k1 = ouExclusive(k1_, k2_)
    k2 = etLogique(k2_, k1_)
    
    k1 = decalageGauche(k1, 2)
    k2 = decalageDroit(k2, 1)
    
    return "(" + k1 + ", " + k2 + ")"

result = GenererCles("01101101", "65274130")

print(result)



