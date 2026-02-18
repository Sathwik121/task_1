#5. take 3 subject marks from user append it to list. print total and average

a = int(input("enter subject 1 marks "))
b = int(input("enter subject 2 marks "))
c = int(input("enter subject 3 marks "))
l = []
l.append(a)
l.append(b)
l.append(c)
l

total = l[0]+l[1]+l[2]
avg = total/len(l)
print(total,avg)
