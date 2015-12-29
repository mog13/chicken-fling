from GameObject import GameObject


class Bullet(GameObject):

    #inherit from game object
    def __init__(self,direction,position):
        super(GameObject, self).__init__()
        #I dont know why i cant delete this :(?!
        self.position = position
        self.direction = direction

    #Always move each update
    def update(self):
        self.move(1,self.direction)

    def _on_collision(self, gameObject):
        self.alive = False
