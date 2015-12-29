"""
This class tests the Index Controller
"""


# Global imports
import unittest

# Local includes
from app.objects.GameObject import GameObject
from app.Position import Position
from app.objects.Bullet import Bullet

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
        self.assertEqual(self.gameObject.direction, 0)

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

    def test_get_type(self):
        self.assertEqual(self.gameObject.get_type(), "unknown")

    """
    I should be able to get data
    """
    def test_to_data(self):
        self.assertEqual(self.gameObject.to_data(),{ "type":"unknown", "position":[0,0], "direction": 0, "alive": True})

if __name__ == '__main__':
    unittest.main()
