def buat_sandwich(*bahan):
    print("\nSandwich yang dipesan:")

    for item in bahan:
        print(f"- {item}")


buat_sandwich("Keju", "Selada", "Tomat")
buat_sandwich("Daging", "Keju")
buat_sandwich("Telur", "Mayones", "Selada", "Tomat", "Saus")