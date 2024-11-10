# Task 1 for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1
# from scr.Nov.ex_01112024.Lab054 import num_1
from math import remainder

num1=int(input("Enter your Divident : "))
num2=int(input("Enter your Divisor  : "))
rem=num1%num2
quotient=(num1-rem)/2
print(" Remaider:", rem)
print(" Quotient:", quotient )