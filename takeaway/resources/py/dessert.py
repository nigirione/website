import json
import os

#PRICES

NORMALBOX = "8.00€"
BANANA = "4.80€"
PUMKIM = "3.90€"


# Define menu items

menu_items = [
  {"number": "C14","title": "Banana Frita", "price": BANANA, "image": "resources/img/kitchen/c14.png"},
  {"number": "C15","title": "Bolas de Sésamo c/ Doce de Feijão", "price": NORMALBOX, "image": "resources/img/kitchen/F9.jpg"},
  {"number": "C16","title": "Tartes de Abóbora", "price": PUMKIM, "image": "resources/img/kitchen/c16.png"}
]


# Define directory and file paths
directory = "../js"
file_path = os.path.join(directory, "dessert.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)
