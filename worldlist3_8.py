
# seeing_the_world.py

places = ["Korea", "Swiss", "Korea Selatan", "Italia", "China"]

# Menampilkan list dalam urutan awal
print("Original list:")
print(places)

# Menampilkan list berdasarkan urutan alfabetis tanpa mengubah list asli
print("\nAlphabetical order:")
print(sorted(places))

# Membuktikan bahwa list asli tidak berubah
print("\nOriginal list:")
print(places)

# Menampilkan list berdasarkan urutan alfabetis terbalik
print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))

# Membuktikan bahwa list asli masih tidak berubah
print("\nOriginal list:")
print(places)

# Membalik urutan list
places.reverse()
print("\nReverse the list:")
print(places)

# Mengembalikan list ke urutan awal
places.reverse()
print("\nReverse the list again:")
print(places)

# Mengurutkan list secara alfabetis
places.sort()
print("\nSort the list alphabetically:")
print(places)

# Mengurutkan list secara alfabetis terbalik
places.sort(reverse=True)
print("\nSort the list in reverse alphabetical order:")
print(places)
