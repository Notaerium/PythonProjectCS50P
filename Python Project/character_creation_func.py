from classes import Muggle, Ghost, Student, Professor, Wizard, Wand
import os

def creation_menu():
    """
    Prompt the user to create a character working at Hogwarts.

    :return: a tuple of the character and it's wand. If the character doesn't have a wand, return an empy string instead
    :rtype: Muggle() or Wizard() or Student() or Professor() and it's Wand()
    """
    classChoice = ["Director", "Professor", "Student", "Ghost", "Caretaker", "Muggle"]
    choice = 0
    print("Welcome to Hogwarts, please fill in this form :")
    while choice not in classChoice:
        print("-Character creation-")
        print("Do you want to create a:")
        for i in range(len(classChoice)):
            print(f"{i+1}. {classChoice[i]}")
        choice = input("? ")
        if choice not in classChoice:
            try:
                choice = int(choice)
                if choice < 1 or choice > 6:
                    raise ValueError()
                else:
                    choice = classChoice[choice-1]
            except ValueError:
                choice = 0
                os.system('cls')
                print("❌!! PLEASE SELECT ONE OF THE OPTIONS (1 to 6 or by typing the name of the profession) !!")

    name = input(f"What is the name of this {choice}? ").strip().title()

    character = class_create(name, choice)

    error = True
    while error:
        try:
            error = False
            character.age = int(input("How old is this person? "))
        except ValueError:
            print("❌ Age not believable")
            error = True
            pass
    character.home = input("Where does this person live outside of the school? ").strip()
    if isinstance(character, Wizard):
        has_a_wand = input("Does this wizard have a wand? (y/n) ").lower().strip()
        if has_a_wand == "y" or has_a_wand == "yes":
            character.wand = wand_creation_menu()
    if isinstance(character, Student):
        error = True
        while error:
            try:
                error = False
                character.house = input("In which house is the student? ")
            except ValueError:
                print("❌ House doesn't exist")
                error = True
                pass
    if isinstance(character, Professor):
        character.subject = input("What does this professor teach? ")

    if hasattr(character, 'wand') :       
        return character, character.wand
    else:
        return character, ""

def class_create(name, role):
    match role:
        case "Director":
            choosed = Wizard(name, profession = role)
        case "Professor":
            choosed = Professor(name, profession = role)
        case "Student":
            choosed = Student(name, profession =  role)
        case "Ghost":
            choosed = Ghost(name, profession =  role)
        case "Caretaker" | "Muggle" :
            choosed = Muggle(name, profession =  role)
        case _:
            raise ValueError("❌ This profession is not covered")
    
    return choosed


def wand_creation_menu():
    """
    Prompt the user to create a wand object from it's wood, core and length.

    :return: an object of class Wand()
    :rtype: Wand()
    """
    woodChoice = [
        "acacia", "alder", "apple", "ash", "aspen", "beech", "blackthorn", "black walnut", "cedar", "cherry", "chestnut", "cypress", "dogwood",
        "ebony", "elder", "elm", "english oak", "fir", "hawthorn", "hazel", "holly", "hornbeam", "larch", "laurel", "maple", "pear", "pine",
        "poplar", "red oak", "redwood", "rowan", "silver lime", "spruce", "sycamore", "vine", "walnut", "willow", "yew" 
            ]
    coreChoice = [
        "dragon heartstring", "phoenix feather", "unicorn tail hair", "veela hair", "thestral tail hair", "troll whisker", "coral", 
        "dittany stalk", "thunderbird tail feather", "wampus cat hair", "white river monster spine", "rougarou hair", "horned serpent horn",
        "snallygaster heartstring", "jackalope antler", "kneazle whisker", "kelpie hair", "basilisk horn", "curupira hair", "african mermaid hair",
        "fairy wing"
    ]
    wood = ""
    core = ""
    length = 0
    while wood not in woodChoice:
        wood = input("Which wood the wand is made of? ").lower().strip()
        if wood not in woodChoice:
            print(f"❌!!! Can't find '{wood}' in the wood database !!!")
    while core not in coreChoice:
        core = input("Which core the wand is made of from? ").lower().strip()
        if core not in coreChoice:
            print(f"❌!!! Can't find '{core}' in the core database !!!")
    while length < 8 or length > 16:
        try:
            length = float(input("What size is the wand in inches ? (just type the number)"))
        except ValueError:
            print("❌!!! Please enter a number !!!")
        if length < 8 or length > 16:
            print(f"❌!!! No wand smaller than 8 or bigger than 16 inches !!!")

    wand = Wand(wood, length, core)
    return wand
