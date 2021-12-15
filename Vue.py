from appJar import gui
import Modèle
import Contrôleur

app = gui()

liste_animaux = ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']
liste_actions = ['nourrir', 'divertir', 'coucher', 'reveiller']

def refresh():
    for animal in liste_animaux:
        état = Modèle.lit_état(animal)
        lieu = Modèle.lit_lieu(animal)
        race = Modèle.lit_race(animal)
        app.setLabel(f"{animal}", f"{animal}")
        app.setLabel(f'{animal} état', f'{race}, {état}, {lieu}')

def press():
    action = None
    animal = app.getRadioButton("id_animal")
    lieu_passé = Modèle.lit_lieu(animal)
    if app.getRadioButton('action') == 'nourrir':
        disp = Modèle.vérifie_disponibilité('mangeoire')
        action = Contrôleur.nourrir(animal)
    elif app.getRadioButton('action') == 'divertir':
        disp = Modèle.vérifie_disponibilité('roue')
        action = Contrôleur.divertir(animal)
    elif app.getRadioButton('action') == 'coucher':
        disp = Modèle.vérifie_disponibilité('nid')
        action = Contrôleur.coucher(animal)
    elif app.getRadioButton('action') == 'reveiller':
        disp = Modèle.vérifie_disponibilité('litière')
        action = Contrôleur.reveiller(animal)
    if disp == 'libre' and lieu_passé != Modèle.lit_lieu(animal):
        app.infoBox("", f"Félicitations, {animal} a rejoint le/la {Modèle.lit_lieu(animal)} et est maintenant {Modèle.lit_état(animal)}.")
    if action != None:
        app.warningBox("", action)
    refresh()

app.addLabel("en-tête", "Bienvenue à l'animalerie!", 0, 0, 2)
app.setLabelBg("en-tête", "salmon")
app.setLabelFg("en-tête", "white")

app.addLabel("sous-titre", "Tableau de bord", 1, 0, 2)
app.setLabelBg("sous-titre", "gray")
app.setLabelFg("sous-titre", "white")

for index,animal in enumerate(liste_animaux):
    état = Modèle.lit_état(animal)
    lieu = Modèle.lit_lieu(animal)
    race = Modèle.lit_race(animal)
    app.addLabel(f'{animal}',f'{animal}',index+2 ,0)
    app.addLabel(f'{animal} état', f'{race}, {état}, {lieu}', index+2 , 1)
    if index % 2 == 0:
        app.setLabelBg(f'{animal}', "lavender")
        app.setLabelBg(f'{animal} état', "lavender")

app.addLabel("sous-titre2", "Actions", len(liste_animaux)+2, 0, 2)
app.setLabelBg("sous-titre2", "gray")
app.setLabelFg("sous-titre2", "white")

for index, animal in enumerate(liste_animaux):
    app.addRadioButton("id_animal", animal,len(liste_animaux)+2+index+1,0)

for index,action in enumerate(liste_actions):
    app.addRadioButton("action", action,len(liste_animaux)+2+index+1, 1)

app.addButton('Go', press, 2*len(liste_animaux)+2+len(liste_actions)+1,0,2)

# Button go permet de lancer l'exécution d'une fonction selon la syntaxe
app.go()
