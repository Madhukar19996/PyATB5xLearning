# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300

# Logic Building

# num1 = int(input("Enter the num1\n"))
# num2 = int(input("Enter the num2\n"))
# num3 = int(input("Enter the num3\n"))


def sum_three(n1=100, n2=200, n3=300):
    return n1+n2+n3


result= sum_three (n1=300,n2=200)



print(result)

# result2 = sum_three()
# result2 = sum_three(10)
# result2 = sum_three(10,20)
# result2 = sum_three(10,20,30)
print("_______________________________________________________________________________________________________")

def print_mul_arguments(*args):
    print(args)
    # # *args -> List
    # for i in args:
    #     print(i)


print_mul_arguments("Madhukar", "Pandey")
print_mul_arguments("Madhukar", "Pushkar", "Piyush")
print_mul_arguments("amit", 10, True, False, "Madhukar ")

#########################################################################################################
print("_______________________________________________________________________________________________________")
# Pizza Lovers

# Toppings -  mushroom, paneer, olives, corn, pineapple, jalapeno

def make_pizza(*toppings):
    print(toppings)
    # for i in toppings:
    #     print(i)

pramod = make_pizza("tomato","olives")
jayati = make_pizza("pineapple","olives","corn","paneer")
vinay = make_pizza("tomato")

r1 = max(1, 2, 3, 4, 6)
r2 = max(1, 2, 3)
r2 = max(2, 3)

