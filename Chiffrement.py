# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 15:05:29 2023

@author: EJEUNA1
"""

from Fonctions import *

def chiffrement(n, pi, p, k1, k2):
    clePermute = permutation(n, pi)
    G0 = clePermute[0:len(clePermute)//2]
    D0 = clePermute[len(clePermute)//2:len(clePermute)]
    
    D1 = ouExclusive(permutation(G0, p), k1)
    G1 = ouExclusive(D0, ouInclusive(G0, k1))
    
    D2 = ouExclusive(permutation(G1, p), k2)
    G2 = ouExclusive(D1, ouInclusive(G1, k2))
    
    C = G2 + D2
    
    pi_1 = inversePermutation(pi)
    
    result = permutation(C, pi_1)
    
    return result

print(chiffrement('01101110', '46027315', '2013', '1110', '0010'))
    
    