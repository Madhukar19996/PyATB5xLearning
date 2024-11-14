class Person:
    # Class Variables
    # Instance variables
    # name = "Surjit" # hardcoded value
    def __init__(self, name):
        self.name = name

    def walk(self):
        return self.name


p1 = Person("Sanju")
p2 = Person("Sallu")
print(p1.name)
print(p2.name)
print("Who is walking with the object sallu -> ", p2.walk())