from classes import Student, Professor, Wizard, Muggle, Ghost
from character_creation_func import creation_menu
from check_character_func import check_characters_menu
import os
import csv

#Create a customized character attending/working at hogwart
#adding the created character to a DB (here a csv file) and reading their introduction
#allow to check entries using keywords

def main():
    filename = "character.csv"
    selection = 0
    while selection != 1 and selection != 2:
        print("--What would you like to do?--")
        print("1. Check character list \n2. Create a new character \n(type 1 or 2, default = 1) : ", end="")
        selection = main_menu(input(""))
    if selection == 2:
        character, wand = creation_menu()
        #If a wand object is returned and not just an empty string
        if hasattr(wand, 'wood'):
            wand = f"{wand.wood, wand.core, wand.length}"
        #If the file doesn't exist yet, then the program should write the header, else it should proceed with the character details
        if not os.path.isfile(filename):
            with open(filename, 'w', newline='') as my_file:
                writer = csv.DictWriter(my_file, fieldnames= ["name", "age", "profession", "home", "house", "subject", "wand"])
                writer.writeheader()
        print(write_record(filename, character, wand))
        print(catchphrase(character))
    elif selection == 1:
        entries = check_characters_menu(filename)
        for entry in entries:
            print(entry)


def catchphrase(character):
    return character.introduction()

def write_record(filename, character, wand):
    with open(filename,  'a') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "age", "profession", "home", "house", "subject", "wand"], lineterminator = '\n')
            if isinstance(character, Professor):
                writer.writerow({"name": character.name, "age": character.age, "profession": character.profession, "home": character.home,
                                 "house": " ", "subject": character.subject, "wand" : wand
                                })
            elif isinstance(character, Student):
                writer.writerow({"name": character.name, "age": character.age, "profession": character.profession, "home": character.home,
                                 "house": character.house, "subject": " ", "wand" : wand
                                })
            elif isinstance(character, Wizard):
                writer.writerow({"name": character.name, "age": character.age, "profession": character.profession, "home": character.home,
                                 "house": " ", "subject": " ", "wand" : wand
                                })
            elif isinstance(character, Muggle) or isinstance(character, Ghost):
                writer.writerow({"name": character.name, "age": character.age, "profession": character.profession, "home": character.home})

    return f"✅ {character.profession} {character.name} has been added in '{file.name}'"


def main_menu(str):
    match str:
        case "1" | "":
            return 1
        case "2":
            return 2
        case _:
            os.system('cls')
            print("❌!! PLEASE SELECT ONE OF THE OPTIONS (1 or 2) !!")
    



if __name__ == "__main__":
    main()