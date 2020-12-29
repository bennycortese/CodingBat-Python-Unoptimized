def first_last6(nums):
  return nums[0] == 6 or nums[len(nums) - 1] == 6
  #-1 also works for length since python has negative indices

def same_first_last(nums):
  if(len(nums) > 0):
    return nums[0] == nums[-1]
  return False

def make_pi():
  return [3, 1, 4]

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
  sum = 0
  for num in nums:
    sum += num
  return sum

def rotate_left3(nums):
  last_num = nums[0]
  for i in range(len(nums) - 1):
    nums[i] = nums[i + 1]
  nums[-1] = last_num
  return nums

def reverse3(nums):
  nums = nums[::-1]
  #nums.reverse()
  return nums

def max_end3(nums):
    first_val = nums[0]
    last_val = nums[-1]
    if (first_val > last_val):
        bigger_val = first_val
    else:
        bigger_val = last_val  # I KEEP FORGETTING MAX/MIN ARE A THING
    for i in range(len(nums)):
        nums[i] = bigger_val

    return nums

def sum2(nums):
  if(len(nums) == 1):
    return nums[0]
  if (len(nums) == 0):
    return 0
  return nums[0] + nums[1]

def middle_way(a, b):
  return [a[1], b[1]]

def make_ends(nums):
  return [nums[0], nums[-1]]

def has23(nums):
    for i in range(len(nums)):
        if (nums[i] == 2 or nums[i] == 3):
            return True

    return False
