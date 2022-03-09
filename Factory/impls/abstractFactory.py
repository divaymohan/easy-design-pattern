class Dog:
    """One of the objects to be returned"""

    def speak(self):
        return "Woof!"
    
    def __str__(self) -> str:
        return "Dog"


class DogFactory:
    """Concrete factory"""
    def get_pet(self):
        pass

    def get_food(self):
        pass