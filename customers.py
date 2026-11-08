# ISM2411 Lab 11 - Customer Dictionary & Lookup
# Name: Hunter
#
# REFLECTION (write your own answers, 2-3 sentences each)
#
# 1. In Exercise 3 you saw the difference between .get() and bracket notation.
#    When in real work would you use each one, and what's your rule of thumb?
#
#     I would use bracket notation when I'm certain a key exists and want my code to fail fast if it's missing,
#     whereas I'd use .get() when dealing with messy external data or optional fields where a missing key is normal. 
#     My rule of thumb is to use brackets for required configuration or database fields and .get() with a default value for user inputs or API responses.
#
# 2. Exercise 8 built a summary dictionary with a loop. What does this remind
#    you of from Excel, and why might the Python version be more useful for
#    large datasets?
#
#    This loop reminds me of an Excel PivotTable or a SUMIFS function that aggregates sales numbers by a specific category like region.
#    The Python version is much better for large datasets because it avoids Excel's row limits, runs much faster, and can easily automate 
#    processing millions of records without manual spreadsheet manipulation.


# ---------------------------------------------------------------------------
# Exercise 1: One customer
# ---------------------------------------------------------------------------
print("=== Exercise 1: One customer ===")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# ---------------------------------------------------------------------------
# Exercise 2: Update and add
# ---------------------------------------------------------------------------
print("\n=== Exercise 2: Update and add ===")
customer["phone"] = "305-555-0142"      # add a new field
print(customer)

customer["tier"] = "platinum"           # update an existing field
print(customer)

del customer["email"]                   # remove a field
print(customer)


# ---------------------------------------------------------------------------
# Exercise 3: Safe lookup
# ---------------------------------------------------------------------------
print("\n=== Exercise 3: Safe lookup ===")
# .get() returns the default instead of crashing when the key is missing
print(customer.get("email", "no email on file"))

# Bracket notation raises KeyError for a missing key
try:
    print(customer["email"])
except KeyError as err:
    print(f"KeyError: {err}")


# ---------------------------------------------------------------------------
# Exercise 4: Iterate
# ---------------------------------------------------------------------------
print("\n=== Exercise 4: Iterate ===")
for key, value in customer.items():
    print(f"{key}: {value}")

# Looping over the dict without .items() only gives you the keys (one value
# per pass), so you'd have to look up each value yourself with customer[key].
# .items() hands you the key AND the value together on every pass.
print("-- without .items() --")
for key in customer:
    print(key)


# ---------------------------------------------------------------------------
# Exercise 5: Lookup table
# ---------------------------------------------------------------------------
print("\n=== Exercise 5: Lookup table ===")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)   # unknown tier -> no discount
purchase = 200
final_price = purchase * (1 - discount)
print(f"Tier: {tier} | Discount: {discount:.0%} | Final price: ${final_price:.2f}")


# ---------------------------------------------------------------------------
# Exercise 6: List of dicts
# ---------------------------------------------------------------------------
print("\n=== Exercise 6: List of dicts ===")
customers = [
    {"name": "Alice", "email": "alice@example.com", "tier": "platinum", "ytd_spend": 5200.00},
    {"name": "Bob",   "email": "bob@example.com",   "tier": "silver",   "ytd_spend": 840.25},
    {"name": "Carla", "email": "carla@example.com", "tier": "gold",     "ytd_spend": 2310.75},
    {"name": "Dev",   "email": "dev@example.com",   "tier": "bronze",   "ytd_spend": 95.00},
]

purchase = 300
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = purchase * rate
    print(f"{c['name']:<6} | {c['tier']:<9} | discount on ${purchase}: ${discount_amount:.2f}")


# ---------------------------------------------------------------------------
# Exercise 7: Nested catalog
# ---------------------------------------------------------------------------
print("\n=== Exercise 7: Nested catalog ===")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} (only {info['stock']} left)")


# ---------------------------------------------------------------------------
# Exercise 8: Sales by region
# ---------------------------------------------------------------------------
print("\n=== Exercise 8: Sales by region ===")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

region_totals = {}
for t in transactions:
    region_totals[t["region"]] = region_totals.get(t["region"], 0) + t["amount"]

for region in sorted(region_totals):
    print(f"{region}: {region_totals[region]}")
