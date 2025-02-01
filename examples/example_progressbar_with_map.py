from executorx.futures import ProcessPoolExecutor, ThreadPoolExecutor
from executorx.addons import Progress, VarRegistry
import time


def func(x):
    time.sleep(0.1)
    a = x * x * VarRegistry.get('base')
    return a

def main():
    executor = ThreadPoolExecutor(
        max_workers=4, addons=[
            Progress(), VarRegistry(base=100)
        ]
    )
    results = executor.map(func, range(20))
    # executor.join()
    print(list(results))
    pass


if __name__ == '__main__':
    main()
