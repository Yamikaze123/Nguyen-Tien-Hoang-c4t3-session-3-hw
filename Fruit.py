prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

print()
print("Fruits' price and stock information:")
print()

for price in prices:
    print(price)
    print("price:", prices[price])
    print("stock:", stock[price])
    print()

print()

print("Money made:")
print()

total = 0

for price in prices:
    print(price, end=": ")
    multi = prices[price] * stock[price]
    print(int(multi))
    total = total + multi

print()

print("Total:", total)
