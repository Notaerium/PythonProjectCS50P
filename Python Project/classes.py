class Muggle:
    def __init__(self, name, profession, age=20, home=""):
        self.age = age
        self.home = home
        self.name = name
        self.profession = profession

    def introduction(self):
        return f"{self.name}: My name is {self.name} and I work here. I ain't seeing anything strange though."
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age < 11:
            raise ValueError("Too young to be at Hogwarts")
        if age > 150:
            raise ValueError("In't it too old to be anything but a ghost?")
        self._age = age

    @property
    def home(self):
        return self._home
    
    @home.setter
    def home(self, home):
        self._home = home

    @property
    def profession(self):
        return self._profession
    
    @profession.setter
    def profession(self, profession):
        if not profession:
            raise ValueError("Missing Profession")
        self._profession = profession

class Wizard(Muggle):
    def __init__(self, name, profession, age=20, home="", wand =""):
        super().__init__(name, profession, age, home)
        self.wand = wand

    def introduction(self):
        return f"{self.name}: I am pleased to be part of Hogwarts, it sure change from {self.home}."

    def __str__(self):
        return f"{self.name}: Magic is fun, even when you are {self.age} years old."

    @property
    def wand(self):
        return self._wand
    
    @wand.setter
    def wand(self, wand):
        self._wand = wand

    def gandalf(self):
        return "A wizard is never late, nor is he early. He arrives precisely when he means to."

class Student(Wizard):
    def __init__(self, name, profession, age=20, home="", wand ="", house = "Gryffindor"):
        super().__init__(name, profession, age, home, wand)
        self.house = house

    def introduction(self):
        return f"{self.name}: Eager to learn with my friends from {self.house}!"
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("Unknown house")
        self._house = house

class Professor(Wizard):
    def __init__(self, name, profession, age=20, home="", wand ="", subject = ""):
        super().__init__(name, profession, age, home, wand)
        self.subject = subject
    
    def introduction(self):
        return f"{self.name}: Pleased to teach you {self.subject} this year."

    @property
    def subject(self):
        return self._subject
    
    @subject.setter
    def subject(self, subject):
        self._subject = subject

    def yell(self):
        return (f"My name is {self.name} and I will be your {self.subject} {self.profession} this year! Go to your sit and quiet now!")

class Ghost(Muggle):
    def __init__(self, name, profession,  age=20, home=""):
        super().__init__(name, profession, age, home)
        self.age = age

    def introduction(self):
        return f"Booooooooooh, Oh! You know me ? I'm {self.name}, although it was not my name when I was still alive."

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Even a ghost can't have a negative age!")
        self._age = age

class Wand:
    def __init__(self, wood, length, core):
        self.wood = wood
        self.length = length
        self.core = core

    @property
    def wood(self):
        return self._wood
    
    @wood.setter
    def wood(self, wood):
        self._wood = wood

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, length):
        self._length = length

    @property
    def core(self):
        return self._core
    
    @core.setter
    def core(self, core):
        self._core = core


