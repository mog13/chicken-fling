from GameObject import GameObject


class Fire(GameObject):

    #inherit from game object
    def __init__(self,position):
        super(GameObject, self).__init__()
        self.position = position
        self.type = "fire"
        self.life = 3;

    #Always move each update
    def update(self,world):
        self.life -=1;
        if(self.life <=0):
            self.alive = False

    def _on_collision(self, gameObject):
        pass
