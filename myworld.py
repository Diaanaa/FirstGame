import entity
import room
import random

class World:

    def __init__(self):

        human = entity.Hero('kek')
        vodka = entity.Thing('водочка')
        cucumber = entity.Thing('закусочка')
        good_drinker = entity.Drinker('добрячок Валера')
        bad_drinker = entity.Drinker('злой Петрович')
        things = []

        number_of_rooms = [0, 1, 2, 3, 4]
        other_number_of_rooms = [0, 1, 2, 3, 4]

        vodka_position = random.choice(number_of_rooms)
        number_of_rooms.remove(vodka_position)
        cucumber_position = random.choice(number_of_rooms)
        number_of_rooms.remove(cucumber_position)
        bad_drinker_position = random.choice(number_of_rooms)
        number_of_rooms.remove(bad_drinker_position)
        human_position = random.choice(number_of_rooms)
        good_drinker_position = random.choice(other_number_of_rooms)
               
        rooms =[]
        for i in number_of_rooms:
            new_room = room.Room(i)
            if i == vodka_position:
                new_room.in_room.update({'водочка' : vodka})

            if i == cucumber_position:
                new_room.in_room.update({'закусочка' : cucumber})

            if i == good_drinker_position and vodka_position:
                new_room.in_room.update({'водочка' : vodka, 'добрячок Валера' : good_drinker})

            if i == good_drinker_position and cucumber_position:
                new_room.in_room.update({'закусочка' : cucumber, 'добрячок Валера' : good_drinker})

            if i == good_drinker_position:
                new_room.in_room.update({'добрячок Валера' : good_drinker})
        rooms.append(new_room)
        
        self.room = rooms


        def labyrinth(room, available_rooms):
            number_of_available_rooms = len(available_rooms)
            if human is None:
                start = 1
            else:
                start = 0

            if 'bad_drinker' in room.in_room:
                stop = 2
            else:
                stop = 3

            number_of_available_rooms = range(start, stop)
            ways = random.choice(number_of_available_rooms)

            #if number_of_available_rooms < ways:
                #ways = number_of_available_rooms

            if ways != 0:
                for i in range(ways):
                    random_room = random.choice(available_rooms)
                    room.ways.append(random_room)
                    available_rooms.remove(random_room)

                for way in room.ways:
                    labyrinth(way, available_rooms)

        available_rooms = rooms.copy()
        new_room = random.choice(available_rooms)
        labyrinth(new_room, available_rooms)












        self.rooms = rooms
        self.player = human_position


 

            


        







