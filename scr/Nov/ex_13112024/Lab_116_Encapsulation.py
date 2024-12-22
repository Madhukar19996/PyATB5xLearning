# Encapsulation -
# Hide the data members(class variables, instance variables)
# by using only the methods.

class Car:
    def __init__(self):
        self.password = "Madhukar" # public instance variable
        self.__password_secure = "pass123" # private instance variable

    def change_password(self):
        self.password_secure = "madhukar123"
        self.__password_secure = "pass123"



object_ref = Car()
print(object_ref.password)
object_ref.change_password()
print(object_ref.password_secure)
print(object_ref.change_password())
# print(object_ref.__password_secure) # 'Car' object has no attribute '__password_secure'