Write a program that reads a year as input and prints whether it is a leap year or not

year= int(input())

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
  print("yes")
else:
  print("no")
