
class GameObject(object):

    alive = True

    def __init__(self, position):
        self.position = position

    #Move object in a given direction by a given amount
    def move(self,amount,direction):
        self.position.move_in_dir(direction,amount)


    #do nothing by default on an update
    def update(self):
        pass

    #returns if this object is colliding with the given one
    def is_collision(self,gameObject):
        return self.position.x == gameObject.position.x and self.position.y == gameObject.position.y

    #logic on what to do on collision
    def _on_collision(self, gameObject):
        from Bullet import Bullet
        if isinstance(gameObject,Bullet):
            self.alive = False
    #wraps the two, check for collision, if so perform given collision
    def has_collision(self,gameObject):
        if(self.is_collision(gameObject)):
            self._on_collision(gameObject)
