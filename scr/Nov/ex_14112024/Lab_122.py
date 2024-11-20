class Son:
    gold = "1kg"

class Father(Son):
    diamond = "22karat"

class GrandFather(Father):
    btc = "1btc"

gf  = GrandFather()
print(gf.gold)
s=Son()
#print(s.diamond)