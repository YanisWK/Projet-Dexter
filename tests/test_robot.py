from src.robot import Robot 

import unittest

class TestRobot(unittest.TestCase):
    def test_robot_est_instancce_de_robot(self):
        test_robot = Robot("Dexter",50,25,0,0)
        self.assertIsInstance(test_robot, Robot)

    def test_robot_avancer(self):
        test_robot = Robot("Dexter",50,25,0,0)
        test_robot.avancer(10)
        self.assertEqual(test_robot.x, 0)
        self.assertEqual(test_robot.y, -10)

    def test_robot_tourner(self):
        test_robot = Robot("Dexter",50,25,0,0)
        test_robot.tourner(90)
        self.assertEqual(test_robot.direction, 180)
        test_robot.tourner(-180)
        self.assertEqual(test_robot.direction, 0)

    #def test_robot_pos_coins_Robot(self):
    #    test_robot = Robot("Dexter",50,25,0,0)
    #    test_robot.pos_coins_Robot()
    #    self.assertEqual(test_robot.coordRobot, [(25.0, 0.0), (25.0, 50.0), (-25.0, 50.0), (-25.0, 0.0)])

    def test_robot_deplacementRobot(self):  
        test_robot = Robot("Dexter",50,25,0,0)
        test_robot.deplacementRobot(1)
        self.assertEqual(test_robot.x, 0)
        self.assertEqual(test_robot.y, 0)

if __name__ == '__main__':
    unittest.main()
