import random
import pandas as pd
from datetime import date, timedelta

random.seed(42)

products = {
    "Bread": ("Bakery", 40), "Milk": ("Dairy", 30), "Butter": ("Dairy", 55),
    "Eggs": ("Dairy", 70), "Rice": ("Grocery", 60), "Cooking Oil": ("Grocery", 140),
    "Dal": ("Grocery", 95), "Sugar": ("Grocery", 45), "Tea": ("Beverages", 120),
    "Coffee": ("Beverages", 180), "Juice": ("Beverages", 85), "Biscuits": ("Snacks", 20),
    "Chips": ("Snacks", 25), "Soap": ("Personal Care", 35), "Shampoo": ("Personal Care", 90),
    "Toothpaste": ("Personal Care", 60), "Detergent": ("Household", 110),
    "Tomato": ("Vegetables", 30), "Onion": ("Vegetables", 35), "Potato": ("Vegetables", 28),
}
combos = [
    ["Bread", "Milk", "Butter"], ["Rice", "Cooking Oil", "Dal"],
    ["Shampoo", "Soap", "Toothpaste"], ["Tea", "Sugar", "Biscuits"],
    ["Tomato", "Onion", "Potato"], ["Chips", "Juice"],
    ["Coffee", "Milk", "Sugar"], ["Eggs", "Bread"],
]
cities = ["Ballari", "Raichur", "Bengaluru", "Hubballi", "Kalaburagi"]
payments = ["Cash", "UPI", "Card"]

customers = {
    f"C{i:03d}": (random.choice(["18-25", "26-35", "36-50", "50+"]),
                  random.choice(["Male", "Female"]),
                  random.choice(cities))
    for i in range(1, 81)
}

rows = []
for t in range(1, 601):
    cust = random.choice(list(customers))
    age, gender, city = customers[cust]
    basket = set()
    for combo in random.sample(combos, random.choice([1, 1, 2])):
        basket |= {p for p in combo if random.random() > 0.15}
    basket |= set(random.sample(list(products), random.choice([0, 1, 2])))
    if not basket:
        basket = {random.choice(list(products))}
    d = date(2025, 1, 1) + timedelta(days=random.randint(0, 364))
    pay, disc = random.choice(payments), random.choice(["Yes", "No"])
    for p in basket:
        cat, price = products[p]
        rows.append([f"T{t:04d}", cust, d, age, gender, city, p, cat,
                     random.randint(1, 3), price, pay, disc])

# Injecting the 8 dirty rows explicitly for preprocessing validation
rows.append([f"T0001", "C001", "2025-06-01", "18-25", "Male", "Ballari", "Bread", "Bakery", 1, 40, "UPI", "No"]) 
rows.append([f"T0001", "C001", "2025-06-01", "18-25", "Male", "Ballari", "Bread", "Bakery", 1, 40, "UPI", "No"])
rows.append([f"T0001", "C001", "2025-06-01", "18-25", "Male", "Ballari", "Bread", "Bakery", 1, 40, "UPI", "No"])
rows.append([f"T0601", "C005", "2025-07-12", "26-35", "Female", "Raichur", None, "Grocery", 2, 95, "Cash", "Yes"])
rows.append([f"T0602", "C012", "2025-08-19", "50+", "Male", "Bengaluru", None, "Dairy", 1, 30, "Card", "No"])
rows.append([f"T0603", "C022", "2025-03-22", "36-50", "Female", "Hubballi", "Chips", "Snacks", -5, 25, "UPI", "No"])
rows.append([f"T0604", "C031", "2025-11-05", "18-25", "Male", "Kalaburagi", "Tomato", "Vegetables", 3, 0, "Cash", "No"])
rows.append([f"T0605", "C044", "2025-01-15", "26-35", "Female", None, "Milk", "Dairy", 1, 30, "UPI", "Yes"])

df = pd.DataFrame(rows, columns=[
    "transaction_id", "customer_id", "transaction_date", "age_group", "gender",
    "city", "product", "category", "quantity", "unit_price",
    "payment_method", "discount_applied"])
df.to_csv("customer_shopping_transactions.csv", index=False)
print("Success! Generated raw dataset with shape:", df.shape)
