import time


class Worker:

    limit = 5

    def __init__(self, n: int):
        self.n = n
        self.arr = []

    def run(self):
        counter = 0

        while counter < self.limit:
            self.arr.append(self.n)
            counter += 1
            time.sleep(1)
