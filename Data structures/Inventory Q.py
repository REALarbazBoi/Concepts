from collections import Counter

i = {
    "apple": 50,
    "mango": 100,
    "banana": 120,
    "orange": 70
}

o = {
    "apple": 10,
    "mango": 12,
    "banana": 15,
    "orange": 5
}

inventory = Counter(i)


def updated_inventory(order):
    inventory.subtract(order)


order = Counter(o)
updated_inventory(order)
print(inventory)
