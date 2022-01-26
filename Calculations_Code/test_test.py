import unittest
import calculations as c
from GUI_Code import PlantObjects as po


class CalculationsTest(unittest.TestCase):
    def setUp(self):
        self.TempPlant = c.PlantSort(po.UserInputs(20, 3, 2, 9)).best()
        #self.TempPlant2 = c.PlantSort(po.UserInputs(22, 4, 1, 7)).best()
    def test_devils(self):
        self.assertEqual(self.TempPlant.name, "Devils Ivy")  # add assertion here
    def test_devilscore(self):
        self.assertEqual(self.TempPlant.desirability_score,20)
    #def test_peace(self):
    #    self.assertEqual(self.TempPlant2.name, "Peace Lily")
if __name__ == '__main__':
    unittest.main()
