"""
This class tests the Index Controller
"""


# Global imports
import unittest

# Local includes
from app.Server import Server
from app.World import World

"""
This class tests the Direction class
"""
class ServerTest(unittest.TestCase):

    def setUp(self):
        self.server = Server()

    def test_get_world(self):
        self.assertIsInstance(self.server.get_world(), World)

if __name__ == '__main__':
    unittest.main()
