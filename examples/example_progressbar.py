from executorx.futures import ProcessPoolExecutor, ThreadPoolExecutor
from executorx.addons import Progress, WorkerId


def func(x):
    return x * x

def main():
    executor = ProcessPoolExecutor(max_workers=4, addons=[WorkerId, Progress(num_tasks=100)])
    for i in range(100):
        executor.submit(func, i)
    executor.join()


if __name__ == '__main__':
    main()
