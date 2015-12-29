from Player import Player
from GameObject import GameObject
from Bullet import Bullet
from Position import Position
from Action import Action
from exceptions.InvalidPlayer import InvalidPlayer
from exceptions.InvalidMove import InvalidMove
from exceptions.OutOfAmmo import OutOfAmmo


class World:
    def __init__(self, width,height):
        self.width = width
        self.height = height
        self.players = []
        self.objects = []

    #Add a player to the world
    def addPlayer(self,name,position):
        player = Player(name,len(self.players))
        player.position = position
        self.players.append(player)

    #Add a game object to the world (no players!)
    def addObject(self,gameObject):
        self.objects.append(gameObject)

    #Get a list of all the players
    def getPlayers(self):
        return self.players

    #Step assumes all updates are possible, this is because they should be parsed/checked when added to the world
    def doStep(self):
        #create a list of all Objects including players
        all_objects = self.players + self.objects

        #make any player specific moves that involve changing/polutting the object list
        for player in self.players:
            player.unlock()
            if(player.action == Action.FIRE):
                shotBullet = Bullet(player.direction,Position(player.position.x,player.position.y))
                shotBullet.update();
                self.addObject(shotBullet)

        #iterate over all objects to update
        for obj in all_objects:
            obj.update()
            if self.checkInWorld(obj.position) == False:
                obj.alive = False;

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


        #Reset all actions
        for player in self.players:
            player.action = Action.NONE

    #Check a given position is in the world
    def checkInWorld(self,position):
        if position.x <0 or position.x > self.width:
            return False
        if position.y <0 or position.y > self.height:
            return False
        return True

    #Check there isnt another object ocupying the given space
    def _checkSpaceEmpty(self,position):
        #check that the move would still be in the world
        if self.checkInWorld(position):
                #create a game obj to use for the check
                tempObj = GameObject(position)
                all_objects = self.players + self.objects
                for obj in all_objects:
                    if not isinstance(obj,Bullet):
                        if obj.is_collision(tempObj) == True:
                            return False
                return True
        return False

    def _playerExists(self,player):
        return len(self.players) > player


    #try and set a players action to move
    def setInputMovePlayer(self,player,direction):
        #check the player exists
        if self._playerExists(player):
            checkPos = Position(self.players[player].position.x, self.players[player].position.y)
            checkPos.move_in_dir(direction)

            if self._checkSpaceEmpty(checkPos):
                self.players[player].action = Action.MOVE
                self.players[player].actionData = direction
            else:
                raise InvalidMove("Invalid move Player (" + str(player) + ") in direction " + str(direction))
        else:
            raise InvalidPlayer("Player (" + str(player) + ") not found")
    #try and set a players action to turn
    def setInputTurnPlayer(self,player,direction):
        if self._playerExists(player):
            self.players[player].action = Action.TURN
            self.players[player].actionData = direction
        else:
            raise InvalidPlayer("Player (" + str(player) + ") not found")

    #try and set a players action to shoot
    def setInputShootPlayer(self,player):
        #check the player exists
        if self._playerExists(player):
            #self.addObject(Bullet(self.players[player].direction),self.players[player].position)
            if self.players[player].amunition > 0:
                self.players[player].action = Action.FIRE
            else:
                raise OutOfAmmo('Not enough ammo')
        else:
            raise InvalidPlayer("Player (" + str(player) + ") not found")

    def setInputReloadPlayer(self,player):
        #check the player exists
        if len(self.players) > player:
            self.players[player].action = Action.RELOAD
        else:
            raise InvalidPlayer("Player (" + str(player) + ") not found")

    def setInputLockPlayer(self,player):
        if self._playerExists(player):
            self.players[player].lock()
        else:
            raise InvalidPlayer("Player (" + str(player) + ") not found")

    def setInputUnlockPlayer(self,player):
        if self._playerExists(player):
            self.players[player].unlock()
        else:
            raise InvalidPlayer("Player (" + str(player) + ") not found")

    def lockAllPlayers(self):
        for player in self.players:
            player.lock()

    def allPlayersLocked(self):
        if len(self.players) == False:
            return False

        for player in self.players:
            if player.locked == False:
                return False
        return True

    #world to string draws 2d ASCII map
    def __str__(self):
        #build a map to fill with all the objects
        map = []
        for n in range(self.width*self.height):
            map.append(' - ')
        for obj in self.objects:
            pos = (obj.position.y * self.width) +obj.position.x
            if obj.alive and pos < len(map):
                if isinstance(obj,Bullet):
                    map[pos] = ' B '
                else:
                    map[pos] = ' X '

        for player in self.players:
            if player.alive:
                pos = (player.position.y * self.width) +player.position.x
                if player.direction == 0:
                    map[pos] = ' ^ '
                elif player.direction == 90:
                    map[pos] = ' > '
                elif player.direction == 180:
                    map[pos] = ' v '
                elif player.direction == 270:
                    map[pos] = ' < '
                else:
                    map[pos] = ' P '

        retStr = ''
        for n in range(len(map)):
            if(n%(self.width) == 0):
                retStr += '\n'
            retStr += map[n]

        return retStr

    __repr__ = __str__
