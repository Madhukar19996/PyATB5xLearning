class PyATB5x:

    def __init__(self, name, age, qualification, gender, address,ph_no):
        self.name = name
        self.age = age
        self.qualification = qualification
        self.gender = gender
        self.address = address
        self.ph_no= ph_no


    def exercise(self):
        print( self.name," is doing exercise daily")

    def studying(self):
        print(self.name,"is studying minimum 3 hours daily")

    def sleep(self):
        print(self.name," is sleeping 8 hours daily")

    def show(self):
        print(self.name, end=" ")
        print( self.age , end=" ")
        print(self.qualification , end=" ")
        print(self.gender , end=" ")
        print(self.address , end=" ")
        print(self.ph_no, end=" ")

        print("\n-----------------------------------")




madhukar = PyATB5x("Madhukar","25","Bsc","male ","Noida","8937885560")

karan=PyATB5x("Karan","24","B.tech Ese","Male","Amritasr ","9134034568")

mushkan=PyATB5x("Mushkan","24","Bca ","Female","Rachi","9865467890")

ajay=PyATB5x("Ajay","26","BE","Male","Dhehradun","8517568760")

rani=PyATB5x("Rani","22","BscIT","Female","Patna","8976556790")

# print(madhukar.name)
#
# print(madhukar.qualification )
#
# print(rani.age)
# print(karan.address)
#
# madhukar.exercise()


def student_details():
    madhukar.show()
    karan.show()
    ajay.show()
    mushkan.show()
    rani.show()


student_details()
mushkan.studying()
madhukar.studying()



