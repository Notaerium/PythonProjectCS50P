# Hogwarts' Logbook

    #### Video Demo:  https://youtu.be/0CahIgOYKMw
    #### Description:
    Hello everyone, I am Vinh from France and here is my final project for the CS50P class.
    It is a reather small project, but I tried to use a lot of things seen during class. I focused on the OOP part of programming as it seems to be something really useful in the job market, even more while using frameworks.

    In this application, the user will be able to fill in a database (not really here, just a csv) with the details of Hogwarts' workers and students. It is very similar to the lesson on OOP but a bit more advanced. Depending on which type of character you would like to put in the record, the questions may vary a little bit. For example, the user will be asked the teaching subject of teachers, or the house of students.
    It won't ask if the person has a wand if it is not considered a magic being.

    **!!! Note that there might be some inacuracy**, I am not a Harry Potter expert, even though I really liked the movies and watched them several times. The inacuracies might be because of my lack of knowledge on the Harry Potter world, or for the sake of simplyfying the code.
    For instance, I first wanted to use regex for the name and home of a character, but while making the tests, it was easier for me to not respect any convention. Also, as the user can imagine any new character, it is possible to create someone with a name or a home not based on English rules.

    As some of the functions and classes were long, I decided to split them in different files. The application allowing to make an entry in the record OR checking the entries, I decided to split the functions as such in two different files named "character_creation_func.py" and "check_character_func.py".
    In the **character_creation_func.py**:
    There is three functions: creation_menu(), class_create() and wand_creation_menu().
        _The first function is what's prompting the user for details concerning the character being created, it returns both the character and its wand, the wand being an object by itself.
        _The second function is only here to create the object of the character depending on its profession. A certain profession is instanciating a certain class!
        _The third function is the one that create the wand of the character. I had trouble with attributing an object to another object, as when I was calling character.wand, has we've sawn during class, the result value is something that look like "<classes.Wand object at 0x000001D308904C80>", and not a clear description of the wand's attributes. That is why the first function need to return the wand object as well, so that I can read into it and writing the wand attributes in the csv more properly.
    In the **check_character_func.py**:
    There is only one function "check_characters_menu" that prompts the user a keyword. For example, if the user is looking for a specific character, it is possible to search by name. But it the user is looking for everyone in Gryffindor for example, it is possible to search by house. The function returns in an array all entries that match the keyword.
    In the classes.py:
    There are six different **classes**.
        _The **Muggle** class is just the basic information on the character (the name, age, home and profession)
        _The **Wizard** is extended from the Muggle class as they also have these attributes, but can have a wand.
        _The **Professor** is extended from the Wizard class and have a subject
        _The **Student** is also extended from the Wizard but have a house
        _The **Ghost** is extended from the Muggle for the sole reason that there is a protection on the character age (someone can't be too old), and this protection is lifted with the Ghost.
        _The **Wand** is its own class with three attributes : the wood and the core used and its length.

    The **project.py** file is here to show the results of the two other functions files, either if the recording was successful or with the results from the inquieries. The filename was placed in a variable in the main function, so that if change is needed, it is easier to access and modify.
    Each class has its own functions, either being its introduction as a character, or other kind of sentences. They actually aren't very useful but it was really helpful when testing the instanciation of each class.

    The other challenge, beside the OOP, was writing in the csv. I had some trouble with it as first, I wanted the program to be able to create a .csv with its headers. So I had to import the os library so that I could check if the file was existing or not, and if it is not, the headers will be writen on the first line. If the file already exists, then the program shall write the character's details directly. If I didn't check for it, the headers would be writtent every time between each entry. As the os library was now imported, I also decided to clean the command window for few occasions, as it would get a bit messy to understand what's happening with every step at the screen. Overall, this program is not really user friendly, but it is working fine. When prompted to make a choice, most of the time, the user can either write the choice or just select its number and the result will be the same.

    The test_project.py is testing the instanciation of the classes and if they work how they are supposed to work. It is also checking if the functions return simple sentences (customized by the character created) are correct, to check that everything went well in the process.

    Thanks for your time, for Professor David J. Malan the team in charge of the CS50P course.
