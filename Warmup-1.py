def sleep_in(weekday, vacation):
  if(not(weekday) or vacation):
    return True
  return False

def monkey_trouble(a_smile, b_smile):
  if(a_smile == b_smile):
    return True
  else:
    return False

def sum_double(a, b):
    if (a == b):
        return 2 * (a + b)

    return a + b

def diff21(n):
  if(n > 21):
    return 2 * (n - 21)
  if(n < 21):
    return 21 - n
  else:
    return 21 - n

def parrot_trouble(talking, hour):
    if (talking):
        if (hour < 7 or hour > 20):
            return True

    return False

def makes10(a, b):
  return (a == 10 or b == 10 or a + b == 10)

def near_hundred(n):
   return(abs(n-100) <= 10 or abs(n-200) <= 10)

def pos_neg(a, b, negative):
  if(negative):
    return (a < 0 and b < 0)
  return((a < 0 and b > 0) or (a > 0 and b < 0))

def not_string(str):
  if(str[0:3] == "not"):
    return str
  else:
    return "not " + str

def missing_char(str, n):
  return str[:n] + str[n+1:]

def front_back(str):
  if(len(str) > 1):
    return str[len(str)-1] + str[1:len(str)-1] + str[0]
  else:
    return str

  def front3(str):
      super_string = ""
      for i in range(3):
          super_string += str[:3]

      return super_string