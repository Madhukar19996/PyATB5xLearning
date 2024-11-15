side1 = int(input("your side1 is :"))
side2 = int(input("your side2 is :"))
side3 = int(input("your side3 is :"))

if side1 == side2 and side2 == side3:
    print(" All side of a triangle  is equal ")
    print("This is a equilateral triangle")

elif side1 == side2 or side1== side3 or side2== side3 :
    print("Two of the sides are equal")
    print("This is a isosceles triangle ")
else:
    print("All sides are different ")
    print(" This triangle is scelene ")
