print(" --- Start of the program --- ")
try:
    a = int(input("Ent the num1")) # ValueError: invalid literal for int()
    b = int(input("Ent the num2")) #  line 4, ValueError
    c = a / b # ZeroDivisionError: division by zero
    print("Result Div is ", c)
except Exception as e: # alias , Exception is what Class - multiple classes
    print(e)
    print("Please check your inputs, it shouldn't be a string or zero")


print(" --- End of the program ---")