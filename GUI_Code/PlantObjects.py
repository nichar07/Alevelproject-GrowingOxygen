class Plant():
    def __init__(self, name, maxtemp, mintemp, brightness, size, ease, careinfo, pests, image):
        self.name = name
        self.maxtemp = maxtemp
        self.mintemp = mintemp
        self.brightness = brightness
        self.size = size
        self.ease = ease
        # initialising a passed in array into an object
        self.pests = Pests(self, pests)
        self.careinfo = careinfo
        self.image = image
        # score to rank the plants
        self.desirability_score = 0

    def scorechange(self, val):
        self.desirability_score += val

    # creating a repr so the testing is understandable without having to access attributes
    def __repr__(self):
        return f'Plant : {self.name} Score : {self.desirability_score}'


class Pests:
    def __init__(self, master, pestlist):
        # taking master for the repr
        self.parent = master
        # branching if the plant has no pests
        if pestlist:
            self.list = [pest_dict[i] for i in pestlist]
        else:
            self.list = 'None'
        # returning a list if the class is printed like it is in the GUI
    def __str__(self):
        return f'{"".join(self.list)}'

    def __repr__(self):
        return f'{self.parent.name} pests : {"".join(self.list)}'


# dictionary for the pests class to look in
pest_dict = {0: 'Aphids ', 1: 'Leaf Miners ', 2: 'GreenFlies ', 3: 'Spider Mites', 4: ' Mealybugs'}


class UserInputs():
    # class to act as a communicator for the GUI and algorithm
    def __init__(self, temperature, brightness, size, ease):
        self.temperature = temperature
        self.ease = ease
        self.size = size
        self.brightness = brightness
    # function that sets the temperature according to a passed value
    def settemp(self, val):
        self.temperature = val
        # testing that it works
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
