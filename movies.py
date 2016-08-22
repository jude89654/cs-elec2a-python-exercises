age = int(input('Enter age: '))
print('WITH PARENT?\n[1]yes\n[2]no')

with_parent = int(input('enter answer: '))

print('Movie cost:\n[1]$7.50\n[2]10.50: ')

movie_cost = int(input('enter movie cost: '))

rating =""
type_of_ticket =""

if(age<13):
    rating = "G"
    if(with_parent==1):
        rating+=", PG"
elif(age>=13 and age<16):
    rating="G, PG"
    if(with_parent==1):
        rating+=(', R')
elif(age>16):
    rating = 'G, PG, R'

if(movie_cost==1):
    type_of_ticket="matinee"
elif(movie_cost==2):
    type_of_ticket=="evening"

print("Movie Rating:" + type_of_ticket + ", "+rating)

