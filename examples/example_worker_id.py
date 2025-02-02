from executorx.futures import ProcessPoolExecutor, ThreadPoolExecutor
from executorx.addons import WorkerId
import time


def func(x):
    time.sleep(0.1)
    worker_id = WorkerId.my_worker_id()
    a = x * x * worker_id
    print('Work ID', worker_id)
    return a

def main():
    executor = ProcessPoolExecutor(
        max_workers=2, addons=[
            WorkerId
        ]
    )
    results = executor.map(func, range(20))
    # executor.join()
    print(list(results))
    pass


if __name__ == '__main__':
    main()
