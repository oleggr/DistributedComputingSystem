from DCS.system import System


if __name__ == '__main__':
    system = System()
    system.create_worker(1)
    system.create_worker(2)

    system.show_workers()
    system.run_workers()

    system.show_workers()

