
class AbstractWorker:

    n: int
    data: list
    limit: int

    def __init__(self, n: int):
        self.n = n
        self.data = []

    def run(self):
        pass
