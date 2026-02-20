a=7
for i in range (0,a):
  for j in range (a-i,0,-1):
    print(" ",end=" ")
  for k in range (0,2*i+1):
      print("*",end=" ")
  print()
for i in range(a-1, 0, -1):
    for j in range(a - i+1, 0, -1):
     print(" ", end=" ")
    for k in range(0, 2 * i - 1):
        print("*", end=" ")
    print()
