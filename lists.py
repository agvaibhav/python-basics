n=int(input("Write the no of commands:"))
l=[]
for k in range(n):
    user_input = input("write the command:").split()
    
    if len(user_input)==3:
        i=int(user_input[1])
        e=int(user_input[2])
        if user_input[0]=="insert":
            l.insert(i,e)
    elif len(user_input)==2:
        e=int(user_input[1])
        if user_input[0]=="append":
            l.append(e)
        elif user_input[0]=="remove":
            l.remove(e)
    elif len(user_input)==1:
        if user_input[0]=="sort":
            l.sort()
        elif user_input[0]=="pop":
            l.pop()
        elif user_input[0]=="reverse":
            l.reverse()
        elif user_input[0]=="print":
            print(l)
        
