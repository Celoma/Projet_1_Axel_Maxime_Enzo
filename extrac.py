import gzip
import shutil


def extraction_csv(fichier):
    """Décompresse un fichier csv vers un fichier nommé donnees.csv
    
    :param fichier(.csv.gz) fichier: Fichier avec .csv.gz comme extension

    :rtype: none
    """
    with gzip.open(fichier, 'rb') as f_in:
        with open('donnees.csv', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
