number_of_columns = int(input())

second_input = input().split()

columns =[]

for x in second_input:
    columns.append(int(x))

columns.sort()

string = ""
for x in columns:
    string += str(x)+" "

print(string)