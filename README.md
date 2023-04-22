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

![alt text](https://github.com/FiscoSkywalker/ProjetDES/blob/master/images/permutation.PNG)
