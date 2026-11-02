jawaban = {}

polling_aktif = True

while polling_aktif:
    nama = input("\nSiapa nama kamu? ")

    tempat = input(
        "Jika kamu bisa mengunjungi satu tempat di dunia, "
        "ke mana kamu akan pergi? "
    )

    jawaban[nama] = tempat

    ulangi = input("Apakah orang lain ingin ikut menjawab? (ya/tidak) ")

    if ulangi == "tidak":
        polling_aktif = False

print("\n--- HASIL POLLING ---")

for nama, tempat in jawaban.items():
    print(f"{nama} ingin mengunjungi {tempat}.")
    