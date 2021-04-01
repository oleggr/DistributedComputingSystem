import threading

from DCS.workers.worker import Worker


class System:

    def __init__(self):
        self.workers = []

    def create_worker(self, n: int):
        self.workers.append(Worker(n))

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
        for worker in self.workers:
            print(worker.n, '>>', worker.arr)
