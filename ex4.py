import re
myfile=open('kati.txt', 'r')
b=[]
pon=1
a=myfile.read()
li=re.split(a)
ser=li[-1]+li[-2]
lw1=li[-2]
lw2=li[-1]
c=2
for i in range(2, len(li)-1):
    b[pon]=a[i-1]+''+a[i]+''+a[i+1]
    pon=pon+1
while c<200:
    for i in range(2, pon):
        if re.split(b[pon])[1]==lw2 and re.split(b[pon])[0]==lw1:
            ser=ser+b[pon]
            lw1=re.split(b[pon])[0]
            lw2=re.split(b[pon])[1]
            c=c+3
