# Global imports
import unittest

# Local includes
from app.objects.GameObject import GameObject
from app.objects.Barrel import Barrel
from app.objects.Bullet import Bullet
from app.World import World
from app.Position import Position

"""
This class tests the ControllerBase by creating a mock from this
Base class
"""
class BarrelTest(unittest.TestCase):

    def setUp(self):
        self.barrel = Barrel(Position())

    """
    """
    def test_defaults(self):
     self.assertEqual(self.barrel.explode,False)

     """
     When a barrel is hit with a bullet it should explode
     """
     def test_explode(self):
         bullet = Bullet(0,Position())
         self.barrel._on_collision(bullet)
         self.assertEqual(self.barrel.explode,True)



    """
    get_data should also include deatials on whether it shoudl explode
    """
    def test_to_data(self):
        self.assertEqual(self.barrel.to_data(),{ "type":"barrel", "position":[0,0], "direction": 0, "alive": True, "explode":False})

    """
    When hit with a bullet it should create 9 flames
    """
    def test_fire(self):
        world = World(5,5)
        world.addObject(Barrel(Position(4,1)))
        world.addObject(Bullet(90,Position(2,1)))
        world.doStep()
        world.doStep()
        world.doStep()
        self.assertEqual(len(world.objects),9)
        

if __name__ == '__main__':
    unittest.main()
