import math
# Complete the function to return the amount of days it will take to cover a route
def car_route(n,m):
  days = m/n
  return math.ceil(days)


# Invoke the function with two integers
print(car_route(20,40))
