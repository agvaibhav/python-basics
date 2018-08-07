def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
        print x
    return total
  
# method 2

def digit_sum(x):
  sum=0
  num=str(x)
  for i in num:
    digit=int(i)
    sum+=digit
  return sum
