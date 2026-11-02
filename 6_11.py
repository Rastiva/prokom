cities = {
    "Jakarta": {
        "country": "Indonesia",
        "population": "Approximately 10.7 million",
        "fact": "Jakarta is the capital of Indonesia."
    },

    "Tokyo": {
        "country": "Japan",
        "population": "Approximately 14 million",
        "fact": "Tokyo is famous for its advanced technology."
    },

    "Paris": {
        "country": "France",
        "population": "Approximately 2.1 million",
        "fact": "Paris is famous for the Eiffel Tower."
    }
}

for city, information in cities.items():
    print(f"\nCity: {city}")
    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")