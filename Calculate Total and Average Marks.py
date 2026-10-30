John wants to learn how to calculate the total and average marks of a student in programming.Write a program that reads the
student's name and marks in five subjects. Then calculate and print

name=input()
m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
total=m1+m2+m3+m4+m5
avg=float(total/5)
print(f"Student Name: {name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {avg:.2f}")
