"""
This class tests the Index Controller
"""


# Global imports
import unittest

# Local includes
from app.Bullet import Bullet
from app.GameObject import GameObject
from app.Position import Position

"""
This class tests the ControllerBase by creating a mock from this
Base class
"""
class BulletTest(unittest.TestCase):

    def setUp(self):
        self.bullet = Bullet(0,Position())

    """
    """
    def test_defaults(self):
        self.assertEqual(self.bullet.position.x,0)
        self.assertEqual(self.bullet.position.y,0)
        self.bullet.update();
        self.bullet.update();
        self.assertEqual(self.bullet.position.x,0)
        self.assertEqual(self.bullet.position.y,-2)


if __name__ == '__main__':
    unittest.main()
