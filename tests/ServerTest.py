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
        self.assertEqual(0, len(world.getPlayers()))
        self.server.run_command('0 REGISTER { "name": "Bruce", "position": [ 1, 2 ] }')
        self.assertEqual(1, len(world.getPlayers()))
        self.server.run_command('0 REGISTER { "name": "Bruce", "position": [ 1, 3 ] }')
        self.assertEqual(2, len(world.getPlayers()))


    def test_command_move(self):
        """
        When I send a move command it should change the player's direction
        """
        world = self.server.get_world()
        world.setInputMovePlayer = MagicMock(name='setInputMovePlayer')
        self.server.run_command('0 MOVE SOUTH')
        world.setInputMovePlayer.assert_called_once_with(0, 180)


if __name__ == '__main__':
    unittest.main()
