from PlantObjects import Plant as P

from PlantObjects import UserInputs


class PlantSort:
    def __init__(self, userinputs):
        self.PlantList = [
            P('Devils Ivy', 24, 18, 3, 2, 9, 'devils ivy.PNG'),
            P('Peace Lily', 26, 20, 4, 1, 7, 'Peace Lily.png'),
            P('Snake Plant', 24, 18, 4, 3, 4, 'snake plant.png')]
        self.UI = userinputs
        self.calculate()

    def calculate(self):
        self.score_bright()
        self.score_temp()
        self.score_size()
        self.score_ease()
        self.PlantList.sort(key=lambda plant: plant.desirability_score, reverse=True)

    def score_bright(self):
        for i in self.PlantList:
            if self.UI.brightness == i.brightness:
                i.scorechange(5)
            elif self.UI.brightness == i.brightness + 1 or self.UI.brightness == i.brightness - 1:
                i.scorechange(2)

    def score_temp(self):

        for i in self.PlantList:

            if i.mintemp <= self.UI.temperature <= i.maxtemp:
                i.scorechange(5)
            else:
                i.scorechange(self.find_temp_dist(self.UI.temperature, i.maxtemp, i.mintemp))

    def find_temp_dist(self, tempval, max, min):
        # finding distance from ideal value of temperature in order to appropriately score the plant
        a = [16, 18, 20, 22, 24, 26]
        if tempval > max:
            return a.index(tempval) - a.index(max)
        if tempval < min:
            return a.index(min) - a.index(tempval)

    def score_size(self):
        for i in self.PlantList:
            if self.UI.size == i.size:
                i.scorechange(5)
            elif self.UI.size == i.size + 1 or self.UI.size == i.size - 1:
                i.scorechange(3)
            elif self.UI.size == i.size + 2 or self.UI.size == i.size - 2:
                i.scorechange(1)

    def score_ease(self):
        for i in self.PlantList:
            value = 5 - abs(self.UI.ease - i.ease)
            # if something is greater than 4 away from the desired ease, it will not be counted
            if value <= 0:
                pass
            else:
                i.scorechange(value)


david = UserInputs(20, 3, 2, 9)
james = PlantSort(david)
print([i for i in james.PlantList])
