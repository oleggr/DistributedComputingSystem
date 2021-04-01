from DCS.system import System


def test_create_worker(system: System):
    system.create_worker(1)

    for worker in system.get_workers():
        assert [] == worker.arr

    system.run_workers()

    for worker in system.get_workers():
        tmp_arr = [worker.n] * worker.limit
        assert tmp_arr == worker.arr
