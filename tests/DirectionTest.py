"""
This class tests the Index Controller
"""


# Global imports
import unittest

# Local includes
from app.Direction import Direction


"""
This class tests the Direction class
"""
class DirectionTest(unittest.TestCase):

    """
    When I set a direction in NORTH, EAST, SOUTH and WEST I should expect the
    correct values to be set
    """
    def test_get_direction(self):
        self.assertEqual(Direction.get_degrees("NORTH"), 0)
        self.assertEqual(Direction.get_degrees("EAST"), 90)
        self.assertEqual(Direction.get_degrees("SOUTH"), 180)
        self.assertEqual(Direction.get_degrees("WEST"), 270)

    """
    When I set a direction in UP, DOWN, RIGHT and LEFT I should expect the
    correct values to be set
    """
    def test_get_direction(self):
        self.assertEqual(Direction.get_degrees("UP"), 0)
        self.assertEqual(Direction.get_degrees("RIGHT"), 90)
        self.assertEqual(Direction.get_degrees("DOWN"), 180)
        self.assertEqual(Direction.get_degrees("LEFT"), 270)

if __name__ == '__main__':
    unittest.main()
