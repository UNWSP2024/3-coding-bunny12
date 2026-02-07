# Name: Abrielle Nyei
# Program: Hot Dog
# Date: February 6, 2026

price = 0
tax_rate = 0.07

print("1. Hot Dog ($3.50)")
print("2. Chili Dog ($4.50)")

choice = int(input("Choose a hot dog (1 or 2): "))

if choice == 1:
    price = 3.50
else:
    price = 4.50

cheese = input("Do you want cheese? (y/n): ")
if cheese == "y":
    price = price + 0.50

peppers = input("Do you want peppers? (y/n): ")
if peppers == "y":
    price = price + 0.75

onions = input("Do you want grilled onions? (y/n): ")
if onions == "y":
    price = price + 1.00

tax = price * tax_rate
total = price + tax

print("Cost: $", format(price, ".2f"))
print("Tax: $", format(tax, ".2f"))
print("Total: $", format(total, ".2f"))
