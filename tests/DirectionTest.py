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
    When I send GET I should just get the values as expected
    """
    def test_get_direction(self):
        self.assertEqual(Direction.get_degrees("NORTH"), 0)
        self.assertEqual(Direction.get_degrees("EAST"), 90)
        self.assertEqual(Direction.get_degrees("SOUTH"), 180)
        self.assertEqual(Direction.get_degrees("WEST"), 270)

if __name__ == '__main__':
    unittest.main()
