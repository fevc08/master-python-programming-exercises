# Complete the function to return the tens digit of a given integer
def tens_digit(num):
  string_num = str(num)
  tens = string_num[len(string_num)-2]
  return int(tens)


# Invoke the function with any integer
print(tens_digit(1234567891))
