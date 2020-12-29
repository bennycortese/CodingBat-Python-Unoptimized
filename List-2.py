def count_evens(nums):
    even_count = 0
    for num in nums:
        if (num % 2 == 0):
            even_count += 1

    return even_count

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
    sum = 0
    for num in nums:
        sum += num
    sum = sum - max(nums) - min(nums)

    return sum / (len(nums) - 2)

def sum13(nums):
    sum = 0
    for i in range(len(nums)):
        if (nums[i] != 13):
            sum += nums[i]
        else:
            if (i != len(nums) - 1):
                if (nums[i + 1] != 13):
                    sum -= nums[i + 1]

    return sum

def sum67(nums):
    sum = 0
    not_in_six_to_seven = True
    for i in range(len(nums)):
        if (nums[i] == 6):
            not_in_six_to_seven = False
        if (not_in_six_to_seven):
            sum += nums[i]
        if (nums[i] == 7):
            not_in_six_to_seven = True

    return sum

def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i] == nums[i + 1]:
            return True

    return False
