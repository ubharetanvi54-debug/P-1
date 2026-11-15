print("================================")
print("       BREW & BITES CAFE")
print("================================")

# Menu and Prices
menu = {
    1: ("Cappuccino", 120),
    2: ("Cold Coffee", 100),
    3: ("Veg Sandwich", 80),
    4: ("French Fries", 70),
    5: ("Chocolate Brownie", 90),
    6: ("Masala Tea", 40)
}

print("\n----------- MENU -----------")

for item, details in menu.items():
    print(item, ".", details[0], "Rs.", details[1])

print("----------------------------")

total = 0

n = int(input("Enter number of items: "))

for i in range(n):
    choice = int(input("\nEnter item number: "))
    quantity = int(input("Enter quantity: "))

    if choice in menu:
        price = menu[choice][1]
        amount = price * quantity
        total = total + amount
    else:
        print("Invalid item number!")

print("\n================================")
print("          FINAL INVOICE")
print("================================")
print("Total Amount: Rs.", total)
print("================================")
print("      THANK YOU! VISIT AGAIN")
print("================================")
