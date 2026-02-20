# 2. reverse a string without using slicing

aa = input("Enter a string")
bb = " "
for ch in range(len(aa)-1,-1,-1):
  bb = bb+aa[ch]
print(bb)  
