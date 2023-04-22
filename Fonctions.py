# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:31:59 2023

@author: EJEUNA1
"""

def permutation(cle, perm):
    if len(cle) != len(perm) :
        return -1
    
    clePermute = ""
    for car in perm:
        index = int(car)
        clePermute = clePermute + cle[index]
        
    
    return clePermute


def ouExclusive(cle1, cle2):
    if len(cle1) != len(cle2):
        return -1
    
    result = ""
    
    for i in range(0, len(cle1)):
        if (cle1[i] == "0" and cle2[i] == "0") or (cle1[i] == "1" and cle2[i] == "1"):
            result = result + "0"
        else:
            result = result + "1"
            
    
    return result

def ouInclusive(cle1, cle2):
    if len(cle1) != len(cle2):
        return -1
    
    result = ""
    
    for i in range(0, len(cle1)):
        if (cle1[i] == "0" and cle2[i] == "0"):
            result = result + "0"
        else:
            result = result + "1"
            
    
    return result


def etLogique(cle1, cle2):
    if len(cle1) != len(cle2):
        return -1;
    
    result = ""
    
    for i in range(0, len(cle1)):
        if (cle1[i] == "1" and cle2[i] == "1"):
            result = result + "1"
        else:
            result = result + "0"
            
    
    return result


def decalageGauche(cle, ordre):
    decal = cle[0:ordre]
    reste = cle[ordre:len(cle)]
    
    return reste + decal


def decalageDroit(cle, ordre):
    taille = len(cle)
    diff = taille - ordre
    
    decal = cle[diff:taille]
    reste = cle[0:diff]
    
    return decal + reste

def inversePermutation(fonctionPermutation):
    result = ""
    i = 0
    
    for i in range(0, len(fonctionPermutation)):
        result = result + str(fonctionPermutation.index(str(i), 0, len(fonctionPermutation)))
        
    return result