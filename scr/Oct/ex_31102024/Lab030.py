#  Wap to find the max number between three numbers using nested if else
num1 = float(int(input("Enter your num1 ")))
num2 = float(int(input("Enter your num2 ")))
num3 = float(int(input("Enter your num3 ")))

if num1 > num2 and  num1 > num3:
    print("Max is ", num1)

elif num2 > num1 and  num2 > num3:

 print("Max is ", num2)
else:
  print("Max is ", num3)
