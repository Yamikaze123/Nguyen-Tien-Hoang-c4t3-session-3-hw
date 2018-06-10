
string = input("String: ").lower()
letters = {}

alphabet = "abcdefghijklmnopqrstuvwxyz"

for char in string:
    if char in alphabet:
        if char in letters:
            letters[char] = letters[char] + 1
        else:
            letters[char] = 1

for char in sorted(letters):
    print(char, letters[char])