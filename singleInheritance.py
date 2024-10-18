class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

    def display_info(self):
        print(f"Name: {self.name}, Species: {self.species}")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Woof! Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball")

my_dog = Dog("Buddy", "Golden Retriever")
my_dog.display_info()
my_dog.make_sound()
my_dog.fetch()
