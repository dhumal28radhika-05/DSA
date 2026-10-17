def highestOccurringElement(nums):
    max_count = 0
    answer = nums[0]

    for i in range(len(nums)):
        count = 0

        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1

        if count > max_count:
            max_count = count
            answer = nums[i]
        elif count == max_count and nums[i] < answer:
            answer = nums[i]

    return answer