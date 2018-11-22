import os
import datetime

def readingFile(logger, path):
    """
    Permet de lire un fichier en lecture seule

    :param logger: logging pour debug
    :param path: chemin relatif du fichier
    :return: le contenu du fichier ou False en cas d'erreur
    """

    # Reading the file
    try:
        logger.info("Lecture du fichier " + path)

        f = open(os.path.join(os.path.dirname(__file__), path), "r")
        content = f.readlines()
        f.close()

        logger.info("Contenu du fichier : " + str(content.__len__()) + " lignes dans le fichier")

        return content

    except Exception as e:
        logger.error("Erreur : pas de fichier trouvé pour " + path)
        return False

def writtingFile(logger, path, content):
    """
    Permet d'écrire dans les fichiers logs en append

    :param logger: logging pour debug
    :param path: chemin relatif du fichier à éditer ou créer
    :param content: contenu à rajouter sur la lgne du log
    :return: True en cas de succès, False en cas d'erreur
    """

    try:
        logger.info("Création ou mise à jour du fichier " + path)

        f = open(os.path.join(os.path.dirname(__file__), path), "a")
        f.write(content)
        f.close()
        return True

    except Exception as e:
        logger.error("Erreur : lors de la création du fichier " + path)
        return False

def loggingAccess(logger, test, callback, journalFile, errorsFile):
    """
    Permet de convertir les données de retour de la fonction access en ligne facile à lire pour les logfiles

    :param logger: logging pour debug
    :param test: données du test (0 : protocol ; 1 : adresse ; 2 : username)
    :param callback: retour de la fonction access
    :param journalFile: chemin du fichier journal
    :param errorsFile: chemin du fichier d'erreur
    :return: le log formaté
    """

    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M")

    # Tout s'est bien passé
    if callback == (True, True):
        log = "[REUSSI] ["+date+"] Connexion " + test[0] + " réussie pour l'adresse " + test[1] + " avec l'utilisateur " + test[2] + "\n"

        writtingFile(logger, journalFile, log)

    elif callback == (False, True):
        log = "[ATTENTION] ["+date+"] Connexion " + test[0] + " réussie pour l'adresse " + test[1] + " mais erreur de connexion avec l'utilisateur " + test[2] + "\n"

        writtingFile(logger, journalFile, log)
        writtingFile(logger, errorsFile, log)

    else:
        log = "[ERREUR] ["+date+"] Connexion " + test[0] + " échouée pour l'adresse " + test[1] + " avec l'utilisateur " + test[2] + "\n"

        writtingFile(logger, errorsFile, log)

    return log
