#while loop
n=int(input()) #123
digits=0
total=0
while n!=0:
     rem=n%10
     digits+=1
     total=total+rem
     n=n//10
print("no of digits:",digits)
print("sum of digits:",total)

num=int(input()) #38
while not (num>=0 and num<=9):
    sums=0
    while num!=0:
        rem=num%10
        sums=sums+rem
        num=num//10
    num=sums
else:
    print(num)
