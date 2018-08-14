def minion_game(string):
    # your code goes here
    sck=0
    scst=0
    vowels="AEIOU"
    for i in range(len(string)):
        if string[i] in vowels:
            sck+=(len(string)-i)
        else:
            scst+=(len(string)-i)
    if scst>sck:
        print("Stuart {}".format(scst))
    elif sck>scst:
        print("Kevin {}".format(sck))
        
    elif sck==scst:
        print("Draw")
