if __name__ == '__main__':
    N = int(input())
    l=[]
    for k in range(N):
        cmd= input().split()
        if len(cmd)==3:
            i=int(cmd[1])
            e=int(cmd[2])
            if cmd[0]=="insert":
                l.insert(i,e)
        elif len(cmd)==2:
            e=int(cmd[1])
            if cmd[0]=='remove':
                l.remove(e)
            elif cmd[0]=='append':
                l.append(e)
        elif len(cmd)==1:
            if cmd[0]=='sort':
                l.sort()
            elif cmd[0]=='pop':
                l.pop()
            elif cmd[0]=='reverse':
                l.reverse()
            elif cmd[0]=='print':
                print(l)
