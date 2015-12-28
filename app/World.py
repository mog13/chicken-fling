from Player import Player
from GameObject import GameObject
from Bullet import Bullet
from Position import Position
from Action import Action
class World:
    def __init__(self, width,height):
        self.width = width
        self.height = height
        self.players = []
        self.objects = []

    #Add a player to the list
    def addPlayer(self,name,position):
        player = Player(name,len(self.players))
        player.position = position
        self.players.append(player)


    def addObject(self,gameObject):
        self.objects.append(gameObject)

    def getPlayers(self):
        return self.players
    #Step assumes all updates are possible, this is because they should be parsed/checked when added to the world
    def doStep(self):
        #create a list of all Objects including players
        all_objects = self.players + self.objects
        #iterate over all objects to update

        for player in self.players:
            if(player.action == Action.FIRE):
                shotBullet = Bullet(player.direction,Position(player.position.x,player.position.y))
                shotBullet.update();
                self.addObject(shotBullet)


        for obj in all_objects:
            obj.update()
            if self.checkInWorld(obj.position) == False:
                obj.alive = False;
            #due to wolrd manipulation fireing functionality is here.

            # if isinstance(obj,Player):
            #     if(obj.action == Action.FIRE):
            #         bulletPos = Position(obj.position.x,obj.position.y)
            #         self.addObject(Bullet(270,bulletPos))


        #do collision check with all
        for i in range(len(all_objects)):
            for ii in range(len(all_objects)):
            #skip itself
                if ii != i:
                    all_objects[i].has_collision(all_objects[ii])


        #remove any objects that are now considered dead
        #NOTE this does not include players!
        deadIndexs= []
        for n in range(len(self.objects)):
            if self.objects[n].alive == False:
                deadIndexs.append(self.objects[n])

        for n in range(len(deadIndexs)):
            self.objects.remove(deadIndexs[n])


        # #If the player has fired then create a bullet with there direction and move it on one, then add to the list
        #  newBullet= newBullet(self.players[i].direction,self.players[i].position)
        #  newBullet.update()
        #  self.bullets.append(newBullet)



    def checkInWorld(self,position):
        if position.x <0 or position.x > self.width:
            return False
        if position.y <0 or position.y > self.height:
            return False
        return True

    def _checkSpaceEmpty(self,position):
        #check that the move would still be in the world
        if self.checkInWorld(position):
                #create a game obj to use for the check
                tempObj = GameObject(position)
                all_objects = self.players + self.objects
                for obj in all_objects:
                    if obj.is_collision(tempObj) == True:
                        return False
                return True
        return False


    def movePlayer(self,player,direction):
        #check the player exists
        if len(self.players) > player:
            checkPos = Position(self.players[player].position.x, self.players[player].position.y)
            checkPos.move_in_dir(direction)

            if self._checkSpaceEmpty(checkPos):
                self.players[player].action = Action.MOVE
                self.players[player].actionData = direction
            else:
                raise Exception('Invalid move')

    def turnPlayer(self,player,direction):
        if len(self.players) > player:
            self.players[player].action = Action.TURN
            self.players[player].actionData = direction


    def shootPlayer(self,player):
        #check the player exists
        if len(self.players) > player:
            #self.addObject(Bullet(self.players[player].direction),self.players[player].position)
            if self.players[player].amunition > 0:
                self.players[player].action = Action.FIRE

    def __str__(self):
        #build a map to fill with all the objects
        map = []
        for n in range(self.width*self.height):
            map.append('[ ]')
        for obj in self.objects:
            pos = (obj.position.y * self.width) +obj.position.x
            if isinstance(obj,Bullet):
                map[pos] = '[B]'
            else:
                map[pos] = '[X]'

        for player in self.players:
            pos = (player.position.y * self.width) +player.position.x
            map[pos] = '[P]'

        retStr = ''
        for n in range(len(map)):
            if(n%(self.width) == 0):
                retStr += '\n'
            retStr += map[n]

        return retStr

    __repr__ = __str__
