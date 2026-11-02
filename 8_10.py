def kirim_pesan(daftar_pesan, pesan_terkirim):
    while daftar_pesan:
        pesan_sekarang = daftar_pesan.pop()
        print(pesan_sekarang)
        pesan_terkirim.append(pesan_sekarang)


pesan_singkat = [
    "Selamat pagi!",
    "Jangan lupa belajar.",
    "Tetap semangat!",
    "Semoga harimu menyenangkan."
]

pesan_terkirim = []

kirim_pesan(pesan_singkat, pesan_terkirim)

print("\nDaftar pesan awal:")
print(pesan_singkat)

print("\nDaftar pesan terkirim:")
print(pesan_terkirim)