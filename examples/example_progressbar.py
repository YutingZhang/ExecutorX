from executorx.futures import ProcessPoolExecutor, ThreadPoolExecutor
from executorx.addons import Progress, WorkerId
import time


def func(x):
    print(WorkerId.my_worker_id(), x)
    time.sleep(0.1)
    return x * x

def main():
    executor = ProcessPoolExecutor(max_workers=4, addons=[Progress(num_tasks=100), WorkerId()])
    for i in range(100):
        executor.submit(func, i)
    executor.join()


if __name__ == '__main__':
    main()
