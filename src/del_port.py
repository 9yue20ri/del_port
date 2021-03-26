import re
b=re.compile('^.*.*?:')
with open(r"C:\Users\Desktop\ip.txt","r") as f:
    c = f.readlines()
    for t in c:
        w=re.findall(b,t)
        n=str(w)
        a=n.replace(':','')
        a1=a.replace('http//','')
        a3=a1.replace('[\'','')
        a4=a3.replace('\']','')
        a5=list(a4)
        ls3 = ''.join(a5)
        ls4=ls3.split()
        print(ls3)
        with open('ips.txt','a+') as z:
            z.write(ls3+'\n')