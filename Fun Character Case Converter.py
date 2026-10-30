Write a program that takes a single character as input and performs the following
chr=input()
if chr.islower():
  print(chr.upper())
elif chr.isupper():
  print(chr.lower())
else:
  print("abcd theriyatha?")
