# CEMCEM
# T'ES MOOOOORT

## Le principe
<p> Le proxenete amateur cemcem a host toutes les images de son site upfollow.com sur ce qu'on appelle un bucket s3. Un bucket s3 c'est un genre de disque dur en ligne tenu par amazon. Le truc c'est que toutes les x requetes, ca lui coute de l'argent au pépère. Et la bonne nouvelle, c'est qu'on peut en faire plein :)</p>

## La PLS
<p> J'ai fait un petit script pour faire des requetes en boucle sur son s3. Pour faire simple, plus vous laissez tourner longtemps, plus la PLS sera astrale pour lui.</p>

## Fonctionnement
### Mac / Linux :
<p> Ouvrez un terminal (cmd + space et taper "terminal" sous macos, ou alors ctrl-t sous linux), et copiez les commandes suivantes dedans, puis appuyez sur entree</p>

```
git clone https://github.com/cemcemtesmort/CEMCEMTESMORT.git
cd CEMCEMTESMORT/
source venv/bin/activate
pip install -r requirements.txt
python script.py
```

### Windows :
<p>Téléchargez le repo en zip (bouton vert en haut a droite), puis dézipez le sur votre bureau. Appuyez sur la touche windows, tapez "powershell" dans la barre de recherche. Clic droit sur powershell -> executer en tant qu'administrateur. Copiez les commandes suivantes dedans, puis appuyez sur entree</p>

```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
cd ~\Desktop\CEMCEMTESMORT-master
.\venv\bin\Activate.ps1
pip install -r .\requirements.txt
python script.py
```

<p>Pour votre information personnelle, chaque tiret qui s'affiche dans la console représente 100 requêtes. Merci de laisser tourner aussi longtemps que possible :) </p>

<p> PS : Vous pouvez réduire la fenetre de la console, mais si vous la fermez le script s'arretera, ça serait ballot.</p>
