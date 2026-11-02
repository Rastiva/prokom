def make_album(nama_artis, judul_album, jumlah_lagu=None):
    album = {
        "artis": nama_artis,
        "album": judul_album
    }

    if jumlah_lagu is not None:
        album["jumlah_lagu"] = jumlah_lagu

    return album


while True:
    print("\nMasukkan informasi album:")
    print("Ketik 'selesai' pada nama artis untuk berhenti.")

    nama_artis = input("Nama artis: ")

    if nama_artis.lower() == "selesai":
        break

    judul_album = input("Judul album: ")

    jumlah_lagu = input("Jumlah lagu (tekan Enter jika tidak diketahui): ")

    if jumlah_lagu:
        album = make_album(nama_artis, judul_album, int(jumlah_lagu))
    else:
        album = make_album(nama_artis, judul_album)

    print(album)


print("\nProgram selesai.")