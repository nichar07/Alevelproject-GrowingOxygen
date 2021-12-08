class Plant():
    def __init__(self, name, maxtemp, mintemp, brightness, size, ease, image):
        self.name = name
        self.maxtemp = maxtemp
        self.mintemp = mintemp
        self.brightness = brightness
        self.size = size
        self.ease = ease
        self.image = image
        self.desirability_score = 0

    def scorechange(self, val):
        self.desirability_score += val


class UserInputs():
    def __init__(self, temperature, ease, size, brightness):
        self.temperature = temperature
        self.ease = ease
        self.size = size
        self.brightness = brightness

    def settemp(self, val):
        self.temperature = val
        print('set', val)
        print(self.temperature)

    def setease(self, val):
        self.ease = val
        print('set', val)

    def setsize(self, val):
        self.size = val
        print('set', val)

    def setbright(self, val):
        self.brightness = val
        print('set', val)
