def apple_sharing(n,k):
  took = k // n
  remain = k % n
  return took, remain
 

print(apple_sharing(6,50))
