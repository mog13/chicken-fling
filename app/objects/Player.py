from GameObject import GameObject
from app.Action import Action

class Player(GameObject):
    def __init__(self,name,id):
        super(GameObject, self).__init__()
        self.name = name
        self.direction = 0
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
    def update(self):
        if self.alive == True:
            if self.action is Action.MOVE:
                self.move(1,self.actionData)
            elif self.action is Action.FIRE:
                 self.amunition -=1
                 #fire handled in world
            elif self.action is Action.TURN:
                self.direction = self.actionData

            elif self.action is Action.RELOAD:
                self.reload()

        #reset the action
        self.action == Action.NONE
