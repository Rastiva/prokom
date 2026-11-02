def buat_mobil(pabrikan, model, **informasi_tambahan):
    mobil = {
        "pabrikan": pabrikan,
        "model": model
    }

    for kunci, nilai in informasi_tambahan.items():
        mobil[kunci] = nilai

    return mobil


mobil = buat_mobil(
    "Subaru",
    "Outback",
    warna="Biru",
    paket_towing=True
)

print(mobil)