class Fanicial_App:
    rate=15
    def __init__(self,name , pri, time  ):
        self.name=name
        self.pri=pri
        #self.rate=rate
        self.time=time

    def greet (self):
        print(self.name," Good Morning Sir")
        print("___________________________________")



    def sim_ins (self):
        si= (self.pri*self.rate*self.time)/100
        print(" Your Simple Intrest is :", si)
        print("___________________________________")

e1=Fanicial_App('Madhukar',100,5)
e1.greet()
e1.sim_ins()

e2=Fanicial_App('Piyush',200,7)
e2.greet()
e2.sim_ins()




