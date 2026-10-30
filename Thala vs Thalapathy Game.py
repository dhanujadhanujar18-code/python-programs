Write a program that takes a number as input and prints a famous Tamil cinema reference based on divisibility:
n=int(input())

if n % 3 ==0 and n % 5 == 0:
  print("ThalaThalapathy")
elif n % 3 == 0:
  print("Thala")
elif n % 5 == 0:
  print("Thalapathy")
else:
  print(n)
