cities_in_F = {
    "New York": 32,
    "Boston": 75,
    "Los Angeles": 100,
    "Chicago": 50
}

cities_in_C = {key: () for (key, value) in cities_in_F.items()}
print(cities_in_C)

cities_in_C = {key: value for (key, value) in cities_in_F.items() if value >= 60}
print(cities_in_C)

cities_in_C = {key: ("ok" if value == 100 else "fail") for (key, value) in cities_in_F.items() if value >= 60}
print(cities_in_C)


def temp(x):
    if 20 <= x <= 40:
        return "cold"
    elif 41 <= x <= 60:
        return "Ok"
    elif 61 <= x <= 100:
        return "hot"


cities_in_C = {key: temp(value) for (key, value) in cities_in_F.items()}
print(cities_in_C)