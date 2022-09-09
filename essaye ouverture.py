import csv

with open("U:\Downloads\temperature-quotidienne-regionale.csv",encoding="utf-8") as fh:
    lecteur_dico = csv.DictReader(fh)
    print (lecteur_dico)