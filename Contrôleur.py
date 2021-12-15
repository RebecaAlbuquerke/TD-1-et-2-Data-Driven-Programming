import Modèle
import json

def nourrir(animal_id):
    with open('animal.json', "r") as f:
        animal = json.load(f)
        if animal_id in animal:
            if animal[animal_id]['ETAT'] != 'affamé':
                return ("Désolé, {animal_id} n'a pas faim!")

            elif Modèle.vérifie_disponibilité('mangeoire') == 'occupé' :
                occ = Modèle.cherche_occupant('mangeoire')
                return (f"Impossible, la mangeoire est actuellement occupée par {occ}")

            else:
                Modèle.change_lieu(animal_id, 'mangeoire')
                Modèle.change_état(animal_id,'repus')
    return None

def divertir(animal_id):
    with open('animal.json', "r") as f:
        animal = json.load(f)
        if animal_id in animal:
            if animal[animal_id]['ETAT'] != 'repus':
                return (f"Désolé, {animal_id} n'est pas en état de faire du sport!")

            elif Modèle.vérifie_disponibilité('roue') == 'occupé' :
                occ = Modèle.cherche_occupant('roue')
                return (f"Impossible, la roue est actuellement occupée par {occ}")

            else:
                Modèle.change_lieu(animal_id, 'roue')
                Modèle.change_état(animal_id,'fatigué')
    return None

def coucher(animal_id):
    with open('animal.json', "r") as x:
        animal = json.load(x)
        if animal_id in animal:
            if animal[animal_id]['ETAT'] != 'fatigué':
                return ("Désolé, {animal_id} n'est pas fatigué!")

            elif Modèle.vérifie_disponibilité('nid') == 'occupé' :
                occ = Modèle.cherche_occupant('nid')
                return (f"Impossible, le nid est actuellement occupée par {occ}")

            else:
                Modèle.change_lieu(animal_id, 'nid')
                Modèle.change_état(animal_id,'endormi')
    return None

def reveiller(animal_id):
    with open('animal.json', "r") as x:
        animal = json.load(x)
        if animal_id in animal:
            if animal[animal_id]['ETAT'] != 'endormi':
                return f'''Désolé, {animal_id} n'est dort pas!'''
            else:
                Modèle.change_lieu(animal_id, 'litière')
                Modèle.change_état(animal_id,'affamé')
    return None