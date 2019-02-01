

import random
import room
import entity

class World:

    def __init__(self):

        positions = [0, 1, 2, 3, 4, 5]
            
        vodka_position = random.choice(positions)
        positions.remove(vodka_position)
        cucumber_position = random.choice(positions)
        positions.remove(cucumber_position)
        drinker_position = random.choice(positions)
        positions.remove(drinker_position)
        bad_drinker_position = random.choice(positions)

        rooms = []  
        for i in range(0,6):
            new_room = room.Room(i)

            if i == vodka_position:
                vodka = entity.Entity("водочка", new_room)             
                new_room.objects.update({"водочка" : vodka})

            elif i == cucumber_position:
                cucumber = entity.Entity("закусочка", new_room)                 
                new_room.objects.update({"закусочка" : cucumber})

            elif i == drinker_position:
                drinker = entity.Entity("добрячок Валера", new_room)   
                new_room.objects.update({"добрячок Валера" : drinker})

            elif i == bad_drinker_position:
                bad_drinker = entity.Entity("злой Петрович", new_room)   
                new_room.objects.update({"злой Петрович" : bad_drinker})
            rooms.append(new_room)

        available_rooms = rooms.copy()
        new_room = random.choice(available_rooms)
        available_rooms.remove(new_room)
        labytinth(new_room, available_rooms)
        
        self.rooms = rooms
        self.player = entity.Entity("игрок", new_room)
        self.player.around()

    def play(self, room_number):
        if room_number == -1:
            room_number = self.player.owner.owner.number 
        self.player.go_to(self.rooms[room_number])
        self.player.around()

def labytinth(room, available_rooms):
 
    available_rooms_count = len(available_rooms)
    if room.owner is None:
        start = 1
    elif len(room.owner.ways) == 1 and available_rooms_count > 0:
        start = 1
    else:
        start = 0    
    stop = 5;

    available_ways_count = range(start, stop)
    ways = random.choice(available_ways_count)

    if available_rooms_count < ways:
        ways = available_rooms_count
    if ways != 0:
        for i in range(ways):
            random_room = random.choice(available_rooms)
            random_room.owner = room
            room.ways.append(random_room)
            available_rooms.remove(random_room)
        for way in room.ways:
            labytinth(way, available_rooms) 

