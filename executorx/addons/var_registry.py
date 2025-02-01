# Author: Yuting Zhang
# This file is part of ExecutorX, licensed under the GNU Lesser General Public License V2.1.

__author__ = ['Yuting Zhang']

__all__ = [
    'VarRegistry'
]


from executorx.foundation.addon import PoolExecutorAddon
from executorx.foundation.executor_identifier import get_current_executor_identifier


var_registry = dict()


def current_var_registry():
    current_executor_id = get_current_executor_identifier()
    if current_executor_id not in var_registry:
        return dict()
    return var_registry[current_executor_id]


def get_var(key):
    return current_var_registry().get(key)

class VarRegistry(PoolExecutorAddon):

    def __init__(self, var_dict: dict = None, /, **kwargs):
        super().__init__()
        if var_dict is None:
            var_dict = {}
        self.var_dict = {**var_dict, **kwargs}
        self.need_to_pickle_var_dict = True

    @classmethod
    def get(cls, key):
        return get_var(key)

    def on_start(self) -> None:
        if not self.executor.is_process_pool_spawn:
            self.need_to_pickle_var_dict = False
            var_registry[self.executor.identifier] = dict(self.var_dict)

    def initializer(self) -> None:
        if self.executor.identifier not in var_registry:
            var_registry[self.executor.identifier] = dict(default=self.var_dict)

    def after_shutdown(self) -> None:
        # clean up if in main thread
        if self.executor.identifier in var_registry:
            try:
                del var_registry[self.executor.identifier]
            except KeyError:
                pass

    def __getstate__(self):
        d = dict(self.__dict__)
        if self.need_to_pickle_var_dict:
            d['var_dict'] = None
        return d
