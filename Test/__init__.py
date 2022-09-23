class Person:
    def __init__(self, name, age):
        self.myname = name
        self.myage = age
        
    def sayMyAge(self):
        return "My name is {} and I am {} years old".format(self.myname, self.myage)
        

p1 = Person("Isaac", 25)

print(p1.sayMyAge())