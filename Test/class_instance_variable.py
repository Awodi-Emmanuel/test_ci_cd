# Declear a class call Dog

class Dog:

    # Class Variable
    animal = 'dog'

    # The init method or contructor

    def __init__(self, breed, color):
        self.dogbreed = breed
        self.dogcolor = color

    
# Intantate Dog object
Rodger = Dog('pug', 'brown')
Buzo = Dog("Bulldog", 'black')
print(Rodger.animal)
    