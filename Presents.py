number_of_friends = int(input())

temp = {}

friend_numbers = [int(x) for x in input().split()]

for x in range(1,number_of_friends+1):
    temp[str(x)] = friend_numbers[x-1]


#print(temp)

string=""
for x in range(number_of_friends):
    string += list(temp.keys())[list(temp.values()).index(x+1)] +" "

print(string)
