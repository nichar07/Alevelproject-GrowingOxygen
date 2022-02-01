import unittest
import calculations as c
from GUI_Code import PlantObjects as po
from Database import PlantList as PL


class CalculationsTest(unittest.TestCase):
    def setUp(self):
        # self.TempPlant = c.PlantSort(po.UserInputs(20, 3, 2, 9)).best()
        # self.TempPlant2 = c.PlantSort(po.UserInputs(22, 4, 1, 7)).best()
        self.TempPlant3 = c.PlantSort(po.UserInputs(18, None, None, None))

    def test_devils(self):
        # testing that it returns a result
        self.assertEqual(self.TempPlant.name, "Devils Ivy")

    def test_devilscore(self):
        # testing that the result is the correct score
        self.assertEqual(self.TempPlant.desirability_score - 20, 20)

    def test_peace(self):
        self.assertEqual(self.TempPlant2.name, "Peace Lily")

    def test_temp(self):
        self.TempPlant3.score_temp()
        self.assertEqual(self.TempPlant3.PlantList[1].desirability_score, 2)


class DatabaseTest(unittest.TestCase):
    def setUp(self):
        self.PlantList = PL

    def test_object(self):
        self.assertIsInstance(self.PlantList[0], po.Plant)

    def test_pest(self):
        firstpest = self.PlantList[0].pests.list[0]
        self.assertEqual(firstpest, po.pest_dict[0])


if __name__ == '__main__':
    unittest.main()
