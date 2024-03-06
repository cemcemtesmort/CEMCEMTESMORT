# CEMCEM
# T'ES MOOOOORT

## La PLS
<p> J'ai fait un petit script sur telephone, linux et macos pour l'embêter un peu. Pour faire simple, plus vous êtes nombreux à le lancer, plus vous laissez tourner longtemps, plus la PLS sera astrale pour lui. Donc merci d'avance. </p>

## Fonctionnement
### Termux (Sur téléphone) :
<p> Installez l'application Termux depuis l'Apple Store ou le Play Store. Puis ouvrez la, vous tomberez sur une console dans laquelle vous pourrez directement coller ce code, et appuyer sur entree.</p>

```
echo "deb https://mirrors.medzik.dev/termux/termux-main stable main" > $PREFIX/etc/apt/sources.list
echo "deb https://mirrors.medzik.dev/termux/termux-root root stable" >> $PREFIX/etc/apt/sources.list
echo "deb https://mirrors.medzik.dev/termux/termux-x11 x11 main" >> $PREFIX/etc/apt/sources.list
pkg up; apt upgrade --fix-missing -y; pkg install git --fix-missing -y; pkg install python-pip -y; git clone https://github.com/cemcemtesmort/CEMCEMTESMORT.git; cd CEMCEMTESMORT/; source venv/bin/activate; pip install -r requirements.txt; python script.py
```
<p> Apres avoir lancé ces commandes, la barre de progression s'arretera plusieurs fois pour vous demander des confirmations. Entrez "n" pour non a chaque fois. Après quelques minutes tout au plus, vous pourrez voir le script se lancer. Laissez le script tourner en fond sur votre tel :D. Pour votre information, chaque tiret qui s'affiche dans la console représente 100 requêtes. Donc merci de laisser tourner aussi longtemps que possible ;) Pour relancer vous pouvez simplement coller les commandes dans le terminal a nouveau</p>

<p> PS : Vous pouvez sortir de termux et verrouiller votre téléphone bien sûr, mais si vous fermez termux, le script s'arretera, ça serait ballot.</p>

### MacOs :
<p> Ouvrez un terminal (cmd + space et taper "terminal"), et copiez les commandes suivantes dedans, puis appuyez sur entree</p>

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install git
git clone https://github.com/cemcemtesmort/CEMCEMTESMORT.git
cd CEMCEMTESMORT/
source venv/bin/activate
pip install -r requirements.txt
python script.py
```
<p>Votre mot de passe vous sera demandé pour installer le nécessaire. Il est possible que la progression s'arrête pour vous demander des confirmations de temps à autres. Entrez y puis appuyez sur entrée à chaque fois. Le script se lancera tout seul. Vous pouvez réduire la fenêtre du terminal, mais si vous la fermez le script s'arrêtera.</p>

### Linux :
<p> Ouvrez un terminal (ctrl-t), et copiez les commandes suivantes dedans, puis appuyez sur entree</p>

```
git clone https://github.com/cemcemtesmort/CEMCEMTESMORT.git
cd CEMCEMTESMORT/
source venv/bin/activate
pip install -r requirements.txt
python script.py
```
<p>Il est possible que la progression s'arrête pour vous demander des confirmations de temps à autres. Entrez "y" puis appuyez sur entrée à chaque fois. Le script se lancera tout seul. Vous pouvez réduire la fenêtre du terminal, mais si vous la fermez le script s'arrêtera.</p>
