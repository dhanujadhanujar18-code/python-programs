Write a program to determine the berth type based on the seat number.

seat = int(input())
berth = seat % 8 

if berth == 1 or berth == 4:
  print("LB")
elif berth == 2 or berth == 5:
  print("MB")
elif berth == 3 or berth == 6:
  print("UB")
elif berth == 7:
  print("SL")
else:
  print("SU")
