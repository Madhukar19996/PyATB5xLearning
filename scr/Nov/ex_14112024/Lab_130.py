class Calc:

    def __int__(self):

        print("DC")



    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


obj_ref = Calc()

# a = int(input("Enter the value a"))

# b = int(input("Enter the value b"))

output_sum = obj_ref.sum(4, 6)
print(output_sum)

output_sub = obj_ref.sub(8,3)
print(output_sub)

output_mul = obj_ref.mul(7,9)
print(output_mul)


output_div = obj_ref.div(15,5)
print(output_div)