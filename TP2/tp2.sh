#!/bin/bash

set -x 
set -e

# Changer le "motd"
ansible all -i inventory -m copy -a "dest=/etc/motd content=Welcome!" --become

# Installer apache grâce au module yum ou apt
ansible mes_debians -i inventory -m apt -a "name=apache2 state=present" --become
ansible mes_centos -i inventory -m yum -a "name=httpd state=present" --become

# Copier un fichier de la machine cliente vers les machines distantes (fichier html à placer dans /var/www/html/)
ansible all -i inventory -m copy -a "src=index.html dest=/var/www/html/" --become

# Démarrer apache
ansible mes_debians -i inventory -m service -a "name=apache2 state=started" --become
ansible mes_centos -i inventory -m service -a "name=httpd state=started" --become

# Redémarrer les machines
ansible all -i inventory -m reboot --become