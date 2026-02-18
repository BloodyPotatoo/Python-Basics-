#its a cafe system
menu = {
    "coffee": 50,
    "tea": 30,
    "sandwich": 70,
    "burger": 100,
    "pizza": 150,
    "coldrink": 20
}
for key, value in menu.items():
    print(f"{key}: {value}")
order_total = 0

order_1 = input("What would you like to order? ").lower()
if order_1 in menu:
    order_total += menu[order_1]
    print(f"Your order {order_1} has been added")
else:
    print(f"Sorry, {order_1} is not on the menu")
order_2 = input("Anything else?(yes/no): ").lower()
if order_2 == "yes":
    order_2_1 = input("What would you like to order? ").lower()
    if order_2_1 in menu:
        print(f"Your order {order_2_1} has been added")
        order_total += menu[order_2_1]
        print(f"Thank you for your order\nYour total is {order_total}")
    else:
        print(f"Sorry, {order_2_1} is not on the menu")
else:
    print(f"Thank you for your order\nYour total is {order_total}")