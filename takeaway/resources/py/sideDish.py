import json

#PRICES

NORMALBOX = "7.50€"
SOUP = "2.00€"
SIMPLESALAD = "1.50€"
SALAD = "2.90€"
FRENCHFRIES = "2.50€"



# Define menu items

menu_items = [
  {"number": "C0","title": "Ravilios", "price": NORMALBOX, "image": "resources/img/kitchen/c0.png"},
  {"number": "C1","title": "Gambas Panadas", "price": NORMALBOX, "image": "resources/img/kitchen/c1.png"},
  {"number": "C2","title": "Crepes", "price": NORMALBOX, "image": "resources/img/kitchen/c2.png"},
  {"number": "C4","title": "Frango Grrelhado c/ Molho", "price": NORMALBOX, "image": "resources/img/kitchen/c4.png"},
  {"number": "C5","title": "Tempura de Gambas", "price": NORMALBOX, "image": "resources/img/kitchen/c5.png"},
  {"number": "C6","title": "Espetada de Frango", "price": NORMALBOX, "image": "resources/img/kitchen/c6.png"},
  {"number": "C7","title": "Espetada de Cogumelos Brancos", "price": NORMALBOX, "image": "resources/img/kitchen/c7.png"},
  {"number": "C17","title": "Espetada de Cogumelos Pretos", "price": NORMALBOX, "image": "resources/img/kitchen/c17.png"},
  {"number": "C18","title": "Asas de Frango Frito", "price": NORMALBOX, "image": "resources/img/kitchen/c18.png"},
  {"number": "C19","title": "Lula Frita", "price": NORMALBOX, "image": "resources/img/kitchen/c19.png"},
  {"number": "C20","title": "Batata Frita", "price": FRENCHFRIES, "image": "resources/img/kitchen/c20.png"},
  {"number": "C8","title": "Sopa Miso", "price": SOUP, "image": "resources/img/kitchen/c8.png"},
  {"number": "C10","title": "Salada", "price": SIMPLESALAD, "image": "resources/img/kitchen/c10.png"},
  {"number": "C11","title": "Salada de Frango Frito", "price": SALAD, "image": "resources/img/kitchen/c11.png"}, 
  {"number": "C12","title": "Salada de Gambas Panadas", "price": SALAD, "image": "resources/img/kitchen/c12.png"},
  {"number": "C13","title": "Salada", "price": SALAD, "image": "resources/img/kitchen/c13.png"},
]

file_path = "resources/js/sideDish.json"

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)