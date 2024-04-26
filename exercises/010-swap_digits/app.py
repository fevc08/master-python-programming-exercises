# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  string_digits = str(num)
  swap = string_digits[1] + string_digits[0]
  return int(swap)
   
# Invoke the function with any two-digit integer as its argument
print(swap_digits(30))
