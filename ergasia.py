def menu():
    print("1. Make espresso")
    print("2. Make latte")
    print("3. Make cappuccino")
    print("4. Report materials type R")

def logoff():
    quit()

def report(materials):
    materialsLength = len(materials)
    for i in range(0,materialsLength-1,2):
        print(materials[i], materials[i+1],"\n")

def materialsCheck(materials,water,milk,coffee,money,choice,var):
    materialsLength = len(materials)
    if (materials[1]-water < 0) or (materials[3]-milk < 0) or (materials[5]-coffee < 0) or (materials[7]-money < 0) :
        print ("There is no enough resources to make coffee ")
        print()

        if materials[1] < water:
            print("Unfortunately there is not enough water ")
            print()
            var = True

        if materials[3] < milk:
            print("Unfortunately there is not enough milk ")
            print()
            var = True

        if materials[5] < coffee:
            print("Unfortunately there is not enough coffee ")
            print()
            var = True


    else:
        materials[1] = materials[1]-water
        materials[3] = materials[3]-milk
        materials[5] = materials[5]-coffee
        
        if (choice == "1"):
            print("Make espresso")
            print()
            print('Here your espresso "\u2615"')
            print()
        elif (choice == "2"):
            print("Make latte")
            print()
            print('Here your latte "\u2615"')
            print()
        else:
            print("Make cappuccino")
            print()
            print('Here your cappuccino "\u2615"')
            print()
    return materials

def change(materials,coffee_money, money):
    materials[7] = materials[7]
    if money > coffee_money:
        if money-coffee_money != 0 :
            c = money - coffee_money
            print("Here your changes:")
            print(c)
            print()
            materials[7] = materials[7] + coffee_money
    elif (coffee_money == money):
        materials[7] = materials[7] + coffee_money
    else:
        print("You don't insert enough money. Try again!!!")
        print("The rest is:", coffee_money - money)
        while (money <= coffee_money):
            money = float(input("Please give me the money: "))
            print("The rest is:", coffee_money - money)




materials  =["Water", 300, "Milk", 200, "Coffee", 100, "Money", 50]
while(True):
    var = False
    print("What would you like to do?")
    menu()
    choice = input("Please type your coice:")
    if(choice == "1"):

        water = 50
        milk = 0
        coffee = 18
        coffee_money = 1.5
        money = float(input("Please give me the money: "))
        materialsCheck(materials,water,milk,coffee,money,choice,var)
        if var:
            change(materials, coffee_money, money)



    elif(choice == "2"):
        water = 200
        milk = 150
        coffee = 24
        coffee_money = 2.5
        money = float(input("Please give me the money: "))
        change(materials, coffee_money, money)
        materialsCheck(materials, water, milk, coffee, money,choice,var)
        if var:
            change(materials, coffee_money, money)



    elif(choice == "3"):
        water = 250
        milk = 100
        coffee = 24
        coffee_money = 3
        money = float(input("Please give me the money: "))
        materialsCheck(materials, water, milk, coffee, money, choice, var)
        if var:
            change(materials, coffee_money, money)



    elif(choice=="report" or choice=="R"):
        report(materials)
    else:
        if (choice== "off"):
            print("Exiting ...")
            print()
            logoff()