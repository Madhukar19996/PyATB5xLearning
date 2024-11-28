class Person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return self.name


mp = Person("Madhukar")
pp = Person("Pushkar")

print(mp.name)
print(pp.name)

print("Who is walking", mp.walk())
print("Who is walking", pp.walk())