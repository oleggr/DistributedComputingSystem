import time

from DCS.workers.abstract_worker import AbstractWorker


class Worker(AbstractWorker):

    limit = 5

    def run(self):
        counter = 0

        while counter < self.limit:
            self.arr.append(self.n)
            counter += 1
            time.sleep(1)
