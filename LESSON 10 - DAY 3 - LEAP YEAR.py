# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆
if year%4==0:
  if year%100==0:
    if year%400==0:
      print("Leap year")
    elif year%400!=0:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
# Write your code below this line 👇
