class Calculator:

        """def __init__(self, x,y):
            self.x = x
            self.y = y"""
        
        def add(self, x, y):
            z = x+y
            return z

        def sub(self, x, y):
            if x > y:
               z = x - y 
               return z
            else:
               z = y - x
               return z
        def mult(self, x, y):
            z = x * y
            return z
        def div(self, x, y):
            z = x / y
            return z

#main
a = int(input("First:"))
symbol = input("Operation:")
b = int(input("Second:"))

c = Calculator()

if symbol == "+":
    print(c.add(a,b))
elif symbol == "-":
    print(c.sub(a,b))
elif symbol == "*":
    print(c.mul(a,b))
elif symbol == "/":
    print(c.div(a,b))
else:
    print ("Error")
