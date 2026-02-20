n = 10
m = n+(n-1)
l = n+2
for i in range (0,n):
  if i == 0 or i == n-1:
    print("* "*l ,end = " ")
  else:
    print("*"," "*m,"*",end = " ")
  print()
