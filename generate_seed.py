import random
from datetime import datetime, timedelta

random.seed(42)

# ----------------------------------------------------------------
# Reference data pools
# ----------------------------------------------------------------

CUISINES = ["Italian", "Mexican", "Japanese", "Indian", "French", "Thai",
            "Greek", "Chinese", "Korean", "Spanish", "Lebanese", "American",
            "Vietnamese", "Moroccan", "Turkish", "Peruvian", "Ethiopian",
            "Cajun", "Brazilian", "German"]

REST_ADJ = ["Golden", "Blue", "Rustic", "Urban", "Coastal", "Royal", "Hidden",
            "Olive", "Saffron", "Velvet", "Copper", "Stone", "Garden",
            "Harbor", "Sunset", "Maple", "Silver", "Amber", "Wild", "Cedar"]

REST_NOUN = ["Table", "Kitchen", "Bistro", "Tavern", "Grill", "House",
             "Plate", "Pot", "Fork", "Spoon", "Oven", "Vine", "Hearth",
             "Market", "Diner", "Cantina", "Trattoria", "Brasserie",
             "Cellar", "Terrace"]

STREET_NAMES = ["Main St", "Oak Ave", "Maple Dr", "Elm St", "Cedar Ln",
                "Park Rd", "Highland Ave", "River Rd", "Sunset Blvd",
                "Market St", "Church St", "Mill St", "King St", "Queen St",
                "Broadway", "5th Ave", "2nd St", "Pine St", "Willow Way",
                "Lake Dr"]

CITIES = ["Springfield", "Riverside", "Fairview", "Madison", "Georgetown",
          "Salem", "Greenville", "Bristol", "Clinton", "Franklin",
          "Arlington", "Burlington", "Dover", "Manchester", "Auburn",
          "Oakland", "Richmond", "Lancaster", "Centerville", "Newport"]

FIRST_NAMES = ["James","Mary","John","Patricia","Robert","Jennifer","Michael",
    "Linda","William","Elizabeth","David","Barbara","Richard","Susan",
    "Joseph","Jessica","Thomas","Sarah","Charles","Karen","Daniel","Nancy",
    "Matthew","Lisa","Anthony","Margaret","Mark","Betty","Donald","Sandra",
    "Steven","Ashley","Paul","Kimberly","Andrew","Emily","Joshua","Donna",
    "Kenneth","Michelle","Kevin","Carol","Brian","Amanda","George","Melissa",
    "Edward","Deborah","Ronald","Stephanie","Timothy","Rebecca","Jason",
    "Laura","Jeffrey","Sharon","Ryan","Cynthia","Jacob","Kathleen","Gary",
    "Amy","Nicholas","Shirley","Eric","Angela","Jonathan","Helen","Stephen",
    "Anna","Larry","Brenda","Justin","Pamela","Scott","Nicole","Brandon",
    "Emma","Benjamin","Samantha","Samuel","Katherine","Gregory","Christine",
    "Frank","Debra","Alexander","Rachel","Raymond","Catherine","Patrick",
    "Carolyn","Jack","Janet","Dennis","Maria","Jerry","Heather"]

LAST_NAMES = ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller",
    "Davis","Rodriguez","Martinez","Hernandez","Lopez","Gonzalez","Wilson",
    "Anderson","Thomas","Taylor","Moore","Jackson","Martin","Lee","Perez",
    "Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson",
    "Walker","Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill",
    "Flores","Green","Adams","Nelson","Baker","Hall","Rivera","Campbell",
    "Mitchell","Carter","Roberts","Gomez","Phillips","Evans","Turner","Diaz",
    "Parker","Cruz","Edwards","Collins","Reyes","Stewart","Morris","Morales",
    "Murphy","Cook","Rogers","Gutierrez","Ortiz","Morgan","Cooper","Peterson",
    "Bailey","Reed","Kelly","Howard","Ramos","Kim","Cox","Ward","Richardson",
    "Watson","Brooks","Chavez","Wood","James","Bennett","Gray","Mendoza",
    "Ruiz","Hughes","Price","Alvarez","Castillo","Sanders","Patel","Myers",
    "Long","Ross","Foster","Jimenez"]

POSITIONS = ["Waiter", "Waitress", "Head Chef", "Sous Chef", "Line Cook",
             "Host", "Hostess", "Bartender", "Manager", "Assistant Manager",
             "Busser", "Dishwasher", "Sommelier", "Pastry Chef", "Cashier"]

CATEGORIES = {
    "Starters": ["Bruschetta", "Spring Rolls", "Calamari", "Hummus Plate",
        "Stuffed Mushrooms", "Garlic Bread", "Edamame", "Samosas",
        "Caprese Salad", "Onion Rings", "Soup of the Day", "Nachos"],
    "Mains": ["Grilled Salmon", "Margherita Pizza", "Beef Tenderloin",
        "Chicken Tikka Masala", "Pad Thai", "Lamb Chops", "Vegetable Curry",
        "Spaghetti Carbonara", "Sushi Platter", "BBQ Ribs", "Mushroom Risotto",
        "Fish Tacos", "Roast Duck", "Falafel Wrap", "Pulled Pork Sandwich",
        "Eggplant Parmesan", "Steak Frites", "Shrimp Scampi"],
    "Desserts": ["Tiramisu", "Cheesecake", "Chocolate Lava Cake",
        "Creme Brulee", "Baklava", "Apple Pie", "Gelato", "Panna Cotta",
        "Churros", "Mochi Ice Cream"],
    "Beverages": ["Iced Tea", "Sparkling Water", "Fresh Lemonade",
        "Espresso", "Cappuccino", "House Red Wine", "House White Wine",
        "Craft Lager", "Mango Smoothie", "Cold Brew Coffee"],
}

DESCRIPTIONS = {
    "Starters": "A light dish to begin the meal.",
    "Mains": "A hearty entree prepared fresh to order.",
    "Desserts": "A sweet finish to your dining experience.",
    "Beverages": "Refreshing drink served chilled or hot as noted.",
}

# ----------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------

def esc(s):
    return s.replace("'", "''")

def random_phone():
    return f"({random.randint(200,999)}) {random.randint(200,999)}-{random.randint(1000,9999)}"

def random_opening_hours():
    open_h = random.choice([7, 8, 9, 10, 11])
    close_h = random.choice([21, 22, 23])
    return f"{open_h:02d}:00-{close_h:02d}:00"

def random_date(start, end):
    delta = end - start
    return start + timedelta(seconds=random.randint(0, int(delta.total_seconds())))

# ----------------------------------------------------------------
# 1. Restaurants (50)
# ----------------------------------------------------------------

NUM_RESTAURANTS = 50
restaurants = []
used_names = set()
for i in range(1, NUM_RESTAURANTS + 1):
    while True:
        cuisine = random.choice(CUISINES)
        name = f"{random.choice(REST_ADJ)} {random.choice(REST_NOUN)}"
        if name not in used_names:
            used_names.add(name)
            break
    address = f"{random.randint(10,9999)} {random.choice(STREET_NAMES)}, {random.choice(CITIES)}"
    restaurants.append({
        "id": i,
        "name": name,
        "cuisine": cuisine,
        "address": address,
        "phone": random_phone(),
        "hours": random_opening_hours(),
    })

# ----------------------------------------------------------------
# 2. Tables (100) - spread across restaurants, each restaurant >= 1
# ----------------------------------------------------------------

NUM_TABLES = 100
tables = []
tid = 1
# guarantee every restaurant gets at least 1 table
for r in restaurants:
    tables.append({"id": tid, "restaurant_id": r["id"], "capacity": random.choice([2,2,4,4,4,6,8])})
    tid += 1
# distribute the remaining tables randomly
while tid <= NUM_TABLES:
    r = random.choice(restaurants)
    tables.append({"id": tid, "restaurant_id": r["id"], "capacity": random.choice([2,2,4,4,4,6,8,10])})
    tid += 1

tables_by_restaurant = {}
for t in tables:
    tables_by_restaurant.setdefault(t["restaurant_id"], []).append(t)
# any restaurant somehow without a table (shouldn't happen) gets one
for r in restaurants:
    if r["id"] not in tables_by_restaurant:
        tables_by_restaurant[r["id"]] = []

# ----------------------------------------------------------------
# 3. MenuItems (1000) - spread across restaurants, cuisine-flavored
# ----------------------------------------------------------------

NUM_MENU_ITEMS = 1000
menu_items = []
mid = 1
# guarantee each restaurant has a reasonable base menu (~14 items: distribute later)
base_per_restaurant = NUM_MENU_ITEMS // NUM_RESTAURANTS  # 20
remainder = NUM_MENU_ITEMS - base_per_restaurant * NUM_RESTAURANTS

counts = [base_per_restaurant] * NUM_RESTAURANTS
for i in random.sample(range(NUM_RESTAURANTS), remainder):
    counts[i] += 1

for idx, r in enumerate(restaurants):
    n_items = counts[idx]
    used_items_for_rest = set()
    for _ in range(n_items):
        category = random.choice(list(CATEGORIES.keys()))
        dish_pool = CATEGORIES[category]
        dish = random.choice(dish_pool)
        # allow repeats across restaurants but vary naming slightly if repeated within same restaurant
        key = (category, dish)
        suffix = ""
        if key in used_items_for_rest:
            suffix = f" ({r['cuisine']} style)"
        used_items_for_rest.add(key)
        name = dish + suffix
        if category == "Mains":
            price = round(random.uniform(12.0, 38.0), 2)
        elif category == "Starters":
            price = round(random.uniform(5.0, 14.0), 2)
        elif category == "Desserts":
            price = round(random.uniform(4.0, 11.0), 2)
        else:
            price = round(random.uniform(2.5, 9.0), 2)
        menu_items.append({
            "id": mid,
            "restaurant_id": r["id"],
            "name": name,
            "description": DESCRIPTIONS[category],
            "price": price,
        })
        mid += 1

menu_items_by_restaurant = {}
for m in menu_items:
    menu_items_by_restaurant.setdefault(m["restaurant_id"], []).append(m)

# ----------------------------------------------------------------
# 4. Employees (100) - spread across restaurants, each restaurant >= 1
# ----------------------------------------------------------------

NUM_EMPLOYEES = 100
employees = []
eid = 1
for r in restaurants:
    employees.append({
        "id": eid,
        "restaurant_id": r["id"],
        "first": random.choice(FIRST_NAMES),
        "last": random.choice(LAST_NAMES),
        "position": random.choice(POSITIONS),
    })
    eid += 1
while eid <= NUM_EMPLOYEES:
    r = random.choice(restaurants)
    employees.append({
        "id": eid,
        "restaurant_id": r["id"],
        "first": random.choice(FIRST_NAMES),
        "last": random.choice(LAST_NAMES),
        "position": random.choice(POSITIONS),
    })
    eid += 1

employees_by_restaurant = {}
for e in employees:
    employees_by_restaurant.setdefault(e["restaurant_id"], []).append(e)

# ----------------------------------------------------------------
# 5. Customers (400)
# ----------------------------------------------------------------

NUM_CUSTOMERS = 400
customers = []
used_emails = set()
for i in range(1, NUM_CUSTOMERS + 1):
    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)
    base_email = f"{first.lower()}.{last.lower()}"
    email = f"{base_email}{i}@example.com"
    customers.append({
        "id": i,
        "first": first,
        "last": last,
        "email": email,
        "phone": random_phone(),
    })

# ----------------------------------------------------------------
# 6. Reservations (500) - each tied to valid restaurant + its own table
# ----------------------------------------------------------------

NUM_RESERVATIONS = 500
reservations = []
RES_START = datetime(2025, 1, 1)
RES_END = datetime(2026, 6, 30)

for i in range(1, NUM_RESERVATIONS + 1):
    customer = random.choice(customers)
    restaurant = random.choice(restaurants)
    table = random.choice(tables_by_restaurant[restaurant["id"]])
    party_size = min(table["capacity"], random.choice([1,2,2,2,3,4,4,5,6,8]))
    res_date = random_date(RES_START, RES_END)
    reservations.append({
        "id": i,
        "customer_id": customer["id"],
        "restaurant_id": restaurant["id"],
        "table_id": table["id"],
        "date": res_date,
        "party_size": party_size,
    })

# ----------------------------------------------------------------
# 7. Orders (500) - ~70% tied to a reservation, ~30% walk-in (NULL)
#    employee must belong to the same restaurant as the reservation
#    order date is on/after the reservation date when linked
# ----------------------------------------------------------------

NUM_ORDERS = 500
orders = []
order_id = 1

reservations_shuffled = reservations[:]
random.shuffle(reservations_shuffled)
num_with_reservation = int(NUM_ORDERS * 0.7)

for i in range(num_with_reservation):
    res = reservations_shuffled[i % len(reservations_shuffled)]
    restaurant_id = res["restaurant_id"]
    emp_pool = employees_by_restaurant[restaurant_id]
    employee = random.choice(emp_pool)
    order_date = res["date"] + timedelta(minutes=random.randint(0, 90))
    orders.append({
        "id": order_id,
        "reservation_id": res["id"],
        "restaurant_id": restaurant_id,
        "employee_id": employee["id"],
        "date": order_date,
        "total": 0.0,  # filled after order items generated
    })
    order_id += 1

while order_id <= NUM_ORDERS:
    restaurant = random.choice(restaurants)
    emp_pool = employees_by_restaurant[restaurant["id"]]
    employee = random.choice(emp_pool)
    order_date = random_date(RES_START, RES_END)
    orders.append({
        "id": order_id,
        "reservation_id": None,
        "restaurant_id": restaurant["id"],
        "employee_id": employee["id"],
        "date": order_date,
        "total": 0.0,
    })
    order_id += 1

orders_by_id = {o["id"]: o for o in orders}

# ----------------------------------------------------------------
# 8. OrderItems (1500) - each order gets 1+ items from its own
#    restaurant's menu; TotalAmount on Orders computed from these
# ----------------------------------------------------------------

NUM_ORDER_ITEMS = 1500
order_items = []
oi_id = 1

# guarantee every order has at least 1 item
order_ids_list = [o["id"] for o in orders]
remaining_slots = NUM_ORDER_ITEMS - NUM_ORDERS  # extra items beyond the guaranteed 1 each

for o in orders:
    menu_pool = menu_items_by_restaurant[o["restaurant_id"]]
    item = random.choice(menu_pool)
    qty = random.choice([1,1,1,2,2,3])
    order_items.append({"id": oi_id, "order_id": o["id"], "item_id": item["id"],
                         "quantity": qty, "unit_price": item["price"]})
    oi_id += 1

# distribute the remaining items across random orders (weighted, but every order can get more)
for _ in range(remaining_slots):
    o = random.choice(orders)
    menu_pool = menu_items_by_restaurant[o["restaurant_id"]]
    item = random.choice(menu_pool)
    qty = random.choice([1,1,1,2,2,3])
    order_items.append({"id": oi_id, "order_id": o["id"], "item_id": item["id"],
                         "quantity": qty, "unit_price": item["price"]})
    oi_id += 1

# compute TotalAmount per order from its order items
totals = {}
for oi in order_items:
    totals[oi["order_id"]] = totals.get(oi["order_id"], 0.0) + oi["quantity"] * oi["unit_price"]

for o in orders:
    o["total"] = round(totals.get(o["id"], 0.0), 2)

print("Restaurants:", len(restaurants))
print("Tables:", len(tables))
print("MenuItems:", len(menu_items))
print("Employees:", len(employees))
print("Customers:", len(customers))
print("Reservations:", len(reservations))
print("Orders:", len(orders))
print("OrderItems:", len(order_items))

# ----------------------------------------------------------------
# Write DML
# ----------------------------------------------------------------

lines = []
lines.append("-- =========================================================")
lines.append("-- Restaurant Management System - Seed Data (DML)")
lines.append("-- Generated fictional but internally consistent dataset")
lines.append("-- 50 Restaurants | 100 Tables | 1000 MenuItems | 100 Employees")
lines.append("-- 400 Customers | 500 Reservations | 500 Orders | 1500 OrderItems")
lines.append("-- =========================================================")
lines.append("")
lines.append("USE RestaurantDB;")
lines.append("GO")
lines.append("")
lines.append("SET NOCOUNT ON;")
lines.append("GO")
lines.append("")

def fmt_dt(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")

# Restaurants
lines.append("-- ---------------------------------------------------------")
lines.append("-- Restaurants (50)")
lines.append("-- ---------------------------------------------------------")
lines.append("SET IDENTITY_INSERT Restaurants ON;")
for r in restaurants:
    lines.append(
        f"INSERT INTO Restaurants (RestaurantId, Name, Address, PhoneNumber, OpeningHours) VALUES "
        f"({r['id']}, N'{esc(r['name'])} ({esc(r['cuisine'])})', N'{esc(r['address'])}', "
        f"N'{r['phone']}', N'{r['hours']}');"
    )
lines.append("SET IDENTITY_INSERT Restaurants OFF;")
lines.append("GO")
lines.append("")

# Tables
lines.append("-- ---------------------------------------------------------")
lines.append("-- Tables (100)")
lines.append("-- ---------------------------------------------------------")
lines.append("SET IDENTITY_INSERT Tables ON;")
for t in tables:
    lines.append(
        f"INSERT INTO Tables (TableId, RestaurantId, Capacity) VALUES "
        f"({t['id']}, {t['restaurant_id']}, {t['capacity']});"
    )
lines.append("SET IDENTITY_INSERT Tables OFF;")
lines.append("GO")
lines.append("")

# MenuItems
lines.append("-- ---------------------------------------------------------")
lines.append("-- MenuItems (1000)")
lines.append("-- ---------------------------------------------------------")
lines.append("SET IDENTITY_INSERT MenuItems ON;")
for m in menu_items:
    lines.append(
        f"INSERT INTO MenuItems (ItemId, RestaurantId, Name, Description, Price) VALUES "
        f"({m['id']}, {m['restaurant_id']}, N'{esc(m['name'])}', N'{esc(m['description'])}', {m['price']});"
    )
lines.append("SET IDENTITY_INSERT MenuItems OFF;")
lines.append("GO")
lines.append("")

# Employees
lines.append("-- ---------------------------------------------------------")
lines.append("-- Employees (100)")
lines.append("-- ---------------------------------------------------------")
lines.append("SET IDENTITY_INSERT Employees ON;")
for e in employees:
    lines.append(
        f"INSERT INTO Employees (EmployeeId, RestaurantId, FirstName, LastName, Position) VALUES "
        f"({e['id']}, {e['restaurant_id']}, N'{esc(e['first'])}', N'{esc(e['last'])}', N'{esc(e['position'])}');"
    )
lines.append("SET IDENTITY_INSERT Employees OFF;")
lines.append("GO")
lines.append("")

# Customers
lines.append("-- ---------------------------------------------------------")
lines.append("-- Customers (400)")
lines.append("-- ---------------------------------------------------------")
lines.append("SET IDENTITY_INSERT Customers ON;")
for c in customers:
    lines.append(
        f"INSERT INTO Customers (CustomerId, FirstName, LastName, Email, PhoneNumber) VALUES "
        f"({c['id']}, N'{esc(c['first'])}', N'{esc(c['last'])}', N'{esc(c['email'])}', N'{c['phone']}');"
    )
lines.append("SET IDENTITY_INSERT Customers OFF;")
lines.append("GO")
lines.append("")

# Reservations
lines.append("-- ---------------------------------------------------------")
lines.append("-- Reservations (500)")
lines.append("-- ---------------------------------------------------------")
lines.append("SET IDENTITY_INSERT Reservations ON;")
for r in reservations:
    lines.append(
        f"INSERT INTO Reservations (ReservationId, CustomerId, RestaurantId, TableId, ReservationDate, PartySize) VALUES "
        f"({r['id']}, {r['customer_id']}, {r['restaurant_id']}, {r['table_id']}, "
        f"'{fmt_dt(r['date'])}', {r['party_size']});"
    )
lines.append("SET IDENTITY_INSERT Reservations OFF;")
lines.append("GO")
lines.append("")

# Orders
lines.append("-- ---------------------------------------------------------")
lines.append("-- Orders (500) - ~70% linked to a reservation, rest walk-in")
lines.append("-- ---------------------------------------------------------")
lines.append("SET IDENTITY_INSERT Orders ON;")
for o in orders:
    res_val = "NULL" if o["reservation_id"] is None else str(o["reservation_id"])
    lines.append(
        f"INSERT INTO Orders (OrderId, ReservationId, EmployeeId, OrderDate, TotalAmount) VALUES "
        f"({o['id']}, {res_val}, {o['employee_id']}, '{fmt_dt(o['date'])}', {o['total']});"
    )
lines.append("SET IDENTITY_INSERT Orders OFF;")
lines.append("GO")
lines.append("")

# OrderItems
lines.append("-- ---------------------------------------------------------")
lines.append("-- OrderItems (1500)")
lines.append("-- ---------------------------------------------------------")
lines.append("SET IDENTITY_INSERT OrderItems ON;")
for oi in order_items:
    lines.append(
        f"INSERT INTO OrderItems (OrderItemId, OrderId, ItemId, Quantity) VALUES "
        f"({oi['id']}, {oi['order_id']}, {oi['item_id']}, {oi['quantity']});"
    )
lines.append("SET IDENTITY_INSERT OrderItems OFF;")
lines.append("GO")
lines.append("")

with open("/home/claude/seed_data.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("\nSeed SQL file written.")
