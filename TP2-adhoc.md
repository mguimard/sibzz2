# TP2 : Utilisation des différentes commandes Ad hoc en parallèle sur plusieurs nœuds

Le but de ce TP est de savoir exécuter plusieurs commandes ad-hoc sur tous les noeuds de l'inventaire

## Ecriture d'un inventaire

Ecrire l'inventaire des différentes machines pour pouvoir utiliser la commande suivante

```sh
$ ansible my_machines -i inventory -m debug -a "msg=hello"
```

Exemple de déclaration d'une machine vagrant dans inventaire

`machine1 ansible_ssh_host=192.168.56.11`

L'inventaire devra :

* Séparer dans des groupes les machines debian des machines centos ("machines_debian" et "machines_centos" par exemple)
* Créer un super groupe qui regroupe les machines debian et centos ("my_machines" par exemple)

## Commandes

Réaliser les opérations suivantes à l'aide de commandes ad-hoc (sur toutes les machines)

* Changer le "motd"
* Installer apache grâce au module yum ou apt
* Copier un fichier de la machine cliente vers les machines distantes (fichier html à placer dans /var/www/html/)
* Démarrer apache
* Redémarrer les machines

Vérifiez manuellement que apache est bien démarré après le reboot des machines. Si ce n'est pas le cas, utiliser le module service pour l'activer.

Pour consigner ces commandes nous crérons un fichier tp2.sh

