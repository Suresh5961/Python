# Multi level inheritence

class bank:
    def name(self):
        print("axis bank")

class bank1(bank):
    def name1(self):
        print("hdfc bank")

class bank2(bank1):
    def name2(self):
        print("sbi bank")

A=bank2()
A.name()
A.name1()
A.name2()