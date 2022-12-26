from __future__ import annotations


def selection_sort(nums: list[float]) -> list[float]:
    """Sorts a numeric list, in ascending order, in-place, based on the Selection Sort
    algorithm.
    Complexity: time O(n²), space TO(n) AO(1)

    :param nums: Numeric list to be sorted.
    :return: Reference to the input list, now sorted.
    """
    for loop in range(len(nums)):
        min_idx = loop

        for idx in range(loop + 1, len(nums)):
            if nums[idx] < nums[min_idx]:
                min_idx = idx

        nums[loop], nums[min_idx] = nums[min_idx], nums[loop]

    return nums
