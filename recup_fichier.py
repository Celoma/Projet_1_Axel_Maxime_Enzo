import wget, gzip


def recup_fichier(url):
    """Récupère (télécharge) un fichier compressé sur le web grâce au module 'wget'

    :param str url: url menant au fichier sur le web

    :rtype: none
    """
    wget.download(url)

