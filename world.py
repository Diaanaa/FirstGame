import entity
import room
import random

class World:

    def __init__(self):

        human = entity.Hero()
        fakel = entity.Thing('факел')
        key = entity.Thing('ключ')
        door = entity.Thing('дверь')
        rooms = [0, 1, 2, 3, 4]
        whole = []


        human_position = random.choice(rooms)
        fakel_postition = random.choice(rooms)

        key_position = random.choice(rooms)
        rooms.remove(key_position)

        door_position = random.choice(rooms)
        rooms.remove(door_position)


        for i in rooms:
            whole = room.Room(i)
           






        







