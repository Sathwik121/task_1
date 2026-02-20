#side arrow


for i in range (1,6):
  for j in range (1,i+1):
    print("*",end=" ")
  print()
for i in range (4,0,-1):
  for j in range (1,i+1):
    print("*",end=" ")
  print()


for i in range (1,6):
  print("* "*i)
for i in range (6,0,-1):
  print("* "*i)


#top arrow
a = 3
for i in range (0,a):
  for j in range (a-i,0,-1):
    print(" ",end=" ")
  for k in range (0,2*i+1):
      print("*",end=" ")
  print()

#bottom arrow
a = 3
for i in range(a, 0, -1):
    for j in range(a - i, 0, -1):
        print(" ", end=" ")
    for k in range(0, 2 * i - 1):
        print("*", end=" ")
    print()
