pesanan_sandwich = [
    "tuna",
    "pastrami",
    "beef",
    "pastrami",
    "ayam",
    "pastrami",
    "keju"
]

sandwich_selesai = []

print("Maaf, deli kehabisan pastrami.")

while "pastrami" in pesanan_sandwich:
    pesanan_sandwich.remove("pastrami")

while pesanan_sandwich:
    sandwich_sekarang = pesanan_sandwich.pop()

    print(f"Saya sudah membuat sandwich {sandwich_sekarang}.")

    sandwich_selesai.append(sandwich_sekarang)

print("\nDaftar sandwich yang sudah dibuat:")

for sandwich in sandwich_selesai:
    print(sandwich)
    