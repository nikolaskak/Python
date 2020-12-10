class Calculator:

        """def __init__(self, x,y):
            self.x = x
            self.y = y"""
        def prosthesh(self, x, y):
            z = x+y
            return z

        def afairesh(self, x, y):
            print (x-y)
        def pollaplasiasmos(self, x, y):
            print (x*y)
        def diairesh(self, x, y):
            print (x/y)

#main
a = int(input("First:"))
symbol = input("Operation:")
b = int(input("Second:"))

c = Calculator()

if symbol == "+":
    print(c.prosthesh(a,b))
else:
    print ("Error")
