favorite_numbers = {
    "Rani": [7, 10, 15],
    "Dimas": [5, 8],
    "Salsa": [3, 12, 20],
    "Jaden": [4, 9],
    "Nadia": [6, 11]
}

for name, numbers in favorite_numbers.items():
    print(f"\nAngka favorit {name}:")

    for number in numbers:
        print(number)