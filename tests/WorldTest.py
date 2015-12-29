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
from app.exceptions.InvalidPlayer import InvalidPlayer
from app.exceptions.InvalidMove import InvalidMove
from app.exceptions.OutOfAmmo import OutOfAmmo


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

    def test_player_exists(self):
        self.world.addPlayer('Morgan',Position())
        self.assertEqual(self.world._playerExists(0),True)
        self.assertEqual(self.world._playerExists(1),False)

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
    """
    When an object occupies a space it should return false when checked with checkSpaceEmpty
    """
    def test_empty_space_function(self):
        self.world.addPlayer('',Position(0,1))
        self.world.addObject(GameObject(Position(1,0)))
        self.assertEqual(self.world._checkSpaceEmpty(Position(0,1)),False)
        self.assertEqual(self.world._checkSpaceEmpty(Position(1,0)),False)
        self.assertEqual(self.world._checkSpaceEmpty(Position(0,0)),True)
    """
    When I set a move it should raise an exception if the player doesnt exist
    """
    def test_exception_if_player_doesnt_exist(self):
        self.world.addPlayer('Morgan',Position(0,1))
        #Shouldnt throw an exception
        self.world.setInputMovePlayer(0,90)
        self.assertRaises(InvalidPlayer,self.world.setInputMovePlayer,1,90)
        self.assertRaises(InvalidPlayer,self.world.setInputTurnPlayer,2,90)
        self.assertRaises(InvalidPlayer,self.world.setInputShootPlayer,3)
        self.assertRaises(InvalidPlayer,self.world.setInputReloadPlayer,4)
    """
    When i set player to move it should set its action only when possible
    """
    def test_move_player(self):
        self.world.addPlayer('',Position(0,1))
        self.world.addObject(GameObject(Position(1,1)))
        #Player should not be able to move due to game object in the way
        self.assertRaises(InvalidMove, self.world.setInputMovePlayer,0,90)
        self.assertEqual(self.world.players[0].action,0)

        self.world.setInputMovePlayer(0,180)
        self.assertEqual(self.world.players[0].action,1)
    """
    When I set player to turn its action is updated
    """
    def test_turn_player(self):
        self.world.addPlayer('',Position(0,1))
        self.world.setInputTurnPlayer(0,180)
        self.assertEqual(self.world.players[0].direction,0)
        self.world.doStep()
        self.assertEqual(self.world.players[0].direction,180)
    """
    When i set a player to reload it should set the correct Action
    """
    def test_reload(self):
        self.world.addPlayer('',Position(0,0))
        self.world.players[0].amunition = 4
        self.world.setInputReloadPlayer(0)
        self.world.doStep()
        self.assertEqual(self.world.players[0].amunition,10)

    """
    When i try and shoot with no ammo an exception should be raised
    """
    def test_out_of_ammo(self):
        self.world.addPlayer('',Position(0,0))
        self.world.players[0].amunition = 0;
        self.assertRaises(OutOfAmmo,self.world.setInputShootPlayer,0)
    """
    I should be able to lock and unlock individual players
    """
    def test_lock(self):
        self.world.addPlayer('tesplayer',Position(0,0))
        self.world.setInputLockPlayer(0)
        self.assertEqual(self.world.players[0].locked,True)
        self.world.setInputUnlockPlayer(0)
        self.assertEqual(self.world.players[0].locked,False)

    """
    I should be able to check all players are locked
    """
    def test_all_unlcoked(self):
        self.assertEqual(self.world.allPlayersLocked(),False)
        self.world.addPlayer('player 1', Position(1,2))
        self.world.addPlayer('player 2', Position(4,2))
        self.world.addPlayer('player 3', Position(0,0))
        self.assertEqual(self.world.allPlayersLocked(),False)
        self.world.players[0].lock()
        self.world.players[1].lock()
        self.assertEqual(self.world.allPlayersLocked(),False)
        self.world.players[2].lock()
        self.assertEqual(self.world.allPlayersLocked(),True)

    """
    I should be able to lock all the players at once
    """
    def test_lock_all_pplayers(self):
        self.assertEqual(self.world.allPlayersLocked(),False)
        self.world.addPlayer('player 1', Position(1,2))
        self.world.addPlayer('player 2', Position(4,2))
        self.world.addPlayer('player 3', Position(0,0))
        self.world.lockAllPlayers()
        self.assertEqual(self.world.allPlayersLocked(),True)

    """
    BOOM MAP!
    """
    def test_draw(self):
        self.world.addPlayer('',Position(2,1))
        self.world.players[0].direction = 180
        self.world.addObject(GameObject(Position(1,3)))
        #print(self.world)
        #print('shooting')
        self.world.setInputShootPlayer(0)
        self.world.doStep()
        #print(self.world)
        #print('turning west')
        self.world.setInputTurnPlayer(0,270)
        self.world.doStep();
        #print('moving player right')
        self.world.setInputMovePlayer(0,90)
        self.world.doStep()
        #print(self.world)
        #print('moving player down')
        self.world.setInputMovePlayer(0,180)
        self.world.doStep()
        #print(self.world)

if __name__ == '__main__':
    unittest.main()
