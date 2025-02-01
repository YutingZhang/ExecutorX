__all__ = [
    'get_current_executor_identifier',
    'set_current_executor_identifier',
    'FuncWrapperWithExecutorIdentifier'
]


import contextlib

current_executor_identifier = None


def get_current_executor_identifier():
    return current_executor_identifier


@contextlib.contextmanager
def set_current_executor_identifier(executor_identifier):
    global current_executor_identifier
    previous_executor_identifier = current_executor_identifier
    current_executor_identifier = executor_identifier
    yield
    current_executor_identifier = previous_executor_identifier


class FuncWrapperWithExecutorIdentifier:
    def __init__(self, func, executor_identifier):
        self.func = func
        self.executor_identifier = executor_identifier

    def __call__(self, *args, **kwargs):
        with set_current_executor_identifier(self.executor_identifier):
            return self.func(*args, **kwargs)
