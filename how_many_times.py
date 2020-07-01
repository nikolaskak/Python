'''Read a few numbers until the input is equal with -1
and found how many dublicates exist in your list!'''

def dublicates(l):
    sum = 0
    length = len(l)
    for i in range(length):
        for j in range(length):
            if i == j:
                sum = sum + 1
    print("There are ", int(sum/2), "dublicates!")

myList = []
elements = int(input("Give a number: \t"))
while elements != -1:
    myList.append(elements)
    elements = int(input("Give a number: \t"))

dublicates(myList)
