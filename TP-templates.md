# TP : Utilisation des templates

Le but de ce TP est de découvrir le moteur de template jinja

Documentation officielle du langage

https://jinja.palletsprojects.com/en/3.0.x/

## Création d'un motd

Documentations structures de controle

https://jinja.palletsprojects.com/en/3.0.x/templates/#list-of-control-structures

Ecrire le template permettant de générer le motd suivant, les variables utilisées devront provenir des facts :

```
Bienvenue sur le serveur <hostname>

OS: <Nom du systeme>
Version: <Version du systeme>
Noyau: <Version du noyau utlisé>
Gestionnaire de paquets: <Nom du gestionnaire de paquets>
Gestionnaire de services: <Nom du service d'init>

Liste DNS:
  - <dns 1>
  - <dns 2>
  - ...

Interfaces réseau:
  - <Nom de l'interface 1>: <Ip interface 1>
  - <Nom de l'interface 2>: <Ip interface 2>
  - ...

Partitions disques:
  - <Nom de la partition 1> <Taille>
  - <Nom de la partition 2> <Taille>
  - ...
```

Ecrire le playbook et le template permettant d'envoyer ce fichier sur les machines virtuelles, vérifier que le motd est bien généré en ouvrant une connexion ssh sur les machines virtuelles, ou bien avec la commande `watch cat /etc/motd`
