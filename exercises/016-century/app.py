import math
# Complete the function to return the respective number of the century
def century(year):
  get_century = year/100
  return math.ceil(get_century)


# Invoke the function with any given year
print(century(1901))
