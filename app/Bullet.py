from GameObject import GameObject


class Bullet(GameObject):

    def __init__(self,direction,position):
        super(GameObject, self).__init__()
        self.position = position
        self.direction = direction

    def update(self):
        self.move(1,self.direction)
