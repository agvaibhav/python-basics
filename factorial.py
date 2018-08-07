def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total
  
# method 2

def factorial(x):
  fact=1
  for i in range(1,x+1):
    fact=fact*i
  return fact
