class UiElement:
    def __init__(self, printer, location=None):
        self.printer = printer
        self.location = [0, 0] if location is None else location

        self.printer.add(self)
        self.string = []

    def build(self):
        return self.string

    def center(self):
        element_size = 0 if self.string[0] is None else len(self.string[0])
        self.location = [self.printer.screen_size[1]/2 + element_size/2, self.printer.screen_size[0]/2]


class Selectable(UiElement):
    def __init__(self, printer, location, is_selected=False, callback=None):
        UiElement.__init__(self, printer, location)
        self.callback = callback
        self.is_selected = is_selected

    def select(self):
        self.is_selected = True

    def deselect(self):
        self.is_selected = False

    def action(self):
        if self.callback is not None:
            self.callback()


class Button(Selectable):
    def __init__(self, printer, location=[1, 1], text="Wow, a button!", size=None, is_selected=False, callback=None):
        Selectable.__init__(self, printer, location, is_selected, callback)

        self.borders = ["┌", "─", "┐", "│", "└", "┘"]
        self.selected_borders = ["╔", "═", "╗", "║", "╚", "╝"]
        self.text = text
        self.size = size

        if self.size is None:
            self.size = [1, max(1, len(text))]

    def build(self):
        self.string = []
        borders = self.selected_borders if self.is_selected else self.borders

        self.string.append(borders[0] + self.size[1] * borders[1] + borders[2])

        for i in range(2 * self.size[0]):
            self.string.append(borders[3] + self.size[1] * " " + borders[3])

            if i == self.size[0] - 1:
                intermediate = borders[3] + max(int((self.size[1] - len(self.text))/2), 0) * " "\
                    + self.text[0:self.size[1]] \
                    + max(int((self.size[1] - len(self.text))/2 + (len(self.text) % 2)), 0) * " " + borders[3]
                self.string.append(intermediate)

        self.string.append(borders[4] + self.size[1] * borders[1] + borders[5])

        return self.string

    def center(self):
        self.location[1] = self.printer.screen_size[0] / 2 - self.size[1] / 2


class Text(UiElement):
    def __init__(self, printer, location=[1, 1], text="Wow, random text!"):
        UiElement.__init__(self, printer, location)
        self.text = text

    def build(self):
        self.string = [self.text]
        return self.string

    def center(self):
        self.location[1] = self.printer.screen_size[0] / 2 - len(self.text) / 2

