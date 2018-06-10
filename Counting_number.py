number = [1, 6, 8, 1, 2, 1, 5, 6]
print(*number)

counting_number = int(input("Enter a number?"))

if counting_number == 1:
    count1 = len([i for i in number if i == 1])
    if count1 == 1:
        print("1 appears 1 time in my list")
    else:
        print("1 appears", count1, "times in my list")
elif counting_number == 2:
    count2 = len([i for i in number if i == 2])
    if count2 == 1:
        print("2 appears 1 time in my list")
    else:
        print("2 appears", count2, "times in my list")
elif counting_number == 5:
    count5 = len([i for i in number if i == 2])
    if count5 == 1:
        print("5 appears 1 time in my list")
    else:
        print("5 appears", count5, "times in my list")
elif counting_number == 6:
    count6 = len([i for i in number if i == 6])
    if count6 == 1:
        print("6 appears 1 time in my list")
        print("6 appears", count6, "times in my list")
elif counting_number == 8:
    count8 = len([i for i in number if i == 8])
    if count8 == 1:
        print("8 appears 1 time in my list")
    print("8 appears", count8, "times in my list")
else:
    print("Ban nhap sai roi")