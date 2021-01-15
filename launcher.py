import os
from executor import GameExecutor


def main():
    os.system('setterm -cursor off')
    executor = GameExecutor()
    executor.execute()


main()
