import json

#PRICES

BOX203 = "27.50€"
BOX205 = "29.50€"



# Define menu items

menu_items = [
    {"number": "N203","title": "Califórnia e Maki de Salmão, Gunkan de Salmão, Sashimi de Salmão, Atum e Robalo, Nigiri de Salmão, Atum, Robalo e Gambas, Rolo de Ovo com Gambas Panadas e Sushi com Gambas Panadas e Cebola Frita", "price": BOX203, "image": "resources/img/special/n203.png"},
    {"number": "N205","title": "Dragão, Califórnia e Maki de Salmão, Gunkan de Salmão Defumado, Sashimi de Salmão e Atum, Nigiri de Salmão, Salmão Defumado e Atum, Sushi de Queijo com Salmão e Salmão Defumado", "price": BOX205, "image": "resources/img/special/n205.png"}

]

file_path = "resources/js/specialBig.json"

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)