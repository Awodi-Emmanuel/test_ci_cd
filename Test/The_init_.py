# Declear a class name Person
class Person:

    # The init or The contructor
    def __init__(self, name):
        self.myname = name

    # Method to call for greetings
    def say_hi(self):
        print('Hi, my name is {}'.format(self.myname))

# Instantiate your object
p = Person('Jonnel')
p.say_hi()