import math

class RoundHole:
    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def fits(self, roundPeg): 
        return self.radius >= roundPeg.get_radius()

class RoundPeg:
    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def get_radius(self):
        return self.radius

class SquarePeg:
    def __init__(self, width: float) -> None:
        self.width = width

    def get_width(self):
        return self.width

class SquareAdpter(RoundPeg):
    peg: SquarePeg = None

    def __init__(self, peg: SquarePeg) -> None:
        self.peg = peg
    
    def get_radius(self):
        return self.peg.get_width() * math.sqrt(2)/2


hole = RoundHole(10)
peg = RoundPeg(18)

print(f'peg fits into hole = {hole.fits(peg)}')

hole = RoundHole(10)
peg = SquarePeg(17)
square_adapter = SquareAdpter(peg)

print(f'square peg fits into hole = {hole.fits(square_adapter)}')