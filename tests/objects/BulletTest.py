"""
This class tests the Index Controller
"""


# Global imports
import unittest

# Local includes
from app.objects.Bullet import Bullet
from app.objects.GameObject import GameObject
from app.objects.Fire import Fire
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
        self.bullet.update(None);
        self.bullet.update(None);
        self.assertEqual(self.bullet.position.x,0)
        self.assertEqual(self.bullet.position.y,-2)
        self.assertEqual(self.bullet.get_type(), "bullet")

    """
    When a bullet hits fire it shouldnt die
    """
    def test_fire_collision(self):
        self.bullet._on_collision(Fire(Position()))
        self.assertEqual(self.bullet.alive,True)

if __name__ == '__main__':
    unittest.main()
