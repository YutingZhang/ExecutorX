# Author: Yuting Zhang
# This file is part of ExecutorX, licensed under the GNU Lesser General Public License V2.1.

__author__ = ['Yuting Zhang']

__all__ = [
    'my_worker_id',
    'total_workers',
    'rank_and_world_size',
    'my_rank',
    'world_size',
    'WorkerId',
]


import multiprocessing
import os
from .. import threading
from ..foundation.addon import PoolExecutorAddon
from ..foundation.executor_identifier import get_current_executor_identifier

_worker_ids = dict()


def _get_worker_uid():
    return os.getpid(), threading.get_ident()


def rank_and_world_size():
    global _worker_ids
    worker_uid = _get_worker_uid()
    if worker_uid in _worker_ids:
        return _worker_ids[worker_uid]
    else:
        worker_uid = get_current_executor_identifier()
        if worker_uid in _worker_ids:
            return _worker_ids[worker_uid]
    return None, None


def my_worker_id():
    return rank_and_world_size()[0]


def total_workers():
    return rank_and_world_size()[1]


my_rank = my_worker_id
world_size = total_workers


class WorkerId(PoolExecutorAddon):

    @staticmethod
    def my_worker_id():
        return my_worker_id()

    def __init__(self):
        super().__init__()
        self._lock = multiprocessing.Lock()
        self._counter = multiprocessing.Value('i', 0)
        self.max_workers = 0
        self.executor_identifier = None

    def before_start(self) -> None:
        self.max_workers = self.executor.max_workers
        self.executor_identifier = self.executor.identifier

    @property
    def total_started_workers(self) -> int:
        with self._lock:
            return self._counter.value

    def initializer(self) -> None:
        with self._lock:
            my_worker_id = self._counter.value
            self._counter.value += 1
        global _worker_ids
        if not self.max_workers:
            worker_uid = self.executor_identifier
        else:
            worker_uid = _get_worker_uid()
        _worker_ids[worker_uid] = (my_worker_id, self.max_workers)

