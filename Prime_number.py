number = int(input("Enter a number:"))

if number == 1:
    print(number, "is not a prime number")
elif number == 2:
    print(number, "is a prime number")
else:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
        else:
            print(number, "is a prime number")