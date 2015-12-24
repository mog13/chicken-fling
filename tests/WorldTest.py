"""
This class tests the Index Controller
"""


# Global imports
import unittest

# Local includes
from app.World import World
from app.Position  import Position
from app.Player import Player
from app.Bullet import Bullet
from app.GameObject import GameObject
"""
This class tests the ControllerBase by creating a mock from this
Base class
"""
class WorldTest(unittest.TestCase):

    def setUp(self):
        self.world = World(5,5)

    """
    A player should be assigned a new ID based of what number player they are
    """
    def test_defaults(self):
        self.assertEqual(self.world.getPlayers(), [])
        self.world.addPlayer('Morgan',Position())
        self.world.players[0].id = 0
        self.world.addPlayer('Shahmir',Position())
        self.world.players[1].id = 1
        self.assertEqual(len(self.world.getPlayers()),2)

    """
    objects overlapping should have there collisions correclty processed on world update
    furthermore any 'dead' objects should be cleaned up
    """
    def test_step(self):
        #create two bullets and a a player in position 0,0... all should die
        self.world.addObject(Bullet(180,Position()))
        self.world.addObject(Bullet(180,Position()))
        self.world.addPlayer('Morgan',Position())
        self.world.players[0].position.y = 1
        self.world.addPlayer('Shahmir',Position())
        self.world.players[1].position.y = 1
        self.world.doStep()
        self.assertEqual(len(self.world.objects),0)
        self.assertEqual(self.world.players[0].alive,False)
        self.assertEqual(self.world.players[1].alive,False)

    def test_step2(self):
        self.world.addObject(Bullet(180,Position(5,2)))
        self.world.addObject(Bullet(90,Position(1,3)))
        #Morgan should live!
        self.world.addPlayer('Morgan',Position())
        #shahmir should die!
        self.world.addPlayer('Shahmir',Position(2,3))
        #Add random object to check there not destoryed by player 0
        self.world.addObject(GameObject(Position()))
        self.world.addObject(GameObject(Position()))
        self.world.doStep()
        self.assertEqual(len(self.world.objects),4)
        self.assertEqual(self.world.players[0].alive,True)
        self.assertEqual(self.world.players[1].alive,False)

    def test_multiple_steps(self):
        self.world.addPlayer('Bruce Wayne',Position())
        self.world.addPlayer('Thomas Wayne',Position(4,1))
        self.world.addPlayer('Martha Wayne',Position(3,1))

        self.world.addObject(Bullet(90,Position(0,1)))
        self.world.doStep()
        self.world.doStep()

        self.assertEqual(self.world.players[0].alive,True)
        self.assertEqual(self.world.players[1].alive,True)
        self.assertEqual(self.world.players[2].alive,True)
        self.world.doStep()
        self.assertEqual(self.world.players[2].alive,False)
        self.world.doStep()
        self.assertEqual(self.world.players[1].alive,False)
        self.assertEqual(self.world.players[0].alive,True)

    def test_empty_space_function(self):
        self.world.addPlayer('',Position(0,1))
        self.world.addObject(GameObject(Position(1,0)))
        self.assertEqual(self.world._checkSpaceEmpty(Position(0,1)),False)
        self.assertEqual(self.world._checkSpaceEmpty(Position(1,0)),False)
        self.assertEqual(self.world._checkSpaceEmpty(Position(0,0)),True)
    def test_move_player(self):
        self.world.addPlayer('',Position(0,1))
        self.world.addObject(GameObject(Position(1,1)))
        self.world.movePlayer(0,90)
        self.assertEqual(self.world.players[0].action,0)

        self.world.movePlayer(0,180)
        self.assertEqual(self.world.players[0].action,1)

    def test_draw(self):
        self.world.addPlayer('',Position(2,1))
        self.world.addObject(GameObject(Position(1,3)))
        print(self.world)
if __name__ == '__main__':
    unittest.main()
