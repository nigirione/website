import json

import os
#PRICES

NORMALBOX = "8.00€"
SPECIALBOX = "8.50€"
RICE = "3.50€"



# Define menu items

menu_items = [
    {"number": "M1","title": "Massa Vegetais", "price": NORMALBOX, "image": "resources/img/kitchen/m1.png"},
    {"number": "M2","title": "Massa c/ Vaca", "price": NORMALBOX, "image": "resources/img/kitchen/m2.png"},
    {"number": "M3","title": "Massa c/ Frango", "price": NORMALBOX, "image": "resources/img/kitchen/m3.png"},
    {"number": "M4","title": "Massa c/ Gambas", "price": NORMALBOX, "image": "resources/img/kitchen/m4.png"},
    {"number": "M5","title": "Massa de Arroz c/ Vegetais", "price": NORMALBOX, "image": "resources/img/kitchen/m5.png"},
    {"number": "M6","title": "Massa de Arroz c/ Frango", "price": NORMALBOX, "image": "resources/img/kitchen/m6.png"},
    {"number": "M7","title": "Massa de Arroz c/ Vaca", "price": NORMALBOX, "image": "resources/img/kitchen/m7.png"},
    {"number": "M8","title": "Massa de Arroz c/ Gambas", "price": NORMALBOX, "image": "resources/img/kitchen/m8.png"},
    {"number": "616","title": "Massa de Udon c/ Gambas", "price": SPECIALBOX, "image": "resources/img/kitchen/616.png"},
    {"number": "C9","title": "Arroz Salteado", "price": RICE, "image": "resources/img/kitchen/615.png"}
]


# Define directory and file paths
directory = "../js"
file_path = os.path.join(directory, "noodlesRice.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)