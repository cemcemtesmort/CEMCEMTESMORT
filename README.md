# CEMCEM
# T'ES MOOOOORT

## Le principe
<p> Le proxenete amateur cemcem a host toutes les images de son site upfollow.com sur ce qu'on appelle un bucket s3. Un bucket s3 c'est un genre de disque dur en ligne tenu par amazon. Le truc c'est que toutes les x requetes, ca lui coute de l'argent</p>

## La PLS
<p> J'ai fait un petit script pour faire des requetes en boucle sur son s3. Sur mon pc portable un peu faible je suis a 1400 requetes par minute. Pour faire simple, plus vous laissez tourner longtemps, plus la PLS sera astrale pour lui.

## Fonctionnement
### Mac / Linux :
<p> Ouvrez un terminal (cmd + space et taper "terminal" sous macos, ou alors ctrl-t sous linux), et copiez les commandes suivantes dedans, puis appuyez sur entree</p>
<code>git clone https://github.com/cemcemtesmort/CEMCEMTESMORT.git && cd CEMCEMTESMORT/
source venv/bin/activate
python script.py
</code>
### Windows :
<p>Telechargez le repo en zip (bouton vert en haut a gauche), puis dézipez le sur votre bureau. Appuyez sur la touche windows, tapez "powershell" dans la barre de recherche. Clic droit sur powershell -> executer en tant qu'administrateur. Copiez les commandes suivantes dedans, puis appuyez sur entree</p>
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force

```
Activate.ps1
