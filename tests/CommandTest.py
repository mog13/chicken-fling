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

    def test_default_commands_with_no_data(self):
        """
        When I send GET I should just get the values as expected
        """
        self.assertEqual(self.command.process("1 GET"), (1, "GET", None))
        self.assertEqual(self.command.process("1 LOCK"), (1, "LOCK", None))
        self.assertEqual(self.command.process("1 UNLOCK"), (1, "UNLOCK", None))
        self.assertEqual(self.command.process("LOCK"), (None, "LOCK", None))
        self.assertEqual(self.command.process("PRINT"), (None, "PRINT", None))


    def test_trim(self):
        """
        When my command has next lines, ensure that it is trimed

        Found this because the server will send a \n in the command causing it
        to not pick up the right value for method
        """
        self.assertEqual(self.command.process("1 MOVE SOUTH\n"), (1, "MOVE", 180))


    def test_move(self):
        """
        When I Move east I should get 90 degrees back
        """
        self.assertEqual(self.command.process("1 MOVE EAST"), (1, "MOVE", 90))

    def test_turn(self):
        """
        When I Turn east I should get 90 degrees back
        """
        self.assertEqual(self.command.process("1 TURN EAST"), (1, "TURN", 90))

    def test_different_player(self):
        """
        When I set a different player it should reflect
        """
        self.assertEqual(self.command.process("2 GET"), (2, "GET", None))

    def test_register(self):
        """
        When I register a player It should sort my data out
        """
        self.assertEqual(self.command.process(
            '1 REGISTER { "name": "Bruce Wayne", "position": [ 1, 2 ] }'),
            (
                1,
                "REGISTER",
                {
                    "name": "Bruce Wayne",
                    "position": [ 1, 2 ]
                }
            )
        )

if __name__ == '__main__':
    unittest.main()
