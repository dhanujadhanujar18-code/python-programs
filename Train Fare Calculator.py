Write a program to calculate the train fare based on the passenger’s age and distance to travel. The fare rules are:

age= int(input())
distance= int(input())

fare= distance * 5

if age < 12:
  fare = distance * 5 * 0.5
elif age <= 59:
  fare = distance * 5 
else:
  fare= distance * 5 * 0.75
  
print(int(fare))
