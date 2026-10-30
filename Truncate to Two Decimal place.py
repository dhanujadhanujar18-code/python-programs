Write a program that takes a floating-point number as input and prints the value truncated (cut off) to two decimal places without rounding

num=float(input())
result=int(num*100)/100
print(f"{result:.2f}")
