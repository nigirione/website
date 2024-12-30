import json
import os

#PRICES

BOX203 = "28.50€"
BOX205 = "30.50€"



# Define menu items

menu_items = [
    {"number": "N203","title": "Califórnia e Maki de Salmão, Gunkan de Salmão, Sashimi de Salmão, Atum e Robalo, Nigiri de Salmão, Atum, Robalo e Gambas, Rolo de Ovo com Gambas Panadas e Sushi com Gambas Panadas e Cebola Frita", "price": BOX203, "image": "resources/img/special/203.jpg"},
    {"number": "N205","title": "Dragão, Califórnia e Maki de Salmão, Gunkan de Salmão Defumado, Sashimi de Salmão e Atum, Nigiri de Salmão, Salmão Defumado e Atum, Sushi de Queijo com Salmão e Salmão Defumado", "price": BOX205, "image": "resources/img/special/205.jpg"}

]



# Define directory and file paths
directory = "../js"
file_path = os.path.join(directory, "specialBig.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)



# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)