def leap(year):
   # year = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                year = True
            else:
                year = False
        else:
            year = True

        return year


x = leap(2023)

print(x)
