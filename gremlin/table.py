from gremlin import uielement


class Table:
    def __init__(self, dimensions=None, position=None):
        if dimensions is None:
            raise ValueError("Please define the table dimensions - [x, y]")

        if position is None:
            raise ValueError("Please define the table dimensions - [x, y]")

        self.dimensions = dimensions
        self.position = position
        self.cells = []

    def append_left(self, new_cell, old_cell=None):
        pass

    def append_right(self, new_cell, old_cell=None):
        pass

    def append_top(self, new_cell, old_cell=None):
        pass

    def append_bottom(self, new_cell, old_cell=None):
        pass

    def replace(self, new_cell, old_cell):
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                if self.cells[i][j] == old_cell:
                    self.cells[i][j] = new_cell
                    return

    def remove(self, old_cell):
        for i in range(self.dimensions[0]):
            self.cells[i].remove(old_cell)

    def print(self):
        print_position = self.position

        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                self.cells[i][j].print()


class Cell:
    def __init__(self, cell_position, uielement):
        self.position = cell_position
        self.content = uielement

    def print(self, position)
        uielement.position = 
