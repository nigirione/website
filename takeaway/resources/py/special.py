import json
import os

#PRICES

SPECIALBOX = "8.50€"
VIPBOX = "8.80€"



# Define menu items

menu_items = [
    {"number": "Dragao","title": "Dragão", "price": SPECIALBOX, "image": "resources/img/special/B5.png"},
    {"number": "A40","title": "Donburi de Salmão Defumado com Molho", "price": SPECIALBOX, "image": "resources/img/special/A40.jpg"},
    {"number": "A41","title": "Donburi de Gambas Panadas com Molho", "price": SPECIALBOX, "image": "resources/img/special/A41.jpg"},
    {"number": "A42","title": "Donburi de Frango Panado com Molho", "price": SPECIALBOX, "image": "resources/img/special/A42.jpg"},
    {"number": "N71","title": "Sushi Misto de Gambas Panadas e Salmão", "price": VIPBOX, "image": "resources/img/special/N71.jpg"},
    {"number": "N72","title": "Sushi Misto de Gambas Panadas e Salmão", "price": VIPBOX, "image": "resources/img/special/N72.jpg"},
    {"number": "N73","title": "Sushi Misto de Gambas Panadas e Salmão", "price": VIPBOX, "image": "resources/img/special/N73.jpg"},
    {"number": "N74","title": "Queijo Creme com Salmão e Salmão Defumado", "price": VIPBOX, "image": "resources/img/special/N74.jpg"},
    {"number": "N75","title": "Sushi Misto de Salmão, Queijo Creme e Frutas", "price": VIPBOX, "image": "resources/img/special/N75.jpg"},
    {"number": "N76","title": "Sushi Misto de Delícias com Abacate e Morango", "price": VIPBOX, "image": "resources/img/special/N76.jpg"},
    {"number": "N77","title": "Sushi de Morangos, Rabanete Japonês (vegetariano)", "price": VIPBOX, "image": "resources/img/special/N77.jpg"},
    {"number": "N78","title": "Sushi de Gambas Panadas e Temaki Salmão", "price": VIPBOX, "image": "resources/img/special/N78.jpg"},
    {"number": "N79","title": "Sushi Misto de Salmão e Gambas Panadas com Molho", "price": VIPBOX, "image": "resources/img/special/N79.jpg"},
    {"number": "N80","title": "Sushi de Rabanete Japonês, Gambas Panadas com Molho", "price": VIPBOX, "image": "resources/img/special/N80.jpg"},
    {"number": "N81","title": "Sushi de Rabanete Japonês e Delícias do Mar", "price": VIPBOX, "image": "resources/img/special/N81.jpg"},
    {"number": "N82","title": "Sushi de Queijo Creme e Frutas", "price": VIPBOX, "image": "resources/img/special/N82.jpg"},
    {"number": "N83","title": "Sashimi de Salmão e Maki de Salmão", "price": VIPBOX, "image": "resources/img/special/N83.jpg"},
    {"number": "N84","title": "Sashimi de Salmão e Califórnia com Ovas", "price": VIPBOX, "image": "resources/img/special/N84.jpg"},
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