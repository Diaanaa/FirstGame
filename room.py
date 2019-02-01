class Room:

    def __init__(self, number):

        self.number = number
        self.owner = None
        self.objects = {}
        self.ways = []
        
       