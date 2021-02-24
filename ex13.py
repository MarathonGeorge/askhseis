f=open('kati.txt', 'r')
c=str(f.read())
lst=c.split(' ')
a=list()
print(lst)
met=0
for i in range(0, len(lst)-2):
    for j in range(i+1, len(lst)-1):
       if len(lst[i])+len(lst[j])==20:
           a[met]=str(lst[i]+lst[j])
           met=met+1
print(a)


        
        
