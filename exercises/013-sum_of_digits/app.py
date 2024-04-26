# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
  suma = 0
  for digit in str(num):
    suma += int(digit)
  return suma


# Invoke the function with any three-digit number
print(digits_sum(123))
