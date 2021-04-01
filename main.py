from DCS.system import System


if __name__ == '__main__':
    system = System()

    workers_num = 10

    for i in range(0, workers_num):
        system.create_worker(i)

    system.show_workers()
    system.run_workers()
    print('---------------------------------')
    system.show_workers()

