# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 15:05:29 2023

@author: EJEUNA1
"""

from Fonctions import *

def dechiffrement(n, pi, p, k1, k2):
    clePermute = permutation(n, pi)
    G2 = clePermute[0:len(clePermute)//2]
    D2 = clePermute[len(clePermute)//2:len(clePermute)]
    
    inv_p = inversePermutation(p)
    
    G1 =  permutation(ouExclusive(D2, k2), inv_p)
    D1 = ouExclusive(G2, ouInclusive(G1, k2))
    
    G0 = permutation(ouExclusive(D1, k1), inv_p)
    D0 = ouExclusive(G1, ouInclusive(G0, k1))
    
    N = G0 + D0
    
    inv_pi = inversePermutation(pi)
    
    result = permutation(N, inv_pi)
    
    return result

print(dechiffrement('10110010', '46027315', '2013', '1110', '0010'))
    
    