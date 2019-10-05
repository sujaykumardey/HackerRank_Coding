def marsExploration(s):
        a="SOS"
        flag=0
        for i in range(0,len(s)//3):
            if a =="".join([s[k] for k in range(i*3,(i+1)*len(a))]):
                continue
            else:
                m=0
                for j in range(i*3,(i+1)*len(a)):
                    
                    if a[m]!=s[j]:
                        flag+=1
                    m+=1
        return flag
 s=input()
 result=marsExploration(s)
 print(result)
