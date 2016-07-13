class Animal:

    def __init__(self, name, species):
        self.species = species
        self. name = name

class Species:
    def __init__(self):
        self.common_name = ""
        self.geo_region = ""

class BettaTrifasciata(Species):
    def __init__(self, color):
        self.color = color
        self.common_name = "Betta fish"

class Betta(Animal):
    def __init__(self, color, name):
        Animal.__init__(self, name, BettaTrifasciata(color)) # calls constructor function for Animal

class Habitat:
    def __init__(self):
        self.name = ""
        self.members = set()

    def add_member(self, member):
        self.members.add(member)

    def remove_member(self, member):
        self.members.remove(member)

class Aquarium(Habitat):
    def __init__(self, water_type):
        Habitat.__init__(self)
        self.water_type = water_type

class Walking:
    def __init__(self):
        self.legs = 0
        self.walk_speed = 0
        self.legs = 0

class Flying:
    def __init__(self):
        self.air_speed = 0
        self.wings = 0
        self.wing_span = 0

class Swimming:
    def __init__(self):
        self.swim_speed = 0
        self.fins = False
        self.flippers = False
        self.web_feet = False
