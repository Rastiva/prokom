rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China"
}

print("Informasi sungai:")

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nNama sungai:")

for river in rivers.keys():
    print(river)

print("\nNama negara:")

for country in rivers.values():
    print(country)