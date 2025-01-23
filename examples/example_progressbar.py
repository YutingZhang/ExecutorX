from executorx.futures import ProcessPoolExecutor
from executorx.addons import Progress, WorkerId


def func(x):
    print(x * x)

def main():
    executor = ProcessPoolExecutor(max_workers=4) #, addons=[WorkerId])
    for i in range(100):
        executor.submit(func, i)
    executor.join()


if __name__ == '__main__':
    main()
