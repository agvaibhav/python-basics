from collections import Counter
x=input()
shoe=list(map(int, input().split()))
num=Counter(shoe)
cus=int(input())
sum=0
for i in range(cus):
    inp=list(map(int,input().split()))
    if inp[0] in num and num[inp[0]]>0:
        sum+=inp[1]
        num[inp[0]]-=1
        
print(sum)
