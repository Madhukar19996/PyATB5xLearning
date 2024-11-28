a = 10 # Global Variable


class Person:
    # b = 11  # Instance - Belong to class
    b =24

    def print_info(self):
        c = 20  # Local variable
        print(c)

        print(self.b)

        global a
        a = "Hello"
        

        print(a)


object_ref = Person()
object_ref.print_info()
print(a)

