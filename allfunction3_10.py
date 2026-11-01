
# every_function.py

# Membuat list brand mewah
brands = ["Chanel", "Dior", "Gucci", "Louis Vuitton", "Prada"]

# Mengakses elemen dalam list
print("Brand pertama:", brands[0])
print("Brand terakhir:", brands[-1])

# Mengubah elemen dalam list
brands[0] = "Hermes"
print("\nSetelah mengubah elemen:")
print(brands)

# Menambahkan elemen menggunakan append()
brands.append("Burberry")
print("\nSetelah menggunakan append():")
print(brands)

# Menambahkan elemen menggunakan insert()
brands.insert(1, "Versace")
print("\nSetelah menggunakan insert():")
print(brands)

# Menghapus elemen menggunakan del
del brands[1]
print("\nSetelah menggunakan del:")
print(brands)

# Menghapus elemen menggunakan pop()
removed_brand = brands.pop()
print("\nBrand yang dihapus menggunakan pop():", removed_brand)
print(brands)

# Menghapus elemen berdasarkan nilai menggunakan remove()
brands.remove("Gucci")
print("\nSetelah menggunakan remove():")
print(brands)

# Mengurutkan sementara menggunakan sorted()
print("\nUrutan alfabetis:")
print(sorted(brands))

# Mengurutkan sementara secara terbalik
print("\nUrutan alfabetis terbalik:")
print(sorted(brands, reverse=True))

# Membalik urutan list menggunakan reverse()
brands.reverse()
print("\nSetelah menggunakan reverse():")
print(brands)

# Mengurutkan list menggunakan sort()
brands.sort()
print("\nSetelah menggunakan sort():")
print(brands)

# Mengurutkan list secara terbalik menggunakan sort()
brands.sort(reverse=True)
print("\nSetelah menggunakan sort(reverse=True):")
print(brands)

# Menghitung jumlah elemen menggunakan len()
print("\nJumlah brand:", len(brands))
