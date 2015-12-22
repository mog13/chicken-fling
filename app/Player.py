class Player(GameObject):
    def __init__(name):
        self.name = name
        self.direction = Direction.NORTH
        self.amunition = 10
        self.action = Action.NONE;
        self.dead = false;

    def reload(self):
        self.amunition = 10;

    #on update we switch depending on what action we have been given
    def update():
        if self.dead is false
            if self.action is action.MOVE
                move(1,direction)
            else if self.action is action.FIRE

            else if self.action is Action.TURNNORTH
                self.direction = Direction.NORTH
            else if self.action is Action.TURNEAST
                self.direction = Direction.EAST
            else if self.action is Action.TURNSOUTH
                self.direction = Direction.SOUTH
            else if self.action is Action.TURNWEST
                self.direction = Direction.WEST


        #reset the action
        self.action == Action.NONE
