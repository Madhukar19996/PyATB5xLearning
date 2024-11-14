class Employee:

    def __init__(self,name , age, phone_id,address,emp_id):
        self.name=name
        self.age=age
        self.phone_id=phone_id
        self.address=address
        self.emp_id=emp_id

    def walk (self ):
        print( " is walking ")
        print("_____________________")

    def talk (self, name):
        print(self.name, " is talking  ")
        print("_____________________")

    def show (self) :
        print(self.name)
        print(self.age)
        print(self.phone_id)
        print(self.address)
        print(self.emp_id)
        print("_____________________")


name=input(" Enter User name ")
age=input(" Enter User age ")
phone_id=input(" Enter User phone_id ")
address=input(" Enter User address ")
emp_id=input(" Enter User emp_id ")
print("_____________________")

E1=Employee(name,age,phone_id,address,emp_id)

name1=input(" Enter User name ")
age1=input(" Enter User age ")
phone_id1=input(" Enter User phone_id ")
address1=input(" Enter User address ")
emp_id1=input(" Enter User emp_id ")
print("_____________________")

E2=Employee(name1,age1,phone_id1,address1,emp_id1)

E1.show()
E1.walk()
E1.talk(name)

E2.show()
E2.walk()
E2.talk(name)








