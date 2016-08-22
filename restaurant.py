type_of_restaurant = int(input('type of restaurant [1] diner [2] good restaurant [3] fancy restaurant:'))

cost_of_meal=float(input("please input cost of meal:"))

party_size=int(input('please input party size [1] 1-5 [2] 6-10 [3] more than 10:'))

service_rating=int(input('[1] poor, [2] good, [3] Excellent:'))

base_tip_percentage=0.0

if(type_of_restaurant==1):
    base_tip_percentage=.12
elif(type_of_restaurant==2):
    base_tip_percentage=.15
elif(type_of_restaurant==3):
    base_tip_percentage=.20

if(party_size==2):
    base_tip_percentage+= .03
elif(party_size==3):
    base_tip_percentage+=.05

if(service_rating==1):
    base_tip_percentage-=.02
elif(service_rating==3):
    base_tip_percentage+=.02

print('tip percentage %.2f'% base_tip_percentage)

tip = (base_tip_percentage) *(cost_of_meal)

print('tip: %.2f'%tipS)
