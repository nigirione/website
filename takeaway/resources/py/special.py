import json

#PRICES

SPECIALBOX = "8.00€"
VIPBOX = "8.50€"



# Define menu items

menu_items = [
    {"number": "Dragao","title": "Dragão", "price": SPECIALBOX, "image": "resources/img/special/dragao.png"},
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
    {"number": "N84","title": "Sashimi de Salmão e Califórnia com Ovas", "price": VIPBOX, "image": "resources/img/special/n84.png"}

]

file_path = "resources/js/special.json"

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)