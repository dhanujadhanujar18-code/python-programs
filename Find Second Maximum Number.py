Write a program that reads three integers and finds the second largest number among them using if-else statements.
If all three numbers are equal, print: No second max.

a=int(input())
b=int(input())
c=int(input())
if a>b and a<c or a>c and a<b:
  print(a)
elif b>a and b<c or b<a and b>c:
  print(b)
elif c>a and c<b or c>b and c<a:
  print(c)
else:
  print("No second max")
