
class Plant():
    def __init__(self, name, maxtemp, mintemp, brightness, size, ease, careinfo, pests, image):
        self.name = name
        self.maxtemp = maxtemp
        self.mintemp = mintemp
        self.brightness = brightness
        self.size = size
        self.ease = ease
        self.pests = Pests(self, pests)
        self.careinfo = careinfo
        self.image = image

        self.desirability_score = 0

    def scorechange(self, val):
        self.desirability_score += val

    def __repr__(self):
        return f'Plant : {self.name} Score : {self.desirability_score}'


pest_dict = {0: 'Aphids ', 1: 'Leaf Miners ', 2: 'GreenFlies '}


class Pests:
    def __init__(self, master, pestlist):
        self.parent = master
        self.list = [pest_dict[i] for i in pestlist]

    def __repr__(self):
        return f'{"".join(self.list)}'


class UserInputs():
    def __init__(self, temperature, brightness, size, ease):
        self.temperature = temperature
        self.ease = ease
        self.size = size
        self.brightness = brightness

    def settemp(self, val):
        self.temperature = val
        print('set', val)
        print(self.temperature)

    def setease(self, val):
        self.ease = int(val)
        print('set', val)
        print(type(val))

    def setsize(self, val):
        self.size = val
        print('set', val)

    def setbright(self, val):
        self.brightness = val
        print('set', val)