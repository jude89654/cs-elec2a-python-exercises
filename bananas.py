user_input = input("please input the starting price of the banana, the pocket money of the soldier, number of bananas")

banana_price = int(user_input.split()[0])

pocket_money = int(user_input.split()[1])

number_of_bananas = int(user_input.split()[2])

total_price = 0

for x in range(number_of_bananas + 1):
    total_price += (x * banana_price)

money_to_borrow = total_price - pocket_money

if money_to_borrow <= 0:
    money_to_borrow = 0

print("MONEY TO BORROW: %i" % money_to_borrow)
