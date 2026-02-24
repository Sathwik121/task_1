#6. menu, no of items, print the total

menu = {"idly":35,"dosa":40,"poori":50,"chapathi":25,"masala_dosa":55}
total = 0
aa = int(input("enter no of items:"))
for i in range(aa):
  b = input("enter item : ")
  total = total +  menu[b]
print(total)
