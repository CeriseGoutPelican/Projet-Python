# Projet python (séance n°4)

Ce projet permet de vérifier la connexion d'un ensemble de serveurs distants et d'inscrire les retours dans différents fichiers log. Ce projet a été réalisé dans le cadre du cours "Python Scripting" par Grégoire Gaonach, Mathieu Gabriel et Adrien Delaurens.
### 1. Installation et utilisation
##### 1.a) Gestion des dépendances
La connexion avec les protocoles _http_ utilise la biliothèque de base `urllib3`. Cependant, pour le protocole _https_, il est nécessaire d'utiliser un certificat de vérification SSL [comme undiqué dans la documentation de la bibliothèque](https://urllib3.readthedocs.io/en/latest/user-guide.html#certificate-verification) à l'aide de `certifi`.

```
$ py -3.6 -m pip install certifi
```

Pour les protocoles _ssh_ et _sftp_, il a été décidé d'utiliser la bibliothèque `paramiko` qui permet de gérer les connexion ssh distantes ([voir la documentation](http://www.paramiko.org/)).

```
$ py -3.6 -m pip install paramiko
```
##### 1.2) Chargement des serveurs distants à tester
Il est possible de tester soit des serveurs distants, soit des serveurs locaux au travers du fichier `access.data` situé à la racine du projet. Le fichier se structure de la manière suivante : `protocole://ip|utilisateur,motDePasse|codeServeur|RetourAttendu`. Voici un exemple de fichier :
```
http://local.techno-web.fr|admin,admin|200|Admin
https://techno-web.fr|Gregoire.GAONACH,azerty|200|welcome Gregoire
ftp://ftp.dlptest.com|dlpuser@dlptest.com,e73jzTRTNqCN9PYAAjjn|230|
sftp://test.rebex.net|demo,password|230|
ssh://test.rebex.net|demo,password|230|
```
L'adresse _local.techno-web.fr_ est la seule adresse locale (127.0.0.1) et ne pourra pas être utilisée pour vos propres tests. Les autres sont tous des tests distants.

Afin de tester la connexion ftp, on a décidé d'utiliser le service dlptest dont vous trouverez [la documentation ici](https://dlptest.com/ftp-test/). Pour les connexions SFTP et SSH, on utilise le service distant Rebex dont vous trouverez [la documentation par ici](http://test.rebex.net/).

##### 1.3) Démarer le logiciel
Pour lancer le fichier il suffit d'ouvrir un terminal de commande et de lancer le fichier `main.py` comme le montre l'exemple suivant :
```
$ py -3.6 main.py --access access.data --journal journal.log --errors errors.log --debug 0
```
En cas d'hésitation sur les arguments, vous pouvez utiliser la fonction `--help`.

### 2. Les fichiers logs

Les fichiers logs se structurent en deux parties : un journal complet et un fichier contenant uniquement les erreurs. Voici un exemple de structure :
```
[ATTENTION] [22/11/2018 14:46] Connexion ssh réussie pour l'adresse test.rebex.net mais erreur de connexion avec l'utilisateur demo
[REUSSI] [22/11/2018 15:21] Connexion http réussie pour l'adresse local.techno-web.fr avec l'utilisateur admin
```

### 3. Structure du projet
| Nom du fichier   | Description du fichier                                                                                                                |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| main.py          | Point d'entrée du programme à lancer depuis le terminal. Il contient les codes des arguments et appelle les autres fichiers sources.  |
| access.py        | Permet de rediriger les protocoles demandés sur les bonnes fonctions stockées sur checks.py                                           |
| checks.py        | Contient les fonctions d'accès aux serveurs distants                                                                                  |
| files.py         | Permet de gérer l'écriture et la lecture des différents fichiers du projets (log et erreurs)                                          |
| unitTesting.py   | Permet de lancer les différents tests unitaires du projet                                                                             |
| tests.py         | Ensemble de fonctions gérant et lançant les tests unitaires                                                                           |
| loggingParams.py | Permet de lancer les paramètres généraux du logger et d'afficher la version de Python active                                          |
| access.data      | Liste des serveurs à tester                                                                                                           |
| errors.log       | Log d'erreurs                                                                                                                         |
| journal.log      | Journal de logs                                                                                                                       |

### 4. Le debug
En cas de problème, deux fonctions sont offertes pour tester le programme. Les fichiers `tests.py`, `loggingParams.py` et `UnitTeststing.py` permettent de lancer une série de tests unitaires (attention au serveur local sur les tests http).
Les tests unitaires sont définis sur ce dernier fichier. Voici un retour du test unitaire :
```
22/11/2018 16:43:26 -     INFO : 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)]
22/11/2018 16:43:26 -     INFO : ========================= DEBUT DES TESTS UNITAIRES =========================
22/11/2018 16:43:26 -     INFO : Le test unitaire s'est bien déroulé pour access(<RootLogger root (INFO)>, 'local.techno-web.fr', 'http', ('admin', 'admin'), 200, 'Admin')
22/11/2018 16:43:26 -     INFO : Le test unitaire s'est bien déroulé pour access(<RootLogger root (INFO)>, 'local.techno-web.fr', 'http', ('root', 'root'), 200, 'Admin')
22/11/2018 16:43:26 -     INFO : Le test unitaire s'est bien déroulé pour access(<RootLogger root (INFO)>, 'local.techno-web-error.fr', 'http', ('admin', 'admin'), 503, 'Admin')
22/11/2018 16:43:28 -     INFO : Le test unitaire s'est bien déroulé pour access(<RootLogger root (INFO)>, 'techno-web.fr', 'https', ('Gregoire.GAONACH', 'azerty'), 200, 'welcome Gregoire')
22/11/2018 16:43:28 -     INFO : Le test unitaire s'est bien déroulé pour access(<RootLogger root (INFO)>, 'bidon.techno-web.fr', 'https', ('Gregoire.GAONACH', 'azerty'), 200, 'welcome Gregoire')
22/11/2018 16:43:30 -     INFO : Le test unitaire s'est bien déroulé pour access(<RootLogger root (INFO)>, 'ftp.dlptest.com', 'ftp', ('dlpuser@dlptest.com', 'e73jzTRTNqCN9PYAAjjn'), 230)
22/11/2018 16:43:30 -     INFO : Le test unitaire s'est bien déroulé pour access(<RootLogger root (INFO)>, 'ftp.dlptest-error.com', 'ftp', ('dlpuser@dlptest.com', 'e73jzTRTNqCN9PYAAjjn'), 230)
22/11/2018 16:43:36 -     INFO : Le test unitaire s'est bien déroulé pour access(<RootLogger root (INFO)>, 'ftp.dlptest.com', 'ftp', ('dlpuser@dlptest.com', 'bidon'), 530)
22/11/2018 16:43:38 -     INFO : Le test unitaire s'est bien déroulé pour access(<RootLogger root (INFO)>, 'adresse.bidon', 'sftp', ('demo', 'password'), 230)
22/11/2018 16:43:39 -     INFO : Le test unitaire s'est bien déroulé pour access(<RootLogger root (INFO)>, 'test.rebex.net', 'sftp', ('demo', 'bidon'), 230)
22/11/2018 16:43:40 -     INFO : Le test unitaire s'est bien déroulé pour access(<RootLogger root (INFO)>, 'test.rebex.net', 'ssh', ('demo', 'password'), 230)
22/11/2018 16:43:42 -     INFO : Le test unitaire s'est bien déroulé pour access(<RootLogger root (INFO)>, 'test.rebex.net', 'ssh', ('demo', 'bidon'), 230)
22/11/2018 16:43:42 -     INFO : Le test unitaire s'est bien déroulé pour access(<RootLogger root (INFO)>, 'adresse.bidon', 'ssh', ('demo', 'password'), 230)
22/11/2018 16:43:42 -     INFO :  
22/11/2018 16:43:42 -     INFO : Nombre de tests : 15 / passés : 15 / erreurs : 0
22/11/2018 16:43:42 -     INFO : =============================================================================
```

Il est également possible d'afficher des messages de debug placés à des endroits clés du programme en passant le paramètre `--debug 1` sur sa position `True`.
