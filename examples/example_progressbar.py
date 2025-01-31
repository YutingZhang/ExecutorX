from executorx.futures import ProcessPoolExecutor, ThreadPoolExecutor
from executorx.addons import Progress, VarRegistry
import time


def func(x):
    time.sleep(0.1)
    a = x * x * VarRegistry.get('base')
    print(a)
    return a

def main():
    executor = ProcessPoolExecutor(
        max_workers=4, addons=[
            Progress(), VarRegistry(base=100)
        ]
    )
    for i in range(100):
        executor.submit(func, i)
    executor.join()


if __name__ == '__main__':
    main()
