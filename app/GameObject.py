
class GameObject(object):

    alive = True

    def __init__(self, position):
        self.position = position

    def move(self,amount,direction):
        if direction == 0:
            self.position.y -= amount
        elif direction == 90:
            self.position.x += amount
        elif  direction == 180:
            self.position.y += amount
        else:
            self.position.x -= amount;

    #do nothing by default on an update
    def update(self):
        pass

    def _is_collision(self,gameObject):
        return self.position.x == gameObject.position.x and self.position.y == gameObject.position.y

    def _on_collision(self, gameObject):
        from Bullet import Bullet
        if isinstance(gameObject,Bullet):
            self.alive = False

    def has_collision(self,gameObject):
        if(self._is_collision(gameObject)):
            self._on_collision(gameObject)
