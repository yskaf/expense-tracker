# . . Installment 4 . .
print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nWelcome! This is your personal expense tracker.\n")

print("MAIN MENU")
print("[1] Add an expense\t\t(coming soon)")
print("[2] View all expenses\t\t(coming soon)")
print("[3] Show total spent\t\t(coming soon)")
print("[4] Exit\t\t\t(coming soon)\n")


name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subtotal =0 
item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))
if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

subtotal += amount1


item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

subtotal += amount2

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

total = amount1 + amount2
average = total / 2
tax_percent = int(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print("\n" + "-" * 40)
print("SUMMARY")
print("  - " + f"{item1}:\t${amount1}")
print("  - " + f"{item2}:\t${amount2}")

print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}.0%):\t${tax}")
print(f"Grand total:\t${total}")

if over_budget:
    print(f"Over budget by ${total - budget}!")
elif total > budget * 0.9:
    print(f"Careful: only ${left} left.")
else:
    print(f"Within budget. ${left} left.")

print("-" * 40)
print(f"Made by: Jenalyn Myka Ferrer | Installment 4")