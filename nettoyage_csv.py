import pandas as pd
import gzip 
import csv


def nettoyage(fichier):
    with open(fichier, 'w') as donnees:
        '''
        lecteur_dico = csv.DictReader(donnees)
        for dico in lecteur_dico:    
           print(lecteur_dico)
        '''
        f = pd.read_csv(donnees)
        print(f.to_string())


nettoyage('donnees.csv')
