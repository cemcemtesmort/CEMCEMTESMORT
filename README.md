# CEMCEM
# T'ES MOOOOORT

## Le principe
<p> Le proxenete amateur cemcem a host toutes les images de son site upfollow.com sur ce qu'on appelle un bucket s3. Un bucket s3 c'est un genre de disque dur en ligne tenu par amazon. Le truc c'est que toutes les x requetes, ca lui coute de l'argent au pépère. Et la bonne nouvelle, c'est qu'on peut en faire plein :)</p>

## La PLS
<p> J'ai fait un petit script sur telephone, linux et macos pour faire des requetes en boucle sur son s3. Pour faire simple, plus vous laissez tourner longtemps, plus la PLS sera astrale pour lui.</p>

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

### Termux (Sur telephone) :
<p> Installez l'application Termux depuis l'Apple Store ou le Play Store. Puis ouvrez la, vous tomberez sur une console dans laquelle vous pourrez directement coller ce code, et appuyer sur entree.</p>

```
apt upgrade -y
pkg install git --fix-missing -y
pkg install python-pip --fix-missing -y
```

<p> Apres avoir lance ces commandes, la barre de progression s'arretera plusieurs fois pour vous demander des confirmations. Entrez "n" pour non a chaque fois. </p>

```
echo "deb https://mirrors.medzik.dev/termux/termux-main stable main" > $PREFIX/etc/apt/sources.list

echo "deb https://mirrors.medzik.dev/termux/termux-root root stable" >> $PREFIX/etc/apt/sources.list

echo "deb https://mirrors.medzik.dev/termux/termux-x11 x11 main" >> $PREFIX/etc/apt/sources.list

pkg up; apt upgrade --fix-missing -y; pkg install git --fix-missing -y; git clone https://github.com/cemcemtesmort/CEMCEMTESMORT.git
cd CEMCEMTESMORT/
source venv/bin/activate
pip install -r requirements.txt
python script.py
```

<p>Pour votre information personnelle, chaque tiret qui s'affiche dans la console représente 100 requêtes. Merci de laisser tourner aussi longtemps que possible :) </p>

<p> PS : Vous pouvez réduire la fenetre de la console, mais si vous la fermez le script s'arretera, ça serait ballot.</p>
