#write a programme that takes your age and prints if the age is between 20 and 30 (teen, adult and 13,19 adult if age is 20 and 59

age = int(input(" Enter your age: "))
if age < 13 and age > 0:
  print("kid")
elif age < 20 and age > 13 :
  print("teen")
elif age < 60:
  print("adult")
else:
  print("senior citizen")   
