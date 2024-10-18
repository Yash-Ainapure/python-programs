class Mammal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Mammal sound"

class Swimmer:
    def swim(self):
        return "Swimming"

class Dolphin(Mammal, Swimmer):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Click-click"

dolphin = Dolphin("Flipper")
print(f"{dolphin.name} says: {dolphin.speak()}")
print(f"{dolphin.name} is: {dolphin.swim()}")
