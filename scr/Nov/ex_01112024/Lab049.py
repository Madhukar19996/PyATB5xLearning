x=int(input("enter side 1: "))
y=int(input("enter side 2: "))
z=int(input("enter side 3: "))

if x==y and y==z and z==x:
    print("this is equaliteral triangle")

elif x==y or y==z or z==x:
    print("this is isolances triangle")

else:
    print("this is scalar triangle")

