def double_char(str):
  double_string = ""
  for i in range(len(str)):
    double_string = double_string + str[i] + str[i]
  return double_string

def count_hi(str):
    count = 0
    for i in range(len(str) - 1):
        if (str[i:i + 2] == "hi"):
            count += 1

    return count

def cat_dog(str):
  cat_count = 0
  dog_count = 0
  for i in range(len(str) - 2):
    if(str[i:i+3] == "cat"):
      cat_count += 1
    if(str[i:i+3] == "dog"):
      dog_count += 1
  return cat_count == dog_count

def count_code(str):
    count = 0
    for i in range(len(str) - 3):
        if (str[i:i + 2] == "co" and str[i + 3:i + 4] == "e"):
            count += 1

    return count

def end_other(a, b):
    # if(len(a) > len(b)):
    #   return (a[len(a) - len(b):].lower() == b.lower())
    # return (b[len(b) - len(a):].lower() == a.lower())

    if (len(a) > len(b)):
        return a.lower().endswith(b.lower())
    return b.lower().endswith(a.lower())

def xyz_there(str):
  trueChecker = False
  for i in range(len(str) - 2):
    if(str[i:i+3] == "xyz"):
      if(i != 0):
        trueChecker = str[i-1:i+3] != ".xyz"
      else:
        trueChecker = True
  return trueChecker
