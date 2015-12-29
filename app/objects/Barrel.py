from GameObject import GameObject
from Fire import Fire
from Bullet import Bullet
from app.Position import Position

class Barrel(GameObject):

    #inherit from game object
    def __init__(self,position):
        super(GameObject, self).__init__()

        self.position = position
        self.type = "barrel"
        self.explode = False

    #Always move each update
    def update(self,world):
        if(self.explode):
            self.alive = False
            world.addObject(Fire(Position(self.position.x,self.position.y)))
            world.addObject(Fire(Position(self.position.x-1,self.position.y-1)))
            world.addObject(Fire(Position(self.position.x,self.position.y-1)))
            world.addObject(Fire(Position(self.position.x+1,self.position.y-1)))
            world.addObject(Fire(Position(self.position.x+1,self.position.y)))
            world.addObject(Fire(Position(self.position.x+1,self.position.y+1)))
            world.addObject(Fire(Position(self.position.x,self.position.y+1)))
            world.addObject(Fire(Position(self.position.x-1,self.position.y+1)))
            world.addObject(Fire(Position(self.position.x-1,self.position.y)))


    def _on_collision(self, gameObject):
        if isinstance(gameObject,Bullet):
            self.explode = True

    def to_data(self):
        data = super(Barrel,self).to_data()
        data["explode"] = self.explode
        return data
