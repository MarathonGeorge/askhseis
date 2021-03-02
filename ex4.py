import re
myfile=open('kati.txt', 'r')
a=myfile.read()
b=re.split(a, ' ')
tri=[]
keim=''
myd=dict()
for i in range(1, len(b)-2):
    tri.append(str(b[i-1]+' '+b[i]+' '+b[i+1]))
    myd[tri[i-1]]='b'
lexeis=0
keim=b[len(b)-2]+' '+b[len(b)-1]+' '
print(keim)
pro=b[len(b)-2]
tel=b[len(b)-1]
myd[tri[len(tri)-1]].append('a')
while lexeis<197:
    exei='b'
    for i in myd:
        if i=='b':
            exei='a'
    if exei=='b':
        break
    else:
        for i in range(0, len(tri)):
            temp=re.split(tri[i], ' ')
            if temp[0]==pro and temp[1]==tel:
                keim=keim+tri[i]+' '
                pro=temp[1]
                tel=temp[2]
                myd[tri[i]].append('a')
                lexeis=lexeis+3
print(keim)
            
        
    


    

    
