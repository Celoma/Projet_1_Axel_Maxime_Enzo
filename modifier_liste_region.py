import csv


def import_table_dicos(fichier):
    """
    fonction utiliser l'année derniere pour ouvrir csv en list de dico

    """
    f = open(fichier, "r", encoding="utf-8")
    tab_dico = []
    lignes = f.readlines()
    f.close()
    descripteurs = lignes[0].strip().split(";")
    for i in range(1, len(lignes)):
        dico = {}
        valeurs = lignes[i].strip().split(";")
        for j in range(len(valeurs)):
            dico[descripteurs[j]] = valeurs[j]
        tab_dico.append(dico)
    return tab_dico



def ajuster_coor(tab):
    """
    renvoie la list de dico avec les coordonnées lisable par folium

    :param tab(dico): tableau de dico composer des clefs "latitude" et "longitude"

    :rtype:  tab(dico)

    """
    for i in range(len(tab)):
        if tab[i]["Latitude"][-1] == "N" :
            eff_dir = "N"
            tab[i]["Latitude"] = tab[i]["Latitude"].rstrip(eff_dir)
        else :
            eff_dir = "S"
            tab[i]["Latitude"] = "-" + tab[i]["Latitude"].rstrip(eff_dir)
        if tab[i]["Longitude"][-1] == "E" :
            eff_dir = "E"
            tab[i]["Longitude"] = tab[i]["Longitude"].rstrip(eff_dir)
        else :
            eff_dir = "W"
            tab[i]["Longitude"] = "-" + tab[i]["Longitude"].rstrip(eff_dir)
    return tab

tab = import_table_dicos("region_coord.csv")

true_region_coord = ajuster_coor(tab)
labels = ['Endroits', 'Latitude', 'Longitude']
try:
    with open('true_region_coord.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for elem in true_region_coord:
            writer.writerow(elem)
except IOError:
    print("I/O error")
