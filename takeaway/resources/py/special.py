import json
import os

#PRICES

SPECIALBOX = "8.50€"
VIPBOX = "8.80€"



# Define menu items

menu_items = [
    {"number": "Dragao","title": "Dragão", "price": SPECIALBOX, "image": "resources/img/special/B5.png"},
    {"number": "A40","title": "Donburi de Salmão Defumado com Molho", "price": SPECIALBOX, "image": "resources/img/special/A40.png"},
    {"number": "A41","title": "Donburi de Gambas Panadas com Molho", "price": SPECIALBOX, "image": "resources/img/special/A41.png"},
    {"number": "A42","title": "Donburi de Frango Panado com Molho", "price": SPECIALBOX, "image": "resources/img/special/a42.png"},
    {"number": "N71","title": "Sushi Misto de Gambas Panadas e Salmão", "price": VIPBOX, "image": "resources/img/special/n71.png"},
    {"number": "N72","title": "Sushi Misto de Gambas Panadas e Salmão", "price": VIPBOX, "image": "resources/img/special/n72.png"},
    {"number": "N73","title": "Sushi Misto de Gambas Panadas e Salmão", "price": VIPBOX, "image": "resources/img/special/n73.png"},
    {"number": "N74","title": "Queijo Creme com Salmão e Salmão Defumado", "price": VIPBOX, "image": "resources/img/special/n74.png"},
    {"number": "N75","title": "Sushi Misto de Salmão, Queijo Creme e Frutas", "price": VIPBOX, "image": "resources/img/special/n75.png"},
    {"number": "N76","title": "Sushi Misto de Delícias com Abacate e Morango", "price": VIPBOX, "image": "resources/img/special/n76.png"},
    {"number": "N77","title": "Sushi de Morangos, Rabanete Japonês (vegetariano)", "price": VIPBOX, "image": "resources/img/special/n77.png"},
    {"number": "N78","title": "Sushi de Gambas Panadas e Temaki Salmão", "price": VIPBOX, "image": "resources/img/special/n78.png"},
    {"number": "N79","title": "Sushi Misto de Salmão e Gambas Panadas com Molho", "price": VIPBOX, "image": "resources/img/special/n79.png"},
    {"number": "N80","title": "Sushi de Rabanete Japonês, Gambas Panadas com Molho", "price": VIPBOX, "image": "resources/img/special/n80.png"},
    {"number": "N81","title": "Sushi de Rabanete Japonês e Delícias do Mar", "price": VIPBOX, "image": "resources/img/special/n81.png"},
    {"number": "N82","title": "Sushi de Queijo Creme e Frutas", "price": VIPBOX, "image": "resources/img/special/n82.png"},
    {"number": "N83","title": "Sashimi de Salmão e Maki de Salmão", "price": VIPBOX, "image": "resources/img/special/n83.png"},
    {"number": "N84","title": "Sashimi de Salmão e Califórnia com Ovas", "price": VIPBOX, "image": "resources/img/special/n84.png"},
    {"number": "N85","title": "Dragão + Califórnia Frito", "price": VIPBOX, "image": "resources/img/special/N85.jpg"},
    {"number": "N86","title": "Gunkan c/Ovas + Sushi Misto Salmão", "price": VIPBOX, "image": "resources/img/special/N86.jpg"},
    {"number": "N87","title": "Maki Frito Picante + Sushi de Gambas Panadas", "price": VIPBOX, "image": "resources/img/special/N87.jpg"},
    {"number": "N88","title": "Califórnia Frito c/Molho de Frutas + Califórnia de Salmão Defumado", "price": VIPBOX, "image": "resources/img/special/N88.jpg"},
    {"number": "N89","title": "Sushi de Morangos + Delícias c/Frutas", "price": VIPBOX, "image": "resources/img/special/N89.jpg"}
    

]

# Define directory and file paths
directory = "../js"
file_path = os.path.join(directory, "special.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)



# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)