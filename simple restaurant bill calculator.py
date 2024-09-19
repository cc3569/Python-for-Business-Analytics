# Dictionary with menu items as keys and unit prices as values
menu_items = {
    "Pizza": 10.00,
    "Salad": 7.50,
    "Drink": 2.00
}

# Flagstaff sales tax rate of 9.181%
tax_rate = 0.09181
#5% restaurant service fee
service_fee = 0.05
#Initialize subtotal variable
subtotal = 0.00

# Greeting to customer
print("Hello! Welcome to Simple Restaurant. The menu is provided below.")
print("\n" + "MENU (Prices in U.S. Dollars)")

# For loop used to iterate through menu items. Displays full menu
for key, items in menu_items.items():
  print(key, "$" + format(items, ".2f"))
print("")

# For loop used to iterate through menu items. Prompts user for quantities
# per menu item. Calculates a running total for quantity inputs. Stores total
# in subtotal variable
for food, price in menu_items.items():
  quantity = int(input(f"How Many {food}s Would You Like? "))
  running_total = quantity * price
  subtotal += running_total

# Calculation of total taxes
tax = subtotal * tax_rate
#Calculation of service fees
service = subtotal * service_fee
#Calculation of grand bill total
total_amt = subtotal + tax + service

# Prints bill
print("\nBILL")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Service Fee: ${service:.2f}")
print(f"Total: ${total_amt:.2f}")

print("\nThank You For Dining at Simple Restaurant!")
