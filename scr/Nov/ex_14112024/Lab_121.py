# Multilevel Inheritance

class GrandFather:
    gold = "2kg"

    def bhk1(self):
        print("1BHK")


class Father(GrandFather):
    diamond = "22 karat"

    def bhk2(self):
        print("2BHK")


class Son(Father):
    btc = "1BTC"

    def bhk3(self):
        print("3BHK")


s = Son()
print(s.gold)
s.bhk1()
s.bhk2()
s.bhk3()
f = Father()
f.bhk1()

gf = GrandFather()