import json
import os

#PRICES

NORMALBOX = "8.00€"
DUCK = "9.95€"



# Define menu items

menu_items = [
  {"number": "B1","title": "Gambas c/ Piripiri", "price": NORMALBOX, "image": "resources/img/kitchen/b1.png"},
  {"number": "B2","title": "Gambas c/ Bambu e Cogumelos", "price": NORMALBOX, "image": "resources/img/kitchen/b2.png"},
  {"number": "B3","title": "Gambas c/ Caril", "price": NORMALBOX, "image": "resources/img/kitchen/b3.png"},
  {"number": "B4","title": "Vaca c/ Bambu e Cogumelos", "price": NORMALBOX, "image": "resources/img/kitchen/b4.png"},
  {"number": "B5","title": "Porco c/ Bambu e Cogumelos", "price": NORMALBOX, "image": "resources/img/kitchen/b5.png"},
  {"number": "B6","title": "Porco com Molho Agridoce", "price": NORMALBOX, "image": "resources/img/kitchen/b6.png"},
  {"number": "B7","title": "Frango c/ Amêndoas", "price": NORMALBOX, "image": "resources/img/kitchen/b7.png"},
  {"number": "B8","title": "Frango c/ Piripiri", "price": NORMALBOX, "image": "resources/img/kitchen/b8.png"},
  {"number": "B9","title": "Frango Frito c/ Amêndoas", "price": NORMALBOX, "image": "resources/img/kitchen/b9.png"},
  {"number": "B11","title": "Vaca c/ Molho de Ostra", "price": NORMALBOX, "image": "resources/img/kitchen/b11.png"},
  {"number": "B12","title": "Frango c/ Caril", "price": NORMALBOX, "image": "resources/img/kitchen/b12.png"},
  {"number": "B13","title": "Vaca c/ Caril", "price": NORMALBOX, "image": "resources/img/kitchen/b13.png"},
  {"number": "610","title": "Pato c/ Molho", "price": DUCK, "image": "resources/img/kitchen/610.png"}
  
]


# Define directory and file paths
directory = "../js"
file_path = os.path.join(directory, "kitchen.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)