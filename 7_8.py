pesanan_sandwich = ["tuna", "beef", "ayam", "keju"]

sandwich_selesai = []

while pesanan_sandwich:
    sandwich_sekarang = pesanan_sandwich.pop()

    print(f"Saya sudah membuat sandwich {sandwich_sekarang}.")

    sandwich_selesai.append(sandwich_sekarang)

print("\nDaftar sandwich yang sudah dibuat:")

for sandwich in sandwich_selesai:
    print(sandwich)