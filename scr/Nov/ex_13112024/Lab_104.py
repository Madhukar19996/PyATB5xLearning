class Cat: # class Name will always start from the Capital letter
    # A
    name = None
    breed = None
    color = None

    # B
    def sleep(self):
        print("Sleeping")

    def run(self):
        print("running")

    def eat(self,food):
        print(food)


c1= Cat()
print(c1.name)
c1.name = "Tom"
print(c1.name)
c1.sleep()
c1.run()
c1.color="blue"
print(c1.color)

c1.eat("fish")

print(" ---- -----------------")


c2 = Cat()
print(c2.name)
c2.name = "Keyo"
print(c2.name)
c2.eat("egg")

# c3 = c1