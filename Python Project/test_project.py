from project import main_menu, write_record, catchphrase
from character_creation_func import class_create
from classes import Wizard, Ghost, Student, Professor, Wand, Muggle
import pytest

def main():
    test_main_menu()
    test_init()
    test_class_create()
    test_wizard_class()
    test_professor_class()
    test_write_record()
    test_catchphrase()

def test_main_menu():
    assert main_menu("1") == 1
    assert main_menu("") == 1
    assert main_menu("2") == 2


def test_init():
    harry_wand = Wand("holly", "phoenix feather", 11)
    severus = Professor("Severus Snape", "Professor", 38, "Spinner's End", " ", "Defense Against Dark Arts")
    assert severus.name == "Severus Snape"
    assert severus.profession == "Professor"
    assert severus.age == 38

    albus = Wizard("Albus Dumbledore", "Director", 115, "Mold on the wold", " ")
    assert albus.name == "Albus Dumbledore"

    harry = Student("Harry Potter", "Student", 18, "Godric's Hollow", harry_wand , "Gryffindor")
    assert harry.profession == "Student"
    assert harry.house == "Gryffindor"

    nick = Ghost("Nearly Headless Nick", "Ghost", 540, "Gryffindor quarter")
    with pytest.raises(ValueError):
        ron_wand = Wand(10, "unicorn tail hair", 12)
        ron_wand = Wand("The wood from this tree over here", "unicorn tail hair", 12)
        ron_wand = Wand("willow", "unicorn tail hair", 18)
        ron = Student("Ron Weasley", "Student", 5, "Ottery St Catchpole", Wand("willow", "unicorn tail hair", 14), "Gryffindor")
        ron = Student("Ron Weasley", "Student", 540, "Ottery St Catchpole", Wand("willow", "unicorn tail hair", 14), "Gryffindor")
        ron = Student("Ron Weasley", "Student", 18, "Ottery St Catchpole", Wand("willow", "unicorn tail hair", 14), "This House over there")

def test_class_create():
    with pytest.raises(ValueError):
        class_create("Severus", "Death Eater")

def test_wizard_class():
    albus = Wizard("Albus Dumbledore", "Director", 115, "Mold on the wold", " ")
    harry = Student("Harry Potter", "Student", 18, "Godric's Hollow", " ", "Gryffindor")
    severus = Professor("Severus Snape", "Professor", 38, "Spinner's End", " ", "Defense Against Dark Arts")
    nick = Ghost("Nearly Headless Nick", "Ghost", 540, "Gryffindor quarter")
    assert severus.gandalf() == "A wizard is never late, nor is he early. He arrives precisely when he means to."
    assert harry.gandalf() == "A wizard is never late, nor is he early. He arrives precisely when he means to."
    assert albus.gandalf() == "A wizard is never late, nor is he early. He arrives precisely when he means to."
    with pytest.raises(AttributeError):
        nick.gandalf()

def test_professor_class():
    albus = Wizard("Albus Dumbledore", "Director", 115, "Mold on the wold", " ")
    harry = Student("Harry Potter", "Student", 18, "Godric's Hollow", " ", "Gryffindor")
    severus = Professor("Severus Snape", "Professor", 38, "Spinner's End", " ", "Defense Against Dark Arts")
    nick = Ghost("Nearly Headless Nick", "Ghost", 540, "Gryffindor quarter")
    assert severus.yell() == "My name is Severus Snape and I will be your Defense Against Dark Arts Professor this year! Go to your sit and quiet now!"
    with pytest.raises(AttributeError):
        albus.yell()
        harry.yell()
        nick.yell()

def test_write_record():
    harry = Student("Harry Potter", "Student", 18, "Godric's Hollow", Wand("holly", "phoenix feather", 11), "Gryffindor")
    assert write_record("test.csv", harry, harry.wand) == f"✅ Student Harry Potter has been added in 'test.csv'"
    harry.name = "Harry"
    assert write_record("test.csv", harry, harry.wand) == f"✅ Student Harry has been added in 'test.csv'"

def test_catchphrase():
    harry = Student("Harry Potter", "Student", 18, "Godric's Hollow", Wand("holly", "phoenix feather", 11), "Gryffindor")
    assert catchphrase(harry) == "Harry Potter: Eager to learn with my friends from Gryffindor!"
    severus = Professor("Severus Snape", "Professor", 38, "Spinner's End", " ", "Defense Against Dark Arts")
    assert catchphrase(severus) == "Severus Snape: Pleased to teach you Defense Against Dark Arts this year."

if __name__ == "__main__":
    main()