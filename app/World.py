from Player import Player

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
        for obj in all_objects:
            obj.update()
            #maybe check if player and fire etc

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



    def CheckInWorld(self,position):
        if position.x <0 or position.x > self.width:
            return false
        if position.y <0 or position.y > self.height:
            return false
        return true

    def CheckCollision(self,position):
        #todo add
        return 0

    def Move(player,direction):
        pass
