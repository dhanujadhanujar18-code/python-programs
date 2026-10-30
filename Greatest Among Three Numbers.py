Write a program that reads an integer and print greatest among tree number using Ternary operator
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
  print(a)
elif b>c and b>a:
  print(b)
else:
  print(c)
  
