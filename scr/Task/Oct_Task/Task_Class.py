class Student:

    def __init__(self,name , age, roll):
        self.name =name
        self.age=age
        self.roll=roll

    def show (self):
     print(self.name)
     print(self.age)
     print(self.roll)
     print("__________________")


s=Student("Madhukar", 24,16678)
s1=Student('Mohit',23,3345)
s2=Student("Rohit", 25,2242)
s.show()
s1.show()
s2.show()
print(s1)
print(s2)

