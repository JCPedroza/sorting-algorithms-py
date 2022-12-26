from __future__ import annotations


def native_sort(nums: list[float]) -> list[float]:
	"""Sorts a numeric list, in ascending order, based on the sorting algorithm
	provided by the runtime.
    Complexity: Depends on the runtime's implementation of the sorting algorithm.

    :param nums: Numeric list to be sorted.
    :return: Sorted copy of the input list.
    """
	return sorted(nums)
