"""
This class tests the Index Controller
"""


# Global imports
import unittest

# Local includes
from app.Player import Player
from app.GameObject import GameObject
from app.Position import Position
from app.Action import Action

"""
This class tests the ControllerBase by creating a mock from this
Base class
"""
class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player = Player('morgan',0)

    """
    """
    def test_defaults(self):
        self.assertEqual(self.player.name,'morgan')

    """
    When firing it should remove a bullet and reload should replace them
    """
    def test_reload(self):
        self.player.action = Action.FIRE;
        self.player.update();
        self.player.update();
        self.assertEqual(self.player.amunition,8)
        self.player.reload();
        self.assertEqual(self.player.amunition,10)

if __name__ == '__main__':
    unittest.main()