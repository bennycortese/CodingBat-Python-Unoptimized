def make_bricks(small, big, goal):
    five_chunks = big
    one_chunks = small
    if (small >= 5):
        five_chunks = five_chunks + one_chunks / 5
        one_chunks = one_chunks % 5

    return (one_chunks + five_chunks * 5 >= goal and small >= goal % 5)

def lone_sum(a, b, c):
  sum = 0
  if(a == b and b == c):
   return 0
  if(a == b):
    a = 0
    b = 0
  if(b == c):
    b = 0
    c = 0
  if(c == a):
    c = 0
    a = 0
  return a + b + c

def lucky_sum(a, b, c):
  sum = 0
  if(a != 13):
    sum += a
  else:
    return sum
  if(b != 13):
    sum += b
  else:
    return sum
  if(c != 13):
    sum += c
  return sum

def fix_teen(n):
  if(n >= 13 and n <= 19 and n != 15 and n != 16):
    n = 0
  return n
def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def round10(num):
  if(num % 10 >= 5):
    num = num - num % 10 + 10
  else:
    num = num - num % 10
  return num
def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)

def for_three(a, b, c):
    if ((abs(a - b) <= 1 or abs(a - c) <= 1) and abs(a - c) >= 2 and abs(b - c) >= 2):
        return True
    return False
def close_far(a, b, c):
    return for_three(a, b, c) or for_three(b, a, c) or for_three(c, a, b)

def make_chocolate(small, big, goal):
  temp_int_holder = goal - big * 5
  while(temp_int_holder < 0):
    temp_int_holder += 5
  if(small >= temp_int_holder):
    return temp_int_holder
  return -1
