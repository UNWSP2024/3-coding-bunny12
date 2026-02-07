# Name: Abrielle Nyei
# Program: Shipping Charges
# Date: February 6, 2026

weight = float(input("Enter the package weight: "))

if weight <= 2:
    price_per_pound = 1.50
elif weight <= 6:
    price_per_pound = 3.00
elif weight <= 10:
    price_per_pound = 4.00
else:
    price_per_pound = 4.75

total_cost = weight * price_per_pound

print("Total shipping cost: $", format(total_cost, ".2f"))
