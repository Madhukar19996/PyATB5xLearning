from abc import ABC, abstractmethod

class PC:
    def __init__(self):
        print("Start PC ")

class Ram:
    @abstractmethod
    def rm(self):
        pass

class Storage:
    @abstractmethod
    def strg(self):
        pass

class  Display:
    @abstractmethod
    def dsp(self):
        pass

class Speaker:
    @abstractmethod
    def spr(self):
        pass


class DDR4(Ram):
    def rm  (self):
        print("I am installing DDR4 Ram in your system ")
        print(" DDR4 Loaded")


class Dobly (Speaker):
    def spr(self):
        print("I am installing Doblly Speaker in your system ")
        print(" Booting Sound ")

class Antigleyer(Display):
    def dsp(self):
        print("I am installing Antigleyer display in your system ")
        print(" Booting Display ")

class SSD(Storage) :
    def strg(self):
        print("I am installing SSD Storage  in your system ")
        print(" Booting Storage ")

class Samsung:
    @staticmethod
    def Logo():
        print("Samsung Logo")

    def Price(self,Mrp):
        self.Mrp=Mrp
        print("Your Personal Desktop price is --->",self.Mrp)




def System_On():
    pc_obj=PC()

    dis_obj=Antigleyer()
    print("==============")
    dis_obj.dsp()
    print("==============")
    Samsung.Logo()
    print("==============")
    dol=Dobly()
    print("==============")
    dol.spr()
    print("==============")
    ddr4=DDR4()
    print("==============")
    ddr4.rm()
    print("==============")
    ssd=SSD()
    print("==============")
    ssd.strg()
    print("==============")
    Sam=Samsung()
    print("===============")

    Sam.Price("48000")

System_On()








