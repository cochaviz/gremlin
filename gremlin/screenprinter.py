import sys
from gremlin import uielement
from gremlin import time


class ScreenPrinter:
    def __init__(self, screen_size):
        self.time = time.Time()

        self.screen_size = screen_size
        self.character_step = 2
        self.elements = []

    def add(self, element):
        self.elements.append(element)

    @staticmethod
    def clear():
        print(chr(27) + "[2J")

    @staticmethod
    def print_at(string, location):
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" %
                         (location[0], location[1], string))
        sys.stdout.flush()


class EntityPrinter(ScreenPrinter):
    def __init__(self, init_screen_size):
        ScreenPrinter.__init__(self, init_screen_size)

    def display(self):
        self.time.update()
        self.clear()

        for entity in self.elements:
            if entity.has_valid_location():
                for i, char_part in enumerate(entity.character):
                    self.print_at(char_part, [entity.location[0], entity.location[1] + i])


class UiPrinter(ScreenPrinter):
    def __init__(self, screen_size):
        ScreenPrinter.__init__(self, screen_size)
        self.selectable = []
        self.selected = None

    def display(self):
        self.clear()

        for element in self.elements:
            for i, element_part in enumerate(element.build()):
                self.print_at(element_part, [element.location[0] + i, element.location[1]])

    def add(self, element):
        if isinstance(element, uielement.Selectable):
            if self.selected is None:
                self.selected = element
            else:
                self.selectable.append(element)

        self.elements.append(element)

    def select_cycle(self, clockwise=True):
        if len(self.selectable) == 0 and self.selected is None:
            return

        if self.selected is not None:
            self.selected.deselect()

            if clockwise:
                self.selectable.append(self.selected)
            else:
                self.selectable.insert(0, self.selected)

        if clockwise:
            self.selected = self.selectable[0]
        else:
            self.selected = self.selectable[len(self.selectable)-1]

        self.selected.select()
        self.selectable.remove(self.selected)
        self.display()
