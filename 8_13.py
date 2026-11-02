def build_profile(nama_depan, nama_belakang, **informasi_pengguna):
    informasi_pengguna["nama_depan"] = nama_depan
    informasi_pengguna["nama_belakang"] = nama_belakang

    return informasi_pengguna


profil = build_profile(
    "Rastiva",
    "Putri",
    jurusan="Teknik Industri",
    hobi="Membaca",
    cita_cita="Bekerja di industri FMCG"
)

print(profil)