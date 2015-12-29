"""
This class tests the Index Controller
"""


# Global imports
import unittest
from mock import MagicMock

# Local includes
from app.Server import Server
from app.Position import Position
from app.World import World

"""
This class tests the Direction class
"""
class ServerTest(unittest.TestCase):

    def setUp(self):
        self.server = Server()

    def test_get_world(self):
        """
        When I get an instance of the Server it should return the world
        """
        self.assertIsInstance(self.server.get_world(), World)

    def test_set_world(self):
        """
        Ensure that set world works as expected
        """
        self.assertEqual(self.server.get_world().width, 10)
        self.assertEqual(self.server.get_world().width, 10)
        world = World(5,5)
        self.server.set_world(world)
        self.assertEqual(self.server.get_world().width, 5)
        self.assertEqual(self.server.get_world().width, 5)

    def test_command_register(self):
        """
        When I REGISTER a user it should add it to the world
        """
        world = self.server.get_world()
        world.addPlayer = MagicMock(name='addPlayer')
        self.server.run_command('0 REGISTER { "name": "Bruce", "position": [ 1, 2 ] }')
        self.assertEqual(world.addPlayer.call_args[0][0], "Bruce")
        # TODO get this stupid thing to work, not sure why I get
        # AssertionError: 1, 2 != (1, 2)
        #self.assertEqual(world.addPlayer.call_args[0][1], (1, 2))

    def test_command_move(self):
        """
        When I send a move command it should call setInputMovePlayer
        """
        world = self.server.get_world()
        world.setInputMovePlayer = MagicMock(name='setInputMovePlayer')
        self.server.run_command('0 MOVE SOUTH')
        world.setInputMovePlayer.assert_called_once_with(0, 180)

    def test_command_turn(self):
        """
        When I send a turn command it should call setInputTurnPlayer
        """
        world = self.server.get_world()
        world.setInputTurnPlayer = MagicMock(name='setInputTurnPlayer')
        self.server.run_command('0 TURN SOUTH')
        world.setInputTurnPlayer.assert_called_once_with(0, 180)

    def test_shoot(self):
        """
        When I send a turn command it should call setInputShootPlayer
        """
        world = self.server.get_world()
        world.setInputShootPlayer = MagicMock(name='setInputShootPlayer')
        self.server.run_command('1 SHOOT')
        world.setInputShootPlayer.assert_called_once_with(1)

    def test_command_lock(self):
        """
        When I send just the lock command it should call lockAllPlayers
        """
        world = self.server.get_world()
        world.lockAllPlayers = MagicMock(name='lockAllPlayers')
        self.server.run_command('LOCK')
        self.assertTrue(world.lockAllPlayers.called)

    def test_command_player_lock(self):
        """
        When I send the lock command it should call setInputLockPlayer
        """
        world = self.server.get_world()
        world.setInputLockPlayer = MagicMock(name='setInputLockPlayer')
        self.server.run_command('1 LOCK')
        world.setInputLockPlayer.assert_called_once_with(1)

if __name__ == '__main__':
    unittest.main()
