import threading

from DCS.workers.regular_worker import RegularWorker
from DCS.workers.abstract_worker import AbstractWorker


class System:

    def __init__(self):
        self.workers = []

    def create_worker(self, n: int):
        self.workers.append(RegularWorker(n))

    def add_worker(self, worker: AbstractWorker):
        self.workers.append(worker)

    def run_workers(self):
        threads_num = len(self.workers)
        threads = []

        for i in range(threads_num):
            t = threading.Thread(
                target=self.workers[i].run,
            )

            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    def show_workers(self):
        for worker in self.get_workers():
            print(worker.n, '>', worker.arr)

    def get_workers(self):
        for worker in self.workers:
            yield worker
