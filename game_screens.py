import os
from gremlin import uielement, screenprinter
import entity


class GameScreen:
    def __init__(self, screen_size=None, executor=None):
        if screen_size is None:
            try:
                rows, columns = os.popen('stty size', 'r').read().split()
                screen_size = [int(columns), int(rows)]
            except:
                print("Error: incompatible terminal! Please check if your terminal has 'stty' installed")

        self.screen_size = screen_size
        self.ui_printer = screenprinter.UiPrinter(self.screen_size)

        if executor is None:
            raise TypeError
        self.executor = executor

    def show(self):
        pass

    def loop(self):
        pass


class MainMenuScreen(GameScreen):
    def __init__(self, screen_size=None, executor=None):
        GameScreen.__init__(self, screen_size, executor)

    def show(self):
        text = uielement.Text(self.ui_printer, location=[20, 30], text="TERMINAL CHESS")
        play_button = \
            uielement.Button(self.ui_printer, size=[1, 20], is_selected=True, text="Play!", location=[30, 20]
                             , callback=self.open_alivescreen)
        quit_button = \
            uielement.Button(self.ui_printer, size=[1, 10], is_selected=False, text="Quit", location=[40, 40]
                             , callback=self.executor.stop)

        nrom_button = \
            uielement.Button(self.ui_printer, size=[1, 10], is_selected=False, text="Hey", location=[50, 50]
                             , callback=self.executor.stop)

        text.center()
        play_button.center()
        nrom_button.center()
        quit_button.center()

        self.ui_printer.display()
        self.loop()

    def loop(self):
        while True:
            try:
                if self.executor.listener.key_pressed():
                    key = self.executor.listener.read_key()

                    if key == 'w':
                        self.ui_printer.select_cycle(clockwise=False)
                    if key == 's':
                        self.ui_printer.select_cycle()
                    if key == '\n':
                        self.ui_printer.selected.action()

            except IOError:
                self.executor.stop()

    def open_alivescreen(self):
        self.executor.open(AliveScreen(self.screen_size, self.executor))


class AliveScreen(GameScreen):
    def __init__(self, screen_size=None, executor=None):
        GameScreen.__init__(self, screen_size, executor)

        self.entity_printer = screenprinter.EntityPrinter(self.screen_size)
        self.player = entity.Mover(self.entity_printer)

    def show(self):
        self.entity_printer.display()
        self.loop()

    def loop(self):
        while True:
            try:
                if self.executor.listener.key_pressed():
                    key = self.executor.listener.read_key()

                    if key == 'w':
                        self.player.move([-1, 0])
                    if key == 'a':
                        self.player.move([0, -1])
                    if key == 's':
                        self.player.move([1, 0])
                    if key == 'd':
                        self.player.move([0, 1])

            except IOError:
                self.executor.stop()

