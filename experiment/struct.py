"""
experiment.struct

Module that contains structure classes
"""
from datetime import datetime
from typing import Dict, Any, Optional
from enum import Enum
from util import compare_object_dict


class RunStatus(Enum):
    """Enumeration for status tracking"""

    CREATED = 1
    READY = 2
    WAITING = 3
    RUNNING = 4
    TERMINATED = 5


DEFAULT_TIME = datetime(2000, 1, 1, 0, 0, 0, 0)


class Experiment:
    """Structure for storing experiment information"""

    __started: datetime = DEFAULT_TIME
    __ended: datetime = DEFAULT_TIME
    __args: Dict[str, Any]
    __status: RunStatus = RunStatus.CREATED
    __return_code: int = -1

    def __init__(self, args: Optional[Dict] = None):
        if args is None:
            args = {}
        self.__args = args

    @property
    def args(self) -> Dict[str, Any]:
        """Experiment arguments"""
        return self.__args

    @property
    def started(self) -> datetime:
        """Whence the experiment has started"""
        return self.__started

    @property
    def ended(self) -> datetime:
        """Whence the experiment has ended"""
        return self.__ended

    @property
    def return_code(self) -> int:
        """Return code of experiment script"""
        return self.__return_code

    @property
    def run_status(self) -> RunStatus:
        """Running status of experiment script"""
        return self.__status

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Experiment):
            return False
        return compare_object_dict(self, other)
