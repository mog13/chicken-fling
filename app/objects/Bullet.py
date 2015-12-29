from GameObject import GameObject
from Fire import Fire

class Bullet(GameObject):

    #inherit from game object
    def __init__(self,direction,position):
        super(GameObject, self).__init__()
        self.position = position
        self.direction = direction
        self.type = "bullet"

    #Always move each update
    def update(self,world):
        self.move(1,self.direction)

    def _on_collision(self, gameObject):
        if not isinstance(gameObject,Fire):
            self.alive = False
