"""
This class tests the Index Controller
"""


# Global imports
import unittest

# Local includes
from app.objects.Player import Player
from app.objects.GameObject import GameObject
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
        self.assertEqual(self.player.get_type(), "player")


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

    def test_lock(self):
        self.assertEqual(self.player.locked,False)
        self.player.lock()
        self.assertEqual(self.player.locked,True)
        self.player.unlock()
        self.assertEqual(self.player.locked,False)

    """
    When I get_data from player it should include the locked data
    """
    def test_to_data(self):
        self.assertEqual(self.player.to_data(),{ "type":"player", "position":[0,0], "direction": 0, "alive": True, "locked":False})

if __name__ == '__main__':
    unittest.main()
