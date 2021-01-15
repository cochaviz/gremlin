from gremlin import keyboard_listener
import game_screens
import os


class GameExecutor:
    def __init__(self, screen_size=None, cur_screen=None):
        os.system('setterm -cursor off')
        self.listener = keyboard_listener.Listener()

        if cur_screen is None:
            cur_screen = game_screens.MainMenuScreen(screen_size, self)

        self.cur_screen = cur_screen
        self.screen_size = self.cur_screen.screen_size

    def execute(self):
        self.cur_screen.show()

    def open(self, game_screen):
        self.cur_screen = game_screen
        self.execute()

    def stop(self):
        self.listener.close()
        os.system('setterm -cursor on && clear')
        quit(0)
