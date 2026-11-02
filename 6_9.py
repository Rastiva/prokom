favorite_places = {
    "Rani": ["Bali", "Japan", "Switzerland"],
    "Dimas": ["Bandung", "Yogyakarta"],
    "Salsa": ["Paris"]
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name}:")

    for place in places:
        print(f"- {place}")