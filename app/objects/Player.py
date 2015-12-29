from GameObject import GameObject
from Bullet import Bullet
from app.Position import Position
from app.Action import Action

class Player(GameObject):
    def __init__(self,name,id):
        super(GameObject, self).__init__()
        self.name = name
        self.amunition = 10
        self.action = Action.NONE
        self.actionData = 0
        self.id = id
        self.locked = False
        self.type = "player"

    #reset amunition to 10
    def reload(self):
        self.amunition = 10

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False
    #on update we switch depending on what action we have been given
    def update(self,world):
        self.unlock()

        if self.alive == True:
            if self.action is Action.MOVE:
                self.move(1,self.actionData)
            elif self.action is Action.FIRE:
                 self.amunition -=1
                 shotBullet = Bullet(self.direction,Position(self.position.x,self.position.y))
                 shotBullet.update(world);
                 world.addObject(shotBullet)

            elif self.action is Action.TURN:
                self.direction = self.actionData

            elif self.action is Action.RELOAD:
                self.reload()
        else:
            self.colideable = False
        #reset the action
        self.action == Action.NONE

    def to_data(self):
        data = super(Player,self).to_data()
        data['locked'] = self.locked
        return data
