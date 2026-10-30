Write a program that reads marks in five subjects and calculates the average. Based on the average, return a fun
and encouraging grade according to the following rules:

m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())
total=m1+m2+m3+m4+m5
average=total/5
if average >= 90:
  print("Excellent!")
elif average >= 80:
  print("Great Job!")
elif average >= 70:
  print("Good Effort!")
elif average >= 50:
  print("Keep Trying!")
else:
  print("Better Luck Next Time!")
