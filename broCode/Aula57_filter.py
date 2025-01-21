import numpy

friends = [
    ("Rachel", 19),
    ("Monica", 18),
    ("Phoebe", 17),
    ("Joey", 16),
    ("Chandler", 21),
    ("Ross", 20)
]

filtro = lambda data: data[1] >= 18

adults = list(filter(filtro, friends))

print(adults)
