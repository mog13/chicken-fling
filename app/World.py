

class World:
    def __init__(self, width,height):
        self.width = width
        self.height = height
        self.players = []
        self.bullets = []

        #Manually add stuff to the map

    #Add a player to the list
    def addPlayer(self,name,position):
        player = Player(name)
        player.position = position
        self.players.append(player)

    def getPlayers(self):
        return self.players
    #Step assumes all updates are possible, this is because they should be parsed/checked when added to the world
    def doStep(self):
        #update all bullets
        for bullet in self.bullets:
            bullet.update()

        #update all players first
        for i in range(len(self.players)):
                self.players[i].update()
                if self.players[i].action is action.FIRE:
                    #If the player has fired then create a bullet with there direction and move it on one, then add to the list
                    newBullet= newBullet(self.players[i].direction,self.players[i].position)
                    newBullet.update()
                    self.bullets.append(newBullet)
                #check to see if the player has hit any bullets
                for bullet in self.bullets:
                    if bullet.position.x is self.players[i].position.x and bullet.position.y is self.players[i].position.y:
                        break;


    def CheckInWorld(self,position):
        if position.x <0 or position.x > self.width:
            return false
        if position.y <0 or position.y > self.height:
            return false
        return true

    def CheckCollision(self,position):
        #todo add
        return 0
