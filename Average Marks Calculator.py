Write a program that reads marks in five subjects and calculates the average.

marks=[int(input()) for _ in range(5)]
average = sum(marks) / 5
if average.is_integer():
  print(int(average))
else:
  print(f"{average:.2f}")

