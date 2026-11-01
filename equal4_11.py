
# my_pizzas.py

# Membuat list pizza milik sendiri
pizzas = ["Pizza Keju", "Pizza Pepperoni", "Pizza Ayam"]

# Menyalin list pizzas ke friend_pizzas
friend_pizzas = pizzas[:]

# Menambahkan pizza ke list sendiri
pizzas.append("Pizza Sosis")

# Menambahkan pizza berbeda ke list teman
friend_pizzas.append("Pizza Jamur")

# Menampilkan pizza favorit sendiri
print("Pizza favorit saya adalah:")

for pizza in pizzas:
    print(pizza)

# Menampilkan pizza favorit teman
print("\nPizza favorit teman saya adalah:")

for pizza in friend_pizzas:
    print(pizza)
