Given two integers A and B, print their sum, difference,product, quotient and remainder each on a new line
a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
if a<0 or b<0:
  c=abs(a)%abs(b)
  print(-1*c)
else:
  print(a%b)
