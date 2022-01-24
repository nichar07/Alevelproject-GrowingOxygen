import unittest
import calculations as c
from GUI_Code import PlantObjects as po


class CalculationsTest(unittest.TestCase):
    def setUp(self):
        self.TempPlant = c.PlantSort(po.UserInputs(20, 3, 2, 9)).best()
    def test_devils(self):
        self.assertEqual(self.TempPlant.name, "Devils Ivy")  # add assertion here


if __name__ == '__main__':
    unittest.main()
