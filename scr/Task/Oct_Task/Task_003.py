class Customer:
    def __init__(self, name, account_no, amount):
        self.name = name
        self.account_no = account_no
        self.amount = amount

    def show(self):
        print(self.name)
        print(self.account_no)
        print(self.amount)
        print("______________________________________")

    def deposit(self, add):
        self.amount = self.amount + add

    def widthdraw(self, sub):
        self.amount = self.amount - sub

    def name_change(self,changed_name):
        self.name=changed_name


c1 = Customer("PIYUSH", 101, 1000)
c2 = Customer("Madhukar", 102, 2000)
c3 = Customer("Pushkar", 103, 3000)
c4= Customer("Rajiv",104,5000)
c5= Customer("Mohit",105,200000)
c1.show()
c2.show()
c3.show()
c4.show()
c5.show()
c1.deposit(50)
c2.widthdraw(100)
c3.deposit(500)
c5.widthdraw(100000)
c4.deposit(100000)
c1.name_change("Piyush Pandey")
c1.show()
c2.show()
c3.show()
c4.show()
c5.show()