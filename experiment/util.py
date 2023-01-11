"""
experiment.util

Modules with utility functions that are meant to be used for implementing package
"""

from typing import Iterable, Dict, Any, Optional


def __compare_object_dict(
    left_dict: Dict[str, Any], right_dict: Dict[str, Any], override: Iterable[str]
) -> bool:
    left_keys = left_dict.keys()
    right_keys = right_dict.keys()

    if len(left_keys) != len(right_keys):
        return False

    for key in left_keys:
        if key in override:
            continue
        left_value = left_dict.get(key)
        right_value = right_dict.get(key)
        if left_value != right_value:
            return False

    return True


def compare_object_dict(
    left: object, right: object, override: Optional[Iterable[str]] = None
) -> bool:
    """
    Compares objects' field and returns True if all fields but overriden fields equals.
    With override iterable, caller can specify which fields will not be compared.
    """

    if not hasattr(left, "__dict__"):
        if hasattr(right, "__dict__"):
            return False
        return left == right
    if not hasattr(right, "__dict__"):
        return False

    left_dict = vars(left)
    right_dict = vars(right)
    if override is None:
        override = []
    return __compare_object_dict(left_dict, right_dict, override)
