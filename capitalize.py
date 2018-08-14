def solve(s):
    l=[]
    user_input=s.split()
    for i in user_input:
        cap=i[0].upper()
        name=cap+i[1:]
        l.append(name)
    user_output=' '.join(l)
    return user_output
