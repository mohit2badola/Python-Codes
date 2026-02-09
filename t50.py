# Count how many numbers between 1–1000 are palindromes.

count=0

for i in range(1,1001):
    num=i
    cnum=0
    while num>0:
        mod=num%10
        cnum=(cnum*10)+mod
        num=int(num/10)
    if cnum==i:
        count+=1
    cnum=0
print(count)