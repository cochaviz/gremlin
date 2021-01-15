import sys
import select
import tty
import termios
import atexit


class Listener:
    def __init__(self):
        try:
            atexit.register(self.restore_settings)
            self.old_settings = termios.tcgetattr(sys.stdin)

            tty.setcbreak(sys.stdin.fileno())

        except IOError or ValueError:
            print("Can't deal with your keyboard!")

    @staticmethod
    def key_pressed():
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    @staticmethod
    def read_key():
        return sys.stdin.read(1)

    def restore_settings(self):
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)

    def close(self):
        atexit.unregister(self.restore_settings)
        self.restore_settings()
        sys.stdin.close()
