import json

menu = {
    "burger": 10.99,
    "pizza": 12.99,
    "pasta": 8.99,
    "salad": 5.99,
    "drink": 2.99,
}

def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

def take_order():
    order = {}
    while True:
        item = input("Enter the food that you want (type 'done' to finish): ")
        if item.lower() == 'done':
            break
        if item in menu:
            quantity = int(input(f"How many {item}s do you want to order? "))
            order[item] = quantity

    return order

def calculate_price(order):
    total_price = 0
    for item, quantity in order.items():
        total_price += menu[item] * quantity
    return total_price

def save_order(order, total_price):
    with open("order_details.txt", "w") as file:
        file.write("Order Details:\n")
        for item, quantity in order.items():
            file.write(f"{item} x{quantity}\n")
        file.write(f"Total Price: ${total_price:.2f}")

if __name__ == "__main__":
    display_menu()
    customer_order = take_order()
    order_price = calculate_price(customer_order)
    save_order(customer_order, order_price)
    print("Order placed successfully. Check order_details.txt for details.")
