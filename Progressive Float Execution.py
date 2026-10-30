Write a program that reads a floating-point number and prints successively rounded values, reducing the number of decimal places by one each step.

import struct
a=float(input())
a=struct.unpack('f',struct.pack('f',a))[0]
print(f"{a:.5f}")
print(f"{a:.4f}")
print(f"{a:.3f}")
print(f"{a:.2f}")
print(f"{a:.1f}")
print(f"{a:.0f}")
