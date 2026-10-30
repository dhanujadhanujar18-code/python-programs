Take an integer as input and return "POSITIVE" if the integer is positive, "NEGATIVE" if the integer is negative and "ZERO" if the integer is zero.

n=int(input())
if n==0:
  print("ZERO")
elif n>=0:
  print("POSITIVE")
else:
  print("NEGATIVE")
