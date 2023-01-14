flag=0
for A in range(1,10000):
    for x in ('0123456789ABC'):
        for y in ('0123456789ABC'):
            M=int('2'+x+'23'+x+'5',15)
            N=int('67'+x+'9'+y,13)
            if (M+A)%N==0:
                print(A)
                flag=1
    if flag:
        break
