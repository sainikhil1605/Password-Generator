#VATTI SAI NIKHIL REDDY
#17881A0434
from random import randint
y=0

print("Enter the length of password of choice greater than 6")
n=int(input())
while(n<6):
    print("Error enter again")
    n=int(input())
while(y!=n):
    print("Enter the number of letters of choice")
    l=int(input())
    print("Enter the number of numbers in pswrd")
    n1=int(input())
    print("Enter the number of symbols")
    sy=int(input())
    y=sy+n1+l
    if(y!=n):
        print("error enter again")
s=''
sp='!@#$%^&*-+/'
for i in range(n1):
    j=randint(1,10)
    s=s+str(j)

for i in range(sy):
    j=randint(0,len(sp)-1)
    s=s+str(sp[j])

for i in range(l//2):
    j=chr(randint(96,122))
    k=chr(randint(64,90))
    s=s+j+k
if(l%2!=0):
    s=s+chr(randint(96,122))

k=''
b=[]
while(len(k)<len(s)):
    j=randint(0,len(s)-1)
    if(j not in b):
        b=b+[j]
        k=k+s[j]
print("Password generated is")
print(k)
