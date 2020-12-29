def string_times(str, n):
  super_string = ""
  for i in range(n):
    super_string += str
  return super_string

def front_times(str, n):
  the_big_string = ""
  for i in range(n):
    the_big_string += str[0:3]
  return the_big_string

def string_bits(str):
  every_other_char_string = ""
  for i in range(0, len(str), 2):
    every_other_char_string += str[i]
  return every_other_char_string

def string_splosion(str):
  string_multi_length = ""
  for i in range(len(str)):
    string_multi_length += str[:i+1]
  return string_multi_length

def last2(str):
    last_count = 0
    for i in range(len(str) - 2):
        if (str[i:i + 2] == str[len(str) - 2:]):
            last_count += 1

    return last_count

def array_count9(nums):
    nine_count = 0
    for i in nums:
        if (i == 9):
            nine_count += 1

    return nine_count

def array_front9(nums):
    first_four = 4

    if (len(nums) < first_four):
        first_four = len(nums)

    for i in range(first_four):
        if nums[i] == 9:
            return True
    return False

def array123(nums):
    for i in range(len(nums) - 2):
        if (nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3):
            return True

    return False

def string_match(a, b):
    count = 0
    if (len(a) < len(b)):  # reminder to self for future, min is a thing in python
        for i in range(len(a) - 1):
            if (a[i:i + 2] == b[i:i + 2]):
                count += 1

    else:
        for i in range(len(b) - 1):
            if (a[i:i + 2] == b[i:i + 2]):
                count += 1

    return count

