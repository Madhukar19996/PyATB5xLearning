def grade(marks):
    marks=float(marks)
    if marks>=90:
        print("Topper A")

    elif marks>=80:
        print("Topper B")

    elif marks >= 70:
        print("Topper C")

    elif marks <= 50 and marks>= 33:
        print("Pass")

    elif marks < 33:
        print("Fail")

    else:
        print("error")


grade(52.6)