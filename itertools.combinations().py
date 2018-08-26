from itertools import combinations
s,n = input().split()
n=int(n)
for i in range(1,n+1):
    for j in combinations(sorted(s),i):
        print(''.join(j))
   
