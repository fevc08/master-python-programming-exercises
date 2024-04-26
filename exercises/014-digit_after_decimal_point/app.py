# Complete the function to return the first digit to the right of the decimal point
def first_digit(num):
  get_decimal = num - int(num)
  get_first = str(get_decimal)[2]
  return int(get_first)


# Invoke the function with a positive real number. ex. 34.33
print(first_digit(1.79))
