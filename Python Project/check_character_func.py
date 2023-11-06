import os
import csv

def check_characters_menu(filename):
    os.system('cls')
    print("Welcome to Hogwarts' library. Who are you looking for?")
    print("- Who is the character you are looking for? -")
    characters = []
    search = 0
    search_way = ["Name", "Age", "Profession", "Home", "House", "Subject"]
    print("I wan't to look for someone by :")

    while search not in search_way:
        for i in range(len(search_way)):
            print(f"{i+1}. {search_way[i]}") 
        search = input("? ").title().strip()
        if search in search_way:
            pass
        else:
            try:
                search = int(search)
                if search < 1 or search > 6:
                    raise ValueError()
                else:
                    search = search_way[int(search)-1]
            except ValueError:
                search = "error"
                os.system('cls')
                print("❌!! PLEASE SELECT ONE OF THE OPTIONS (1 to 6 or by typing the word) !!")

    keyword = input(f"{search}: ").strip().title()
    search = search.lower()
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, fieldnames=["name", "age", "profession", "home", "house", "subject", "wand"])
        for row in reader:
            if keyword == row[search]:
                characters.append({"name": row['name'], "age": row['age'], "profession": row['profession'], "home": row['home'],
                                "house": row['house'], "subject": row["subject"], "wand": row["wand"]})
    if len(characters) == 0:
        os.system('cls')
        print("❌!! Can't find this person in our list, please check the spelling !!")
    return characters
   
