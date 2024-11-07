# WAP to calculate the grade of a student from his marks from the following scheme:
# 90-100 --> Excellent
# 80-90 --> A
# 70-80 --> B
# 60-70 --> C
# 50-60 --> D
# <50 --> F

# marks = int(input("Enter your marks: "))
# if marks >= 90 and marks <= 100:
#     print("Excellent")
# elif marks >= 80 and marks < 90:
#     print("A")
# elif marks >= 70 and marks < 80:
#     print("B")
# elif marks >= 60 and marks < 70:
#     print("C")
# elif marks >= 50 and marks < 60:
#     print("D")
# elif marks < 50:
#     print("F")
# else:
#     print("Invalid input")
score=float((input(" Enter your marks ")))
if score>=90 and score<=100:
    print("Excellent")
    print("Your grade is  Excellent", score)
elif score>=80 and score<90:
    print("A")
    print("Your grade is A", score)
elif score>=70 and score<=80:
    print("B")
    print("Your grade is B", score)
elif score>=60 and score<70:
    print("C")
    print("Your grade is C", score)
elif score >=50 and score <=60:
    print("D")
    print("Your grade is D", score)

else :

    print("Your grade is F", score)
    print("You are fail, Try again next year")