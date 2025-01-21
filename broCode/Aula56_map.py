store = [
    ("shirt", 20),
    ("pants", 25),
    ("jacket", 50),
    ("socks", 10),
]

to_euros = lambda data: (data[0], data[1]*0.82)

store_euros = map(to_euros, store)
store_euros2 = list(map(to_euros, store))
print(store_euros, " --- as an iter")
for item in store_euros:
    print(item)
print()
print(store_euros2, " --- as a list")
for i in store_euros2:
    print(i)
