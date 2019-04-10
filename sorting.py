# if want to sort according to some column k from arr
'''
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    for row in sorted(arr, key=lambda row: row[k]):
        print(*row)
'''


'''
Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
'''

# Method 1
'''
s = input()
print(*sorted(s,key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)),sep='')
'''

# Method 2
'''
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')
'''

# Method 3
'''
import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')
'''
