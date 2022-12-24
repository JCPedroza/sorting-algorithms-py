def bubble_temp_sort(nums):
	for loop in range(len(nums) - 1):
		is_sorted = True

		for idx in range(len(nums) - loop - 1):
			if nums[idx] > nums[idx + 1]:
				temp = nums[idx]
				nums[idx] = nums[idx + 1]
				nums[idx + 1] = temp
				is_sorted = False

		if is_sorted:
			break

	return nums

print(bubble_temp_sort([3, 2, 1]))
