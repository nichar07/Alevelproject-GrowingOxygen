import unittest
import calculations as c
from GUI_Code import PlantObjects as po

plant= c.PlantSort(po.UserInputs(20, 3, 2, 9)).best()
print(plant)
class CalculationsTest(unittest.TestCase):
    def setUp(self):
        self.TempPlant = c.PlantSort(po.UserInputs(20, 3, 2, 9)).best()
    def test_devil(self):

        self.assertEqual(self.TempPlant.name, 'Devils Ivy')  # add assertion here


if __name__ == '__main__':
    unittest.main()
