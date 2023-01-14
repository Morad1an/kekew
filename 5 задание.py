with open('hh.txt') as f:
    dead=f.readline()
glasn='AO'
sogl='CDF'
for z in sogl:
    for x in sogl:
        for c in glasn:
            dead=dead.replace(z+x+c,'*')
count=0
maxik=0
for i in range(len(dead)):
    if dead[i]=='*':
        count+=1
        maxik=max(maxik,count)
    else:
        count=0
print(maxik)
        
            
