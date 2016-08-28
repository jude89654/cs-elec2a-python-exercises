number_of_rooms = int(input("PLEASE INPUT NO OF ROOMS: "))

rooms_available = 0

for x in range(1,number_of_rooms+1):
    room_input = input("PLEASE INPUT THE NUMBER OF WHO ALREADY LIVE AND THE CAPACITY FOR ROOM NO. %i: " % x)
    number_of_people_who_already_lived_in_the_room = int(room_input.split()[0])
    room_capacity = int(room_input.split()[1])
    if(room_capacity-number_of_people_who_already_lived_in_the_room)>=2:
        rooms_available += 1

print("ROOMS AVAILABLE: %i" % rooms_available)