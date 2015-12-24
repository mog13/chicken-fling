
class GameObject(object):

    alive = True

    def __init__(self, position):
        self.position = position

    def move(self,amount,direction):
        self.position.move_in_dir(direction,amount)
    #do nothing by default on an update
    def update(self):
        pass

    def is_collision(self,gameObject):
        return self.position.x == gameObject.position.x and self.position.y == gameObject.position.y

    def _on_collision(self, gameObject):
        from Bullet import Bullet
        if isinstance(gameObject,Bullet):
            self.alive = False

    def has_collision(self,gameObject):
        if(self.is_collision(gameObject)):
            self._on_collision(gameObject)
