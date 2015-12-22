

class GameObject:

    def __init__(self, position):
        self.position = position

    def move(self,amount,direction):

        if direction == 0:
            self.position.y = -1
        elif direction == 90:
            self.position.x = 1
        elif  direction == 180:
            self.position.y = 1
        else:
            self.position.x = -1;

    #do nothing by default on an update
    def update(self):
        pass
