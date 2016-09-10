import itertools

one = [int(x) for x in input().split()]
two = [int(x) for x in input().split()]
three = [int(x) for x in input().split()]
four = [int(x) for x in input().split()]
five = [int(x) for x in input().split()]

test = [one, two, three, four, five]

letters = ['1', '2', '3', '4', '5']

max = 0

for c in itertools.permutations(letters, 5):
    first = test[int(c[0]) - 1][int(c[1]) - 1] + test[int(c[1]) - 1][int(c[0]) - 1] + test[int(c[2]) - 1][
        int(c[3]) - 1] + test[int(c[3]) - 1][int(c[2]) - 1]
    second = test[int(c[1]) - 1][int(c[2]) - 1] + test[int(c[2]) - 1][int(c[1]) - 1] + test[int(c[3]) - 1][
        int(c[4]) - 1] + test[int(c[4]) - 1][int(c[3]) - 1]
    third = test[int(c[2]) - 1][int(c[3]) - 1] + test[int(c[3]) - 1][int(c[2]) - 1]  + test[int(c[4]) - 1][int(c[3]) - 1]+ test[int(c[3]) - 1][int(c[4]) - 1]
    sum = first +second+ third
    #print (sum)
    if sum > max:
        max = sum

print(max)
