a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
if(a>b) and (a>c):
  largest=a
elif(b>a) and(b>c):
  largest=b
else:
  largest=c
print("The largest number among these three is",largest)
