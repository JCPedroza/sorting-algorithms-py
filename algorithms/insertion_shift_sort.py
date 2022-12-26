from __future__ import annotations


def insertion_shift_sort(nums: list[float]) -> list[float]:
    """Sorts a numeric list, in ascending order, in-place, based on the Insertion Sort
    algorithm. This version does one comparison and one swap per iteration, other list
    value displacements are shifts instead of swaps, halving the data moved around when
    compared to the swap-heavy version.
    Complexity: time AO(n²) BO(n) WO(n²), space TO(n) AO(1)

    :param nums: Numeric list to be sorted.
    :return: Reference to the input list, now sorted.
    """
    for loop in range(1, len(nums)):
        idx = loop
        num = nums[idx]

        if nums[0] > nums[idx]:
            # Value is the new minimum, put it at the start of the list
            while idx > 0:
                nums[idx] = nums[idx - 1]
                idx -= 1

            nums[0] = num
        else:
            # Value is not the new minimum, find its correct place in the list
            while nums[idx - 1] > num:
                nums[idx] = nums[idx - 1]
                idx -= 1

            nums[idx] = num

    return nums
