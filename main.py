from DCS.system import System
from DCS.workers.square_worker import SquareWorker


if __name__ == '__main__':
    system = System()

    workers_num = 10

    for i in range(0, int(workers_num / 2)):
        system.create_worker(i)

    for i in range(int(workers_num / 2), workers_num):
        system.add_worker(SquareWorker(i))

    system.show_workers()
    system.run_workers()
    print('---------------------------------')
    system.show_workers()
