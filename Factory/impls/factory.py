class Dog:

    """A simple dog class"""

    def __init__(self,name) -> None:
        self.name = name

    def speak(self):
        return "Woof!"

class Cat:

    """A simple cat class"""

    def __init__(self,name) -> None:
        self.name = name

    def speak(self):
        return "Meow!"
    

def get_pet(pet="dog"):
    """The factory method"""
    pets = dict(dog=Dog("Hope"),cat=Cat("Peace"))
    return pets[pet]

d = get_pet("dog")
print(d.speak())

d = get_pet("cat")
print(d.speak())