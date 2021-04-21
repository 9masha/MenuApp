
from db import *
from restaurant import *


food = load('food')
order = {
    "items": [],
    "total": {
        "amount": 0.00,
        "currency": "MDL"
    },
    "client": {
            "client_name": ' ',
            "address":  '',
            "phone number": ' '
        },
    "delivery" : {
            "amount": 0.00,
            "currency": "MDL"
    }
}
while True:
    action = printActionsMenu(
        ["Show food",
         "Order food",
         "Show order",
         "Checkout",
         "Exit"],
        "MAIN MENU"
    )
    if action == 1:

        printItems(food, "Today in Menu:")

    if action == 2:
        item_i = int(input("Which item do you want to order?")) - 1
        try:
            item_q = int(input(f"How many portions of ❮{food[item_i]['name']}❯ do you want?"))
            if food[item_i]['available'] < item_q:
                print()
                print(f"Unfortunately, we do NOT have so many portions of ❮{food[item_i]['name']}❯, please try again. ")
                input("Hit ENTER to come back...")
            else:
                print()
                print(f"You have just added {item_q} portions of ❮{food[item_i]['name']}❯ ")
                print()
                new_item = createOrderItem(food, item_i, item_q)
                order['items'].append(new_item)
                order['total']['amount'] += new_item['price']['amount']

                input("Hit ENTER to come back...")

        except:
            print(f"Unfortunately, we do NOT have so many portions of ❮{food[item_i]['name']}❯, please try again. ")
            continue




    if action == 3:
        printItems(order["items"], "YOUR ORDER:")

    if action == 4:
        client_name = input("Enter you First and Last Name: ")
        address = input("Enter your adress:")
        ph_number = input("Enter your phone number:")
        order['client']['client_name'] = client_name
        order['client']['address'] = address
        order['client']['phone number'] = ph_number
        delivery_choice = input("Do you need delivery? Y/N")
        if delivery_choice == "Y":
            if order['total']['amount'] < 200:
                order['delivery']['amount'] = 100
                order['total']['amount'] += order['delivery']['amount']
            print("Thank you for your order. Food will be delivered to the address mentioned.")
        else:
            print("Thank you for your oder. You can pick up the food in 15 Minutes.")
        orderWrite(order)



    if action == 5:
        break
