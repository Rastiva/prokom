pet_1 = {
    "animal": "Cat",
    "owner": "Rani"
}

pet_2 = {
    "animal": "Dog",
    "owner": "Dimas"
}

pet_3 = {
    "animal": "Rabbit",
    "owner": "Salsa"
}

pet_4 = {
    "animal": "Hamster",
    "owner": "Jaden"
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}")
    print()