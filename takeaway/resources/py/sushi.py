import json
import os

#PRICES

NORMALBOX = "8.00€"



# Define menu items

menu_items = [
    {"number": "A1" , "title": "Sashimi Salmão", "price": NORMALBOX, "image": "resources/img/sushi/a1.png"},
    {"number": "A2" ,"title": "Sashimi Misto", "price": NORMALBOX, "image": "resources/img/sushi/a2.png"},
    {"number": "A3" ,"title": "Maki + Califórnia", "price": NORMALBOX, "image": "resources/img/sushi/a3.png"},
    {"number": "A4" ,"title": "Sushi Salmão/ Ovo/ Queijo", "price": NORMALBOX, "image": "resources/img/sushi/a4.png"},
    {"number": "A5" ,"title": "Nigiri Salmão", "price": NORMALBOX, "image": "resources/img/sushi/a5.png"},
    {"number": "A6" ,"title": "Nigiri Gambas", "price": NORMALBOX, "image": "resources/img/sushi/a6.png"},
    {"number": "A7" ,"title": "Nigiri Misto", "price": NORMALBOX, "image": "resources/img/sushi/a7.png"},
    {"number": "A8" ,"title": "Nigiri Salmão + Gambas", "price": NORMALBOX, "image": "resources/img/sushi/a8.png"},
    {"number": "A9" ,"title": "Nigiri Tostado", "price": NORMALBOX, "image": "resources/img/sushi/a9.png"},
    {"number": "A10" ,"title": "Nigiri Salmão + Tostado", "price": NORMALBOX, "image": "resources/img/sushi/a10.png"},
    {"number": "A11" ,"title": "Sushi Misto", "price": NORMALBOX, "image": "resources/img/sushi/a11.png"},
    {"number": "A12" ,"title": "Maki + Nigiri", "price": NORMALBOX, "image": "resources/img/sushi/a12.png"},
    {"number": "A13" ,"title": "Maki Vegetais", "price": NORMALBOX, "image": "resources/img/sushi/a13.png"},
    {"number": "A14" ,"title": "Maki Salmão", "price": NORMALBOX, "image": "resources/img/sushi/a14.png"},
    {"number": "A15" ,"title": "Maki Misto", "price": NORMALBOX, "image": "resources/img/sushi/a15.png"},
    {"number": "A16" ,"title": "Maki Misto", "price": NORMALBOX, "image": "resources/img/sushi/a16.png"},
    {"number": "A17" ,"title": "Califórnia Salmão", "price": NORMALBOX, "image": "resources/img/sushi/a17.png"},
    {"number": "A18" ,"title": "Califórnia Gambas Panadas", "price": NORMALBOX, "image": "resources/img/sushi/a18.png"},
    {"number": "A19" ,"title": "Califórnia c/ovas", "price": NORMALBOX, "image": "resources/img/sushi/a19.png"},
    {"number": "A20" ,"title": "Futo Maki Frito", "price": NORMALBOX, "image": "resources/img/sushi/a20.png"},
    {"number": "A21" ,"title": "Maki Misto", "price": NORMALBOX, "image": "resources/img/sushi/a21.png"},
    {"number": "A22" ,"title": "Temaki + Maki", "price": NORMALBOX, "image": "resources/img/sushi/a22.png"},
    {"number": "A23" ,"title": "Sushi Misto", "price": NORMALBOX, "image": "resources/img/sushi/a23.png"},
    {"number": "A24" ,"title": "Sushi Misto", "price": NORMALBOX, "image": "resources/img/sushi/a24.png"},
    {"number": "A25" ,"title": "Sushi Misto", "price": NORMALBOX, "image": "resources/img/sushi/a25.png"},
    {"number": "A26" ,"title": "Sushi Misto", "price": NORMALBOX, "image": "resources/img/sushi/a26.png"},
    {"number": "A27" ,"title": "Maki Frito", "price": NORMALBOX, "image": "resources/img/sushi/a27.png"},
    {"number": "A28" ,"title": "Califónia Frito", "price": NORMALBOX, "image": "resources/img/sushi/a28.png"},
    {"number": "A29" ,"title": "Maki Frito", "price": NORMALBOX, "image": "resources/img/sushi/a29.png"},
    {"number": "A30" ,"title": "Califórnia Frango Panado", "price": NORMALBOX, "image": "resources/img/sushi/a30.png"},
    {"number": "A31" ,"title": "Califórnia Maki Frito", "price": NORMALBOX, "image": "resources/img/sushi/a31.png"},
    {"number": "A32" ,"title": "Temaki", "price": NORMALBOX, "image": "resources/img/sushi/a32.png"},
    {"number": "A33" ,"title": "Queijo Creme", "price": NORMALBOX, "image": "resources/img/sushi/a33.png"},
    {"number": "A34" ,"title": "Temaki Frito c/ Molho", "price": NORMALBOX, "image": "resources/img/sushi/temakis_frito.jpg"}
]


# Define directory and file paths
directory = "../js"
file_path = os.path.join(directory, "sushi.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)



# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)