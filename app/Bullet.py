class Bullet(GameObject):
    def __init__(self,direction,position):
        self.position = position
        self.direction = direction

    def update(self):
        move(1,self.direction)
