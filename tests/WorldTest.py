"""
This class tests the Index Controller
"""


# Global imports
import unittest

# Local includes
from app.World import World


"""
This class tests the ControllerBase by creating a mock from this
Base class
"""
class WorldTest(unittest.TestCase):

    def setUp(self):
        self.world = World(5,5)

    """
    When I send a request to the controller it should return with a
    response
    """
    def test_defaults(self):
        self.assertEqual(self.world.getPlayers(), [])


if __name__ == '__main__':
    unittest.main()
