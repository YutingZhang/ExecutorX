# Author: Yuting Zhang
# This file is part of ExecutorX, licensed under the GNU Lesser General Public License V2.1.

__author__ = ['Yuting Zhang']

__all__ = [
    'RLock',
    'Lock',
]


from .utils import ResetAtPickleObjectWrapper
import threading


class RLock(ResetAtPickleObjectWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(threading.RLock, *args, **kwargs)


class Lock(ResetAtPickleObjectWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(threading.Lock, *args, **kwargs)
