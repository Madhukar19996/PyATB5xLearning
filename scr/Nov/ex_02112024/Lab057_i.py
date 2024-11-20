
# User Defined
# 1. The can't return -> non return
# 2.They can return something
# 3.They have parameters
# 4. They don't parameters / arguments
import math


# 1. The can't return -> non return
# No Return Type and No Parameter / Argument - NRNP
def greet():
    print("Hello")


greet()
# greet("Namaste")


# 2. # No Return Type and with Argument/ Param
#greet_by_name("Pramod")
#
#
# def say_hello_default_arg(name="Pushkar"):
#    print("Hello", name.upper())
#
# say_hello_default_arg("madhukar")
# say_hello_default_arg("piyush")
# say_hello_default_arg()
#
#
# # 3. No Return Type and with Default Argument ( # positional argument)
# def greet_by_name(name):
#     print("Hello,", name)
#
#
# say_hello_default_arg("Pandey")
# say_hello_default_arg()
#
#
# def multiple_args(name1="A", name2="B"):
#     print("Mul -> ", name1, name2)
#
#
# multiple_args()
# multiple_args("Lucky", "Sharma")
# multiple_args(name1="Madhukar")
# multiple_args(name1="Pushkar", name2="Amit")
# multiple_args(name2="Piyush")
# #
#
#
#
# # 4. Argument + return Type
#
#
def sum_of_two(a, b):
    return  a + b


r = sum_of_two(4, 56)
print(r)


def sum_of_two_number_with_default(num1=100, num2=200):
    print("I will sum the two numbers!")
    return num1 + num2

result = sum_of_two_number_with_default(num1=34, num2=34)
print(result)
result = sum_of_two_number_with_default()
print(result)
# //