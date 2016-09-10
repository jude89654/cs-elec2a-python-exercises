a, b, number_of_steps = [int(x) for x in input().split()]

if (abs(a) + abs(b)) < number_of_steps:
    if ((number_of_steps-(a+b)) % 2) == 0:
        print("Yes")
    else:
        print("No")
elif (abs(a) + abs(b)) == number_of_steps:
    print("Yes")
else:
    print("No")
