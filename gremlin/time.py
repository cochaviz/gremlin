import time

class Time:
    def __init__(self):
        self.latest = 0
        self.delta_time = 0
    
    def update(self):
        current = time.time()
        self.delta_time = current - self.latest
        self.latest = current
