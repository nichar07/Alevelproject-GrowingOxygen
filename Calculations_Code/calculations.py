from Calculations_Code.Database import PlantList as P

from GUI_Code.PlantObjects import UserInputs


class PlantSort:
    def __init__(self, userinputs):
        self.PlantList = P
        self.UI = userinputs

    def calculate(self):
        self.score_bright()
        self.score_temp()
        self.score_size()
        self.score_ease()
        self.PlantList.sort(key=lambda plant: plant.desirability_score, reverse=True)

    def best(self):

        self.calculate()
        return self.PlantList[0]

    def score_bright(self):
        if self.UI.brightness:
            for i in self.PlantList:
                if self.UI.brightness == i.brightness:
                    i.scorechange(5)
                elif self.UI.brightness == i.brightness + 1 or self.UI.brightness == i.brightness - 1:
                    i.scorechange(2)
                elif self.UI.brightness == i.brightness + 2 or self.UI.brightness == i.brightness - 2:
                    i.scorechange(1)

    def score_temp(self):
        if self.UI.temperature:

            for i in self.PlantList:
            # seeing if it is within the temperature range
                if i.mintemp <= self.UI.temperature <= i.maxtemp:
                    i.scorechange(5)
                else:
                    i.scorechange(self.find_temp_dist(self.UI.temperature, i.maxtemp, i.mintemp))

    def find_temp_dist(self, tempval, max, min):
        # finding distance from ideal value of temperature in order to appropriately score the plant
        a = [18, 20, 22, 24, 26]
        if tempval > max:
            return a.index(tempval) - a.index(max)
        if tempval < min:
            return a.index(min) - a.index(tempval)

    def score_size(self):
        if self.UI.size:
            for i in self.PlantList:
                if self.UI.size == i.size:
                    i.scorechange(5)
                elif self.UI.size == i.size + 1 or self.UI.size == i.size - 1:
                    i.scorechange(3)
                elif self.UI.size == i.size + 2 or self.UI.size == i.size - 2:
                    i.scorechange(1)

    def score_ease(self):
        if self.UI.ease:
            for i in self.PlantList:
                value = 5 - abs(self.UI.ease - i.ease)
                # if something is greater than 4 away from the desired ease, it will not be counted
                if value <= 0:
                    pass
                else:
                    i.scorechange(value)

#
# daniel = UserInputs(20, 3, 2, 9)
# james = PlantSort(daniel)
# #james.calculate()
# print([i for i in james.PlantList])
