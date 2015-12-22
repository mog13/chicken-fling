"""
This class tests the Index Controller
"""


# Global imports
import unittest

# Local includes
from app.Command import Command


"""
This class tests the ControllerBase by creating a mock from this
Base class
"""
class CommandTest(unittest.TestCase):

    def setUp(self):
        self.command = Command()

    """
    When I send GET I should just get the values as expected
    """
    def test_get(self):
        self.assertEqual(self.command.process("1 GET"), (1, "GET", None))

    """
    When I Move east I should get 90 degrees back
    """
    def test_move(self):
        self.assertEqual(self.command.process("1 MOVE EAST"), (1, "MOVE", 90))

        """
    def test_lock(self):
        self.assertEqual(self.command.process("1 LOCK"), (1, "LOCK", None))

    def test_unlock(self):
        self.assertEqual(self.command.process("1 UNLOCK"), (1, "UNLOCK", None))
        """




if __name__ == '__main__':
    unittest.main()
