def buat_baju(ukuran, tulisan):
    print(f"Baju berukuran {ukuran} dengan tulisan '{tulisan}'.")

# Memanggil fungsi menggunakan positional arguments
buat_baju("L", "Saya suka Python")

# Memanggil fungsi menggunakan keyword arguments
buat_baju(ukuran="XL", tulisan="saya suka kalkulus")