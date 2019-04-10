# to check if all elements of a list are positive and if any of the element is palindrome
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
n = list(input().split())
print(all([int(i)>0 for i in n]) and any(j==j[::-1] for j in n))
