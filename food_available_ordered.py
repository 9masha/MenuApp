food_1_name = 'Pizza'
food_2_name = "Hamburger"
food_3_name = "Latte"

food_1_price = 100       # MDL
food_2_price = 45        # MDL
food_3_price = 30        # MDL

food_1_available:int = 5
food_2_available:int = 7
food_3_available:int = 10

food_1_quantity = int(input('How many ' + food_1_name + 's do you want ?'))
food_2_quantity = int(input('How many ' + food_2_name + 's do you want ?'))
food_3_quantity = int(input('How many ' + food_3_name + 's do you want ?'))

food_1_cost = int(food_1_quantity * food_1_price)
food_2_cost = int(food_2_quantity * food_2_price)
food_3_cost = int(food_3_quantity * food_3_price)

total_food = food_1_cost + food_2_cost + food_3_cost


if food_1_quantity > food_1_available:
    print("Sorry, we have just:", food_1_available, food_1_name, "Please, try again.")
elif food_1_quantity < 0:
    print("Sorry the amount of", food_1_name, "is incorrect. Please, try again.")
else:
    print('You have ordered ', food_1_quantity, ' x ', food_1_name, ' = ', food_1_cost)

    if food_2_quantity > food_2_available:
        print("Sorry, we have just:", food_2_available, food_2_name, "Please, try again.")
    elif food_2_quantity < 0:
        print("Sorry the amount of", food_2_name, "is incorrect. Please, try again.")
    else:
        print('You have ordered ', food_2_quantity, ' x ', food_2_name, ' = ', food_2_cost)

        if food_3_quantity > food_3_available:
            print("Sorry, we have just:", food_3_available, food_3_name, "Please, try again.")
        elif food_3_quantity < 0:
            print("Sorry the amount of", food_3_name, "is incorrect. Please, try again.")
        else:
            print('You have ordered ', food_3_quantity, ' x ', food_3_name, ' = ', food_3_cost)
            food_delivery = input("Do you need the delivery of food? (Yes/No)")
            if food_delivery == "No":
                print ("Thank you for your order! You have to pay:", total_food, "MDL")
            else:
                if total_food >= 1000:
                    print("Thank you for your oder! You get free delivery!You have to pay:", total_food, "MDL")
                else:
                    print("Thank you for your oder! Your delivery will cost you extra 150 MDL. You have to pay:", total_food + 150, "MDL")
