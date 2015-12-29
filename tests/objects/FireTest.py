# Global imports
import unittest

# Local includes
from app.objects.GameObject import GameObject
from app.objects.Fire import Fire
from app.Position import Position

"""
This class tests the ControllerBase by creating a mock from this
Base class
"""
class FireTest(unittest.TestCase):

    def setUp(self):
        self.fire = Fire(Position())

    """
    """
    def test_defaults(self):
        self.assertEqual(self.fire.type,"fire")
        self.assertEqual(self.fire.life,3)

    """
    Fire should lose life each update and eventually die
    """
    def test_update(self):
        self.fire.update(None)
        self.assertEqual(self.fire.life,2)
        self.fire.update(None)
        self.fire.update(None)
        self.assertEqual(self.fire.alive,False)


if __name__ == '__main__':
    unittest.main()
