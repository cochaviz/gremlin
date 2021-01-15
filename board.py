from gremlin import uielement


class Board:
    def __init__(self, printer=None, dimensions=8, size=8):
        self.printer = printer
        self.tiles = []

        for i in range(dimensions):
            self.tiles.append(Tile(printer, size=size))

class Tile(uielement.Button):
    def __init__(self, printer=None, piece=None, size=None):
        if size is None:
            raise ValueError("Size not defined for tile")

        uielement.Button.__init__(self, printer, text="", size=size)

        self.printer = printer
        self.piece = piece

    def update(self):
        pass

