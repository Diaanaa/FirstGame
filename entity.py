class Entity:

    def __init__(self, name):
        self.name = name


class Hero(Entity):

    def __init__(self, mainhero):
        self.mainhero = mainhero


class Thing(Entity):

    def __init__(self, name):
        self.thing = name


