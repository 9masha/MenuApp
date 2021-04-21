from math import ceil
from os import system


def printItems(items, title=None):
    system("cls")
    if title == None:
        print("#" * 40)
    else:
        print("#" * 40)
        print(title.center(40))
        print("-" * 40)
    if len(items) == 0:
        print("Empty.")
        print("#" * 40)
    if title == "YOUR ORDER:":
        for i in range(len(items)):
            print(
                f"{i + 1 :<2} {items[i]['name']:12} {items[i]['price']['amount']:5}{items[i]['price']['currency']:>4} x{items[i]['quantity']:2} {items[i]['total']['amount']:6}{items[i]['total']['currency']:>4} ")
        print("#" * 40)
    if title == "Today in Menu:":
        paginatorItems(items, title)
    input("Hit ENTER to come back...")


def printActionsMenu(items, title=None):
    system("cls")
    if title == None:
        print("#" * 40)
    else:
        print("#" * 40)
        print(title.center(40))
        print("-" * 40)
    for i in range(len(items)):
        print(f"{i + 1 :<2} {items[i]:12}")
    print("#" * 40)
    option = int(input(">>>>>"))
    return option


def createOrderItem(food, item_i, item_q):
    return{
        "name": food[item_i]['name'],
        "quantity": item_q,
        "price": {
            "amount": food[item_i]['price']['amount'],
            "currency": "MDL"
        },
    }



def paginatorItems(items, title):
    page = 0
    per_page = 5
    last_page = ceil(len(items) // per_page)
    while True:
        if page > 0:
            print("#" * 40)
            print(title.center(40))
            print("-" * 40)

        for i in range(page * per_page, page * per_page + per_page):
            try:
                print(
                    f"{i + 1 :<2}{items[i]['name']:12} {items[i]['price']['amount']:>15}{items[i]['price']['currency']:>4}")
            except:
                pass
        for x in range(last_page + 1):
            if x == page:
                print("[", x + 1, "]", end=" ")
            else:
                print(x + 1, end=" ")
        print("\n")
        print("#" * 40)

        page_change = input('enter "p" to change page number "<" / ">"  to go to the prev / next page  "x" to exit')
        if page_change == "<" and page >= 1:
            page -= 1
        if page_change == ">" and page < last_page:
            page += 1
        if page_change == "p":
            page = (int(input("What page would you like to go to? ")) - 1)
        if page_change == "x":
            break


def orderWrite(order):
    with open('bill.txt', 'w') as out:
        for key, val in order.items():
            out.write('{}:{}\n'.format(key, val))

