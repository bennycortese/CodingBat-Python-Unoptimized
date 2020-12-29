def cigar_party(cigars, is_weekend):
  if(is_weekend):
    return(cigars >= 40)
  return(cigars <= 60 and cigars >= 40)

def date_fashion(you, date):
  if(you <= 2 or date <= 2):
    return 0
  if(you >= 8 or date >= 8):
    return 2
  return 1

def squirrel_play(temp, is_summer):
  if(is_summer and temp >= 60 and temp <= 100):
    return True
  return (temp >= 60 and temp <= 90)

def caught_speeding(speed, is_birthday):
    if (is_birthday):
        if (speed <= 65):
            return 0
        if (speed <= 85 and speed >= 66):
            return 1
        if (speed >= 86):
            return 2

    if (speed <= 60):
        return 0
    if (speed <= 80 and speed >= 61):
        return 1
    if (speed >= 81):
        return 2

def sorta_sum(a, b):
  if((a + b) >= 10 and (a+b) <= 19):
    return 20
  return a + b

def alarm_clock(day, vacation):
    if (vacation):
        if (day > 0 and day < 6):
            return "10:00"
        return "off"

    if (day > 0 and day < 6):
        return "7:00"
    return "10:00"

def love6(a, b):
  return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

def in1to10(n, outside_mode):
    if (outside_mode):
        return (n <= 1 or n >= 10)
    return n >= 1 and n <= 10

def near_ten(num):
  return num % 10 >= 8 or num % 10 <= 2
