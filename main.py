import recup_fichier 


annee = input("De quelle année voulez-vous afficher les donnés météorologiques ? (en chiffre)")
mois = input("Et de quelle mois ? (en chiffre)")

url = f"https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.{annee}{mois}.csv.gz"

recup_fichier.recup_fichier(url)