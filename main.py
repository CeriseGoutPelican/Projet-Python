# ----------------------------------------------
# - Importation des bibliothèques & constantes -
# ----------------------------------------------

# ----------------------------------------------
# - Importation des fichiers projet            -
# ----------------------------------------------

from access import *
from files import *
import argparse

# ----------------------------------------------
# - Point d'entrée de l'application            -
# ----------------------------------------------

import warnings
from loggingParams import *

def main(logger, infos, journal, errors, debug):

    logger.info("========================= DEBUT DU MODE DEBBUG =========================")
    logger.info("Fichier acces : " + infos)
    logger.info("Fichier journal : " + journal)
    logger.info("Fichier erreurs : " + errors)
    logger.info("Debbug : " + str(debug))
    logger.info("------------------------------------------------------------------------")

    accesToCheck = readingFile(logger, infos)

    # Pour tous les sites distants à tester listés dans le fichier
    for c in accesToCheck:

        c = str(c).split("|")
        l = c[0].split("://")

        localisation = l[1]
        protocol     = l[0]
        account      = c[1].split(",")
        expectedCode = c[2]
        expectedResult = c[3].rstrip()

        try:
            l = loggingAccess(logger, [protocol, localisation, account[0]], access(logger, localisation, protocol,  account, int(expectedCode), expectedResult), journal, errors)
        except Exception as e:
            l = loggingAccess(logger, [protocol, localisation, account[0]], (False, False))

        logger.info(l)

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def parseargs(parser):
    """
    Permet de récupérer les informations
    """
    #params
    parser.add_argument('--access', required = True, dest="access", type = str, help = 'Path to the file countaining every website, ftp, etc. to watch')
    parser.add_argument('--journal', required = True, dest="journal", type = str, help = 'Path to the logging journal file to create or to complete')
    parser.add_argument('--errors', required = True, dest="errors", type = str, help = 'Path to the errors file to create or to complete')
    parser.add_argument('--debug', required = False, dest="debug", nargs='?', const=True, type = str2bool, help = 'y/n to activate debug mode')

    return parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
    """
    main entry
    """
    # parser
    parser = argparse.ArgumentParser(description='Process some integers.')
    args = parseargs(parser)

    # Logger
    logging.basicConfig(datefmt=DATE_FMT,format=STR_FMT, level=logging.INFO)
    logger = logging.getLogger()

    # Mode debug
    if args.debug is True:
        logger.setLevel(logging.INFO)
        logger.disabled = False
    else:
        warnings.filterwarnings("ignore")
        logger.disabled = True
        logging.getLogger("paramiko").setLevel(logging.WARNING)

    # Go
    main(logger, args.access, args.journal, args.errors, args.debug)

