## 09/09

- recherche de fichiers interréssants sur [data.gouv.fr](data.gouv.fr/) pour choisir un projet -- choisi [données météorologiques](https://www.data.gouv.fr/fr/datasets/donnees-d-observation-des-principales-stations-meteorologiques/) 
- essaie de code pour récup le fichier sur internet directement -- fait grace au module wget
- Essayer de mettre marqueur sur map

## 16/09

- essayer affichage marqueur température sur map
- essaye du module 'wget' sur pc du lycée --- marche sur les pc où wget est installé
- conversion des coordonnées mal écrite sur le fichier [coord_région](https://github.com/NSImoulin2023/Projet_1_Axel_Maxime_Enzo/blob/main/region_coord.csv)
- defini qui fait quoi -- meilleur organisation

### Dans la prochaine séance
1. Créer une fonction qui rassemble les différents fichiers csv uilisés et supprime les données inutiles
2. Finir la fonction qui corrige les données mal-écrites

## 17/09 (Maxime - séance perso)

- fonction 'recup_fichier' qui recupère le fichier compressé venant de [la source](https://www.data.gouv.fr/fr/datasets/donnees-d-observation-des-principales-stations-meteorologiques/)
- fonction 'extraction_csv' qui décompresse le fichier compressé précedemment téléchargé

## 18/09 (Axel - séance perso)

- Modifier le fichier csv "region_coord" pour remplacer les coordonées 'N,S,W,E' par les carractères '+' ou '-' dans le csv "true_region_coord" à l'aide d'une fonction python.
