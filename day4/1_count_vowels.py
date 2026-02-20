#1. take a sentence count how many vowels it has 

count = 0
aa = input(" enter the string")
for ch in aa:
  for j in "a,e,i,o,u":
    if ch == j:
      count = count+1 

print(count)      
