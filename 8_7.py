def make_album(nama_artis, judul_album, jumlah_lagu=None):
    album = {
        "artis": nama_artis,
        "album": judul_album
    }

    if jumlah_lagu is not None:
        album["jumlah_lagu"] = jumlah_lagu

    return album


album_1 = make_album("Taylor Swift", "Midnights")
album_2 = make_album("Ariana Grande", "Positions")
album_3 = make_album("Seventeen", "cxm")
album_4 = make_album("Sabrina Carpenter", "Short n' Sweet", 12)

print(album_1)
print(album_2)
print(album_3)
print(album_4)