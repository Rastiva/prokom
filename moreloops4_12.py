
# foods.py

# Membuat list makanan favorit sendiri
favorite_foods = ["Nasi Goreng", "Sate Ayam", "Rendang"]

# Menyalin list makanan ke list teman
friend_foods = favorite_foods[:]

# Menambahkan makanan ke masing-masing list
favorite_foods.append("Bakso")
friend_foods.append("Mie Ayam")

# Menampilkan makanan favorit sendiri
print("Makanan favorit saya:")

for food in favorite_foods:
    print(food)

# Menampilkan makanan favorit teman
print("\nMakanan favorit teman saya:")

for food in friend_foods:
    print(food)
