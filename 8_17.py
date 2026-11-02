def buat_nama_kota(kota, negara):
    hasil = f"{kota}, {negara}"
    return hasil


print(buat_nama_kota("Jakarta", "Indonesia"))
print(buat_nama_kota("Tokyo", "Jepang"))
print(buat_nama_kota("Paris", "Prancis"))


def buat_album(nama_artis, judul_album, jumlah_lagu=None):
    album = {
        "artis": nama_artis,
        "judul": judul_album
    }

    if jumlah_lagu is not None:
        album["jumlah_lagu"] = jumlah_lagu

    return album


album_1 = buat_album("Taylor Swift", "Midnights")
album_2 = buat_album("Ariana Grande", "Positions")
album_3 = buat_album("Sabrina Carpenter", "Short n' Sweet", 12)

print(album_1)
print(album_2)
print(album_3)



def buat_sandwich(*bahan):
    print("\nSandwich yang dipesan:")

    for item in bahan:
        print(f"- {item}")


buat_sandwich("Keju", "Selada", "Tomat")
buat_sandwich("Daging", "Keju")
buat_sandwich("Telur", "Mayones", "Saus")