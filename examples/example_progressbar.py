from executorx.futures import ProcessPoolExecutor
from executorx.addons import Progress


def func(x):
    return x * x

def main():
    executor = ProcessPoolExecutor(max_workers=4, addons=[Progress])
    for i in range(100):
        executor.submit(func, i)
    executor.join()


if __name__ == '__main__':
    main()
