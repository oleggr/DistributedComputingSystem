
class AbstractWorker:

    n: int
    arr: list
    limit: int

    def __init__(self, n: int):
        self.n = n
        self.arr = []

    def run(self):
        pass
