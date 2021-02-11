a=open('kati.txt', 'r')
keimeno=a.read()
print(len(keimeno))
keimeno2=''
for i in range (0, len(keimeno)-1):
    keimeno2=keimeno2+chr(128-ord(keimeno[i]))
print(keimeno2[::-1])
