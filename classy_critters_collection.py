from datetime import date

class Donkey: 
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()


class Llama:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Snake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Fish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        

jack = Donkey('Jack', 'Irish')
tina = Llama('Tina', 'Llama')
bruce = Snake('Bruce', 'Copperhead')
gigi = Fish('Gigi', 'Clown')