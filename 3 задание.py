a="ПОЛИНА"
count=0
for i1 in a:
    for i2 in a:
        for i3 in a:
            for i4 in a:
                for i5 in a:
                    for i6 in a:
                        for i7 in a:
                            s=i1+i2+i3+i4+i5+i6+i7
                            if (s[0]!="А" and s.count("П")==1 and s.count("А")==1):
                                count+=1
print(count)
