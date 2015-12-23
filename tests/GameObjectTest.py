"""
This class tests the Index Controller
"""


# Global imports
import unittest

# Local includes
from app.GameObject import GameObject
from app.Position import Position
from app.Bullet import Bullet

"""
This class tests the ControllerBase by creating a mock from this
Base class
"""
class GameObjectTest(unittest.TestCase):

    def setUp(self):
        self.gameObject = GameObject(Position())


    def test_defaults(self):
        self.gameObject.move(1,0)
        self.assertEqual(self.gameObject.position.y, -1)
        self.gameObject.move(1,90)
        self.assertEqual(self.gameObject.position.x, 1)
        self.gameObject.move(2,180)
        self.assertEqual(self.gameObject.position.y, 1)
        self.gameObject.move(2,270)
        self.assertEqual(self.gameObject.position.x, -1)

    """
    When collided with a bullet a game object shoudl by default die
    """
    def test_collision(self):
        bullet = Bullet(0,Position())
        self.gameObject.has_collision(bullet)
        self.assertEqual(self.gameObject.alive,False)

    def test_no_collision(self):
        bullet = Bullet(0,Position())
        bullet.position.x +=2
        self.gameObject.has_collision(bullet)
        self.assertEqual(self.gameObject.alive,True)

if __name__ == '__main__':
    unittest.main()
