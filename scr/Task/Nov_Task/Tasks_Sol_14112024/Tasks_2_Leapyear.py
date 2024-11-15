#Leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400.

Leapyear=int(input("Enter your year :"))
if Leapyear%400==0 or Leapyear%4==0 and Leapyear%100!=0:
    print(" This is Leap Year :",Leapyear)
else:
    print("This is not Leap Year :",Leapyear)

