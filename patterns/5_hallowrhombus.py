n = 5
m = n+(n-1)
l = n+2
for i in range (0,n):
  for j in range (n-i,0,-1):
    print(" ",end=" ")
  if i == 0 or i == n-1:
    print("* "*l ,end = " ")
  else:
    print("*"," "*m,"*",end = " ")
  print()
 
