from typing import Any, Iterable, Protocol, Sequence, TypeVar

T = TypeVar("T")


def linear_contains(iterable: Iterable[T], target: T) -> bool:
    """O(n) runtime search implementation"""
    for item in iterable:
        if item == target:
            return True
    return False


C = TypeVar("C", bound="Comparable")


class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...

    def __lt__(self: C, other: C) -> bool:
        ...

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other

    def __le__(self: C, other: C) -> bool:
        return self <= other

    def __ge__(self: C, other: C) -> bool:
        return not self < other


def binary_contains(sequence: Sequence[C], target: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if sequence[mid] < target:
            low = mid + 1
        elif sequence[mid] > target:
            high = mid - 1
        else:
            return True
    return False
