from __future__ import annotations


def bubble_flagless_sort(nums: list[float]) -> list[float]:
    """Sorts a numeric list, in ascending order, in-place, based on the Bubble Sort
    algorithm. No flag is used for early termination for already sorted lists, and no
    temporary variable is used for list value swap.
    Complexity: time O(n²), space TO(n) AO(1)

    :param nums: Numeric list to be sorted.
    :return: Reference to the input list, now sorted.
    """
    for loop in range(len(nums) - 1):
        for idx in range(len(nums) - loop - 1):
            if nums[idx] > nums[idx + 1]:
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]

    return nums
