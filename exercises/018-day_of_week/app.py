# Complete the function to return the number of day of the week for k'th day of year
def day_of_week(k):
  dow = 0
  if k % 7 == 1:
    dow = 4
  elif k % 7 == 2:
    dow = 5
  elif k % 7 == 3:
    dow = 6
  elif k % 7 == 4:
    dow = 0
  elif k % 7 == 5:
    dow = 1
  elif k % 7 == 6:
    dow = 2
  elif k % 7 == 0:
    dow = 3
  return dow


# Invoke function day_of_week with an integer between 1 and 365
print(day_of_week(1))
