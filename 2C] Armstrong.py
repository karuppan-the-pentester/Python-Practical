num=int(input("Enter the number"))
sum=0
temp=num
while temp>0:
 i=temp%10
 sum=sum+(i*i*i)
 temp=temp//10
if sum==num:
 print("Amstrong")
else:
 print("not armstrong")
