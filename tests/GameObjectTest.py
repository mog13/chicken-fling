"""
This class tests the Index Controller
"""


# Global imports
import unittest

# Local includes
from app.GameObject import GameObject
from app.Position import Position


"""
This class tests the ControllerBase by creating a mock from this
Base class
"""
class GameObjectTest(unittest.TestCase):

    def setUp(self):
        self.gameObject = GameObject(Position())

    """
    When I send a request to the controller it should return with a
    response
    """
    def test_defaults(self):
        self.gameObject.move(1,0)
        self.assertEqual(self.gameObject.position.y, -1)
        self.gameObject.move(1,90)
        self.assertEqual(self.gameObject.position.x, 1)
        self.gameObject.move(2,180)
        self.assertEqual(self.gameObject.position.y, 1)
        self.gameObject.move(2,270)
        self.assertEqual(self.gameObject.position.x, -1)


if __name__ == '__main__':
    unittest.main()
