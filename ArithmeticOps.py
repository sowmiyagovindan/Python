from decimal import Decimal

class ArithmeticOps():
    def add(self,a,b):
        ops = a+b
        print(ops)

    def subtract(self,a,b):
        ops = a-b
        print(ops)

    def multiply(self, a, b):
        ops = a*b
        print(format(ops,'.2f'))

    def divide(self, a, b):
        ops = a/b
        print(ops)

    def modulus(self, a, b):
        ops = a%b
        print(ops)

optn = ArithmeticOps()
optn.add(10,3)
optn.subtract(2,3)
optn.multiply(10,100)
optn.divide(1000,100)
optn.modulus(10,5)
