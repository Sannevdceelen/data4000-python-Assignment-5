# pos_checkout.py
# DATA 4000 – Assignment 5
# Exercise 1: Point-of-Sale Checkout System

# ---------------------------
# Step 1 — Student Key & Seed
# ---------------------------

student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

# ---------------------------
# Step 2 — Item Entry Loop
# ---------------------------

subtotal = 0.0
total_units = 0

while True:
    item_name = input("Enter item name (or DONE to finish): ").strip()

    if item_name.upper() == "DONE":
        break

    # Step 3 — Validate Item Name
    if item_name == "":
        print("Invalid item name. Try again.")
        continue

    # Validate Unit Price
    try:
        unit_price = float(input("Enter unit price: "))
        if unit_price <= 0:
            print("Unit price must be greater than 0.")
            continue
    except ValueError:
        print("Invalid price. Try again.")
        continue

    # Validate Quantity
    try:
        quantity = int(input("Enter quantity: "))
        if quantity < 1:
            print("Quantity must be at least 1.")
            continue
    except ValueError:
        print("Invalid quantity. Try again.")
        continue

    # Step 4 — Running Totals
    subtotal += unit_price * quantity
    total_units += quantity


# ---------------------------
# Step 5 — Discount Logic
# ---------------------------

if total_units >= 10 or subtotal >= 100:
    discount_percent = 10
else:
    discount_percent = 0

discount_amount = subtotal * (discount_percent / 100)
total_after_discount = subtotal - discount_amount


# ---------------------------
# Step 6 — Seed-Based Perk
# ---------------------------

perk_applied = "NO"

if seed % 2 != 0:   # odd seed
    total_after_discount -= 3.00
    perk_applied = "YES"

if total_after_discount < 0:
    total_after_discount = 0.00


# ---------------------------
# Step 7 — Output Format
# ---------------------------

print(f"Seed: {seed}")
print(f"Units: {total_units}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: {discount_percent}%")
print(f"Perk applied: {perk_applied}")
print(f"Total: ${total_after_discount:.2f}")