import json

def lit_état(animal_id):
    with open('animal.json',"r") as x:
        animal = json.load(x)
        if animal_id in animal:
            return animal[animal_id]["ETAT"]
        else:
            print(f"Désolé, {animal_id} n'est pas un animal connu")
            return None

def lit_lieu(animal_id):
    with open('animal.json',"r") as x:
        animal = json.load(x)
        if animal_id in animal:
            return animal[animal_id]["LIEU"]
        else:
            return None

def lit_race(animal_id):
    with open('animal.json',"r") as x:
        animal = json.load(x)
        if animal_id in animal:
            return animal[animal_id]["RACE"]
        else:
            return None

def vérifie_disponibilité(équipement_id):
    with open('équipement.json',"r") as x:
        équipement = json.load(x)
        if équipement_id in équipement:
            return équipement[équipement_id]["DISPONIBILITÉ"]
        else:
            print(f"Désolé, {équipement_id} n'est pas un équipement connu")
            return None

def cherche_occupant(lieu):
    occupants = []
    with open('animal.json',"r") as x:
        animal = json.load(x)
        for animal_id in animal:
            if animal[animal_id]["LIEU"] == lieu:
                occupants.append(animal_id)
        if occupants:
            return occupants
        else:
            return None


def change_état(id_animal, état):
    etats_possibles = ["affamé","fatigué","repus","endormi"]
    with open('animal.json',"r") as x:
        animal = json.load(x)
        if id_animal in animal and état in etats_possibles:
            animal[id_animal]["ETAT"] = état
        else:
            print(f"L'état n'est pas accepté.")
            return None
    json.dump(animal, open("animal.json", "w"), indent=4)

def change_lieu(id_animal, lieu):
    with open('équipement.json','r') as y:
        with open('animal.json','r') as z:
            équipement = json.load(y)
            animal = json.load(z)
            if id_animal in animal and lieu in équipement:
                anc_lieu = str(lit_lieu(id_animal))
                if vérifie_disponibilité(lieu) == 'occupé':
                    print(f'Désolé, le lieu {lieu} est déjà occupé')
                elif lieu != 'litière':
                    équipement[lieu]["DISPONIBILITÉ"] = 'occupé'
                    animal[id_animal]["LIEU"] = lieu
                    équipement[anc_lieu]["DISPONIBILITÉ"] = 'libre'
                elif lieu == 'litière':
                    équipement[anc_lieu]["DISPONIBILITÉ"] = 'libre'
                    animal[id_animal]["LIEU"] = lieu
            else:
                return None
        json.dump(animal, open("animal.json", "w"), indent=4)
    json.dump(équipement, open("équipement.json", "w"), indent=4)