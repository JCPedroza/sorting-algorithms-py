from __future__ import annotations


def insertion_swap_sort(nums: list[float]) -> list[float]:
	"""Sorts a numeric list, in ascending order, in-place, based on the Insertion Sort
    algorithm. This version does two comparisons per iteration, and moves twice more
    data than necessary (this can be improved).
    Complexity: time AO(n²) BO(n) WO(n²), space TO(n) AO(1)

    :param nums: Numeric list to be sorted.
    :return: Reference to the input list, now sorted.
    """
	for loop in range(1, len(nums)):
		idx = loop

		while idx > 0 and nums[idx - 1] > nums[idx]:
			nums[idx - 1], nums[idx] = nums[idx], nums[idx - 1]
			idx -= 1

	return nums
