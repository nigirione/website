import json

#PRICES

NORMALBOX = "7.50€"
BANANA = "4.80€"
PUMKIM = "3.90€"


# Define menu items

menu_items = [
  {"number": "C14","title": "Banana Frita", "price": BANANA, "image": "resources/img/kitchen/c14.png"},
  {"number": "C15","title": "Bolas de Sésamo c/ Doce de Feijão", "price": NORMALBOX, "image": "resources/img/kitchen/c15.png"},
  {"number": "C16","title": "Tartes de Abóbora", "price": PUMKIM, "image": "resources/img/kitchen/c16.png"}
]


file_path = "resources/js/dessert.json"

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)