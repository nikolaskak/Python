def menu():
    print("1. Make espresso")
    print("2. Make latte")
    print("3. Make cappuccino")
    print("4. Report materials type R")
    print("off")

def report(ylika):
    for i, j in ylika.items():
        print(i,":", j)

def elegxosYlikwn(ylika, nero, gala, kafes, xrhmata, epilogh, xr):
    if (epilogh == "1"):
        '''
        nero = int(espresso["Water"])
        gala = int(espresso["Milk"])
        kafes = int(espresso["Coffee"])
        kostos = float(espresso["Money"])
        '''
        nero = int(nero)
        gala = int(gala)
        kafes = int(kafes)
        kostos = float(xrhmata)
        xr = False

        if (int(ylika["Water"]) - nero < 0 ) or (int(ylika["Milk"]) - gala < 0 ) or (int(ylika["Coffee"]) - kafes < 0 ) or (int(ylika["Coffee"]) - kafes < 0 ):
            print("There is no enough resources to make coffee")
            print()
            if (int(ylika["Water"]) < nero):
                xr = True
                print("Unfortunately there is not enough water ")
                print()
            elif (int(ylika["Milk"]) < gala):
                xr = True
                print("Unfortunately there is not enough milk ")
                print()
            elif (int(ylika["Coffee"]) < kafes):
                xr = True
                print("Unfortunately there is not enough coffee ")
                print()

        else:
            ylika["Water"] = int(ylika["Water"]) - nero
            ylika["Milk"] = int(ylika["Milk"]) - gala
            ylika["Coffee"] = int(ylika["Coffee"]) - kafes

            print("Make espresso")
            print()
            print('Here your espresso "\u2615"')
            print()


    elif(epilogh == "2"):

        '''
        nero = int(espresso["Water"])
        gala = int(espresso["Milk"])
        kafes = int(espresso["Coffee"])
        kostos = float(espresso["Money"])
        '''
        nero = int(nero)
        gala = int(gala)
        kafes = int(kafes)
        kostos = float(xrhmata)

        if (int(ylika["Water"]) - nero < 0 ) or (int(ylika["Milk"]) - gala < 0 ) or (int(ylika["Coffee"]) - kafes < 0 ) or (int(ylika["Coffee"]) - kafes < 0 ):
            print("There is no enough resources to make coffee")
            print()
            if (int(ylika["Water"]) < nero):
                print("Unfortunately there is not enough water ")
                print()
            elif (int(ylika["Milk"]) < gala):
                print("Unfortunately there is not enough milk ")
                print()
            elif (int(ylika["Coffee"]) < kafes):
                print("Unfortunately there is not enough coffee ")
                print()
        else:
            ylika["Water"] = int(ylika["Water"]) - nero
            ylika["Milk"] = int(ylika["Milk"]) - gala
            ylika["Coffee"] = int(ylika["Coffee"]) - kafes

            print("Make latte")
            print()
            print('Here your latte "\u2615"')
            print()

    else:
        if (epilogh == "3"):
            '''
            nero = int(espresso["Water"])
            gala = int(espresso["Milk"])
            kafes = int(espresso["Coffee"])
            kostos = float(espresso["Money"])
            '''
            nero = int(nero)
            gala = int(gala)
            kafes = int(kafes)
            kostos = float(xrhmata)

            if (int(ylika["Water"]) - nero < 0) or (int(ylika["Milk"]) - gala < 0) or (
                    int(ylika["Coffee"]) - kafes < 0) or (int(ylika["Coffee"]) - kafes < 0):
                print("There is no enough resources to make coffee")
                print()
                if (int(ylika["Water"]) < nero):
                    print("Unfortunately there is not enough water ")
                    print()
                elif (int(ylika["Milk"]) < gala):
                    print("Unfortunately there is not enough milk ")
                    print()
                elif (int(ylika["Coffee"]) < kafes):
                    print("Unfortunately there is not enough coffee ")
                    print()
            else:
                ylika["Water"] = int(ylika["Water"]) - nero
                ylika["Milk"] = int(ylika["Milk"]) - gala
                ylika["Coffee"] = int(ylika["Coffee"]) - kafes

                print("Make cappuccino")
                print()
                print('Here your cappuccino "\u2615"')
                print()


def resta(ylika, cost, xrhmata, epilogh):
    if(epilogh == "1"):
        cost = espresso["Money"]
        cost = float(cost)
        if xrhmata > cost:
            if xrhmata - cost != 0:
                r = xrhmata - cost
                print("Here your changes:")
                print(r)
                print()
                y = float(ylika["Money"])
                y = y + cost
                ylika["Money"] = y
        elif (cost == xrhmata):
            y = float(ylika["Money"])
            y = y + cost
            ylika["Money"] = y

        else:
            print("You don't insert enough money. Try again!!!")
            print("The rest is:", cost - xrhmata)
            while (xrhmata <= cost):
                xrhmata = float(input("Please give me the money: "))
                print("The rest is:", cost - xrhmata)

    if (epilogh == "2"):
        cost = latte["Money"]
        cost = float(cost)
        if xrhmata > cost:
            if xrhmata - cost != 0:
                r = xrhmata - cost
                print("Here your changes:")
                print(r)
                print()
                y = float(ylika["Money"])
                y = y + cost
                ylika["Money"] = y
        elif (cost == xrhmata):
            y = float(ylika["Money"])
            y = y + cost
            ylika["Money"] = y

        else:
            print("You don't insert enough money. Try again!!!")
            print("The rest is:", cost - xrhmata)
            while (xrhmata <= cost):
                xrhmata = float(input("Please give me the money: "))
                print("The rest is:", cost - xrhmata)

    else:
        if (epilogh == "3"):
            cost = cappuccino["Money"]
            cost = float(cost)
            if xrhmata > cost:
                if xrhmata - cost != 0:
                    r = xrhmata - cost
                    print("Here your changes:")
                    print(r)
                    print()
                    y = float(ylika["Money"])
                    y = y + cost
                    ylika["Money"] = y
            elif (cost == xrhmata):
                y = float(ylika["Money"])
                y = y + cost
                ylika["Money"] = y

            else:
                print("You don't insert enough money. Try again!!!")
                print("The rest is:", cost - xrhmata)
                while (xrhmata <= cost):
                    xrhmata = float(input("Please give me the money: "))
                    print("The rest is:", cost - xrhmata)


ylika  = {"Water": 300,
              "Milk": 200,
              "Coffee": 100,
              "Money": 50
              }
espresso = {"Water": 50,
            "Milk": 0,
            "Coffee": 18,
            "Money": 1.5}

latte = {"Water": 200,
            "Milk": 150,
            "Coffee": 24,
            "Money": 2.5}

cappuccino = {"Water": 250,
            "Milk": 100,
            "Coffee": 24,
            "Money": 3}

while(True):
    xr = False
    print("What would you like to do?")
    menu()
    epilogh = input("Please type your coice:")
    print()
    if(epilogh == "1"):
        xrhmata = float(input("Please give me the money: "))
        elegxosYlikwn(ylika,espresso["Water"],espresso["Milk"],espresso["Coffee"],espresso["Money"],epilogh,xr)
        if (xr):
            resta(ylika, float(espresso["Money"]), xrhmata,epilogh)
        else:
            ylika["Money"] = ylika["Money"] - xrhmata



    elif(epilogh == "2"):
        xrhmata = float(input("Please give me the money: "))
        #change(materials, coffee_money, money)
        elegxosYlikwn(ylika,latte["Water"],latte["Milk"],latte["Coffee"],latte["Money"],epilogh,xr)
        if (xr):
            resta(ylika, float(latte["Money"]), xrhmata,epilogh)
        else:
            ylika["Money"] = ylika["Money"] - xrhmata


    elif(epilogh == "3"):
        xrhmata = float(input("Please give me the money: "))
        elegxosYlikwn(ylika,cappuccino["Water"],cappuccino["Milk"],cappuccino["Coffee"],cappuccino["Money"],epilogh,xr)
        if (xr):
            resta(ylika, float(cappuccino["Money"]), xrhmata, epilogh)
        else:
            ylika["Money"] = ylika["Money"] - xrhmata

    elif(epilogh=="report" or epilogh=="R"):
        report(ylika)
        print()
    else:
        if (epilogh== "off"):
            print("Exiting ...")
            print()
            break