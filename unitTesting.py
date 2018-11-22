# ----------------------------------------------
# - Importation des bibliothèques & constantes -
# ----------------------------------------------

# ----------------------------------------------
# - Importation des fichiers projet            -
# ----------------------------------------------

from access import *
from tests import *

# ----------------------------------------------
# - Tests unitaires                            -
# ----------------------------------------------

def tests_unitaires():
    """
    Inscrire simplement ici tous les tests unitaires à effectuer

    :return: rien du tout
    """
    # LOGIN -------------------------------------
    logger = logging.getLogger()

    # HTTP --------------------------------------
    test_unitaire(access, (True, True), logger, "local.techno-web.fr", "http",  ("admin", "admin"), 200, 'Admin')
    test_unitaire(access, (True, False), logger, "local.techno-web.fr/test.html", "http",  ("admin", "admin"), 404, "Admin")
    test_unitaire(access, (True, False), logger, "local.techno-web.fr", "http",  ("root", "root"), 200, "Admin")
    test_unitaire(access, 'ERROR', logger, "local.techno-web-error.fr", "http",  ("admin", "admin"), 503, "Admin")

    # HTTPS -------------------------------------
    test_unitaire(access, (True, True), logger, "techno-web.fr", "https",  ("Gregoire.GAONACH", "azerty"), 200, "welcome Gregoire")
    test_unitaire(access, "ERROR", logger, "bidon.techno-web.fr", "https",  ("Gregoire.GAONACH", "azerty"), 200, "welcome Gregoire")

    # FTP ---------------------------------------
    test_unitaire(access, (True, True), logger, "ftp.dlptest.com", "ftp",  ("dlpuser@dlptest.com", "e73jzTRTNqCN9PYAAjjn"), 230)
    test_unitaire(access, "ERROR", logger, "ftp.dlptest-error.com", "ftp",  ("dlpuser@dlptest.com", "e73jzTRTNqCN9PYAAjjn"), 230)
    test_unitaire(access, (True, True), logger, "ftp.dlptest.com", "ftp",  ("dlpuser@dlptest.com", "bidon"), 530)

    # SFTP --------------------------------------
    test_unitaire(access, (True, True), logger, "test.rebex.net", "sftp", ("demo", "password"), 230)
    test_unitaire(access, "ERROR", logger, "adresse.bidon", "sftp", ("demo", "password"), 230)
    test_unitaire(access, "ERROR", logger, "test.rebex.net", "sftp", ("demo", "bidon"), 230)

    # SSH ---------------------------------------
    test_unitaire(access, (True, True), logger, "test.rebex.net", "ssh", ("demo", "password"), 230)
    test_unitaire(access, (False, True), logger, "test.rebex.net", "ssh", ("demo", "bidon"), 230)
    test_unitaire(access, (False, True), logger, "adresse.bidon", "ssh", ("demo", "password"), 230)

# ----------------------------------------------
# - Main entry                                 -
# ----------------------------------------------

start_tests(tests_unitaires)
