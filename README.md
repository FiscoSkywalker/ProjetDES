# ProjetDES
## Resumé
Ce projet concerne la génération des clés, le chiffrement et déchiffrement avec la méthode de cryptage DSE

Nous avons au prélable écrit des fonctions qui nous ont permis d'éffectuer certanines opérations notamment comme le ou inclusive, le ou exclusive, la fonction de permutation, le et logique, le decalage à gauche, le decalge à droite ainsi qu'une fonction pour calculer l'inverse de la permutation.

voici les codes des différentes fonctions

### Fonction permutation


```Python
def permutation(cle, perm):
    if len(cle) != len(perm) :
        return -1
    
    clePermute = ""
    for car in perm:
        index = int(car)
        clePermute = clePermute + cle[index]
        
    
    return clePermute
```

### Fonction ouExclusive
```Python
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
```

### Fonction ouInclusive
```Python
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
```

### Fonction etLogique
```Python
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
```

### Fonction decalageGauche
```Python
def decalageGauche(cle, ordre):
    decal = cle[0:ordre]
    reste = cle[ordre:len(cle)]
    
    return reste + decal
```

### Fonction decalageDroit
```Python
def decalageDroit(cle, ordre):
    taille = len(cle)
    diff = taille - ordre
    
    decal = cle[diff:taille]
    reste = cle[0:diff]
    
    return decal + reste
```

### Fonction inversePermutation
```Python
def inversePermutation(fonctionPermutation):
    result = ""
    i = 0
    
    for i in range(0, len(fonctionPermutation)):
        result = result + str(fonctionPermutation.index(str(i), 0, len(fonctionPermutation)))
        
    return result
```

![alt text](https://github.com/FiscoSkywalker/ProjetDES/blob/master/images/permutation.PNG)
