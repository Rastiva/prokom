
# more_conditional_tests.py

# 1. Equality and inequality with strings
brand = "Chanel"

print("1. Apakah brand == 'Chanel'? Prediksi: True.")
print(brand == "Chanel")

print("\n2. Apakah brand != 'Chanel'? Prediksi: False.")
print(brand != "Chanel")


# 2. Tests using the lower() method
name = "RASTIVA"

print("\n3. Apakah name.lower() == 'rastiva'? Prediksi: True.")
print(name.lower() == "rastiva")

print("\n4. Apakah name.lower() == 'Rastiva'? Prediksi: False.")
print(name.lower() == "Rastiva")


# 3. Numerical tests
age = 20

print("\n5. Apakah age == 20? Prediksi: True.")
print(age == 20)

print("\n6. Apakah age != 20? Prediksi: False.")
print(age != 20)

print("\n7. Apakah age > 18? Prediksi: True.")
print(age > 18)

print("\n8. Apakah age > 25? Prediksi: False.")
print(age > 25)

print("\n9. Apakah age < 25? Prediksi: True.")
print(age < 25)

print("\n10. Apakah age < 18? Prediksi: False.")
print(age < 18)

print("\n11. Apakah age >= 20? Prediksi: True.")
print(age >= 20)

print("\n12. Apakah age >= 25? Prediksi: False.")
print(age >= 25)

print("\n13. Apakah age <= 20? Prediksi: True.")
print(age <= 20)

print("\n14. Apakah age <= 18? Prediksi: False.")
print(age <= 18)


# 4. Tests using and keyword
print("\n15. Apakah age > 18 and age < 25? Prediksi: True.")
print(age > 18 and age < 25)

print("\n16. Apakah age > 25 and age < 30? Prediksi: False.")
print(age > 25 and age < 30)


# 5. Tests using or keyword
print("\n17. Apakah age < 18 or age == 20? Prediksi: True.")
print(age < 18 or age == 20)

print("\n18. Apakah age < 18 or age > 25? Prediksi: False.")
print(age < 18 or age > 25)


# 6. Tests using in
favorite_foods = ["Pizza", "Sushi", "Rendang"]

print("\n19. Apakah 'Pizza' ada dalam list? Prediksi: True.")
print("Pizza" in favorite_foods)

print("\n20. Apakah 'Burger' ada dalam list? Prediksi: False.")
print("Burger" in favorite_foods)


# 7. Tests using not in
print("\n21. Apakah 'Burger' tidak ada dalam list? Prediksi: True.")
print("Burger" not in favorite_foods)

print("\n22. Apakah 'Sushi' tidak ada dalam list? Prediksi: False.")
print("Sushi" not in favorite_foods)
