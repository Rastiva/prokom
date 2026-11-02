person_1 = {
    "first_name": "Rani",
    "last_name": "Putri",
    "age": 20,
    "city": "Jakarta"
}

person_2 = {
    "first_name": "Dimas",
    "last_name": "Pratama",
    "age": 21,
    "city": "Bandung"
}

person_3 = {
    "first_name": "Salsa",
    "last_name": "Aulia",
    "age": 19,
    "city": "Surabaya"
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"Nama depan: {person['first_name']}")
    print(f"Nama belakang: {person['last_name']}")
    print(f"Usia: {person['age']}")
    print(f"Kota: {person['city']}")
    print()