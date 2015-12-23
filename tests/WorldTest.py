"""
This class tests the Index Controller
"""


# Global imports
import unittest

# Local includes
from app.World import World
from app.Position  import Position
from app.Player import Player
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


if __name__ == '__main__':
    unittest.main()
