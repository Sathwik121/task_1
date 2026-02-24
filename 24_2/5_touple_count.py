#5. combine 2 tuples and count how times a specific value appears

aa = (1,2,3,4,5,6)
bb = (3,4,2,1,6,8)

aa = list(aa)
bb = list (bb)

cc = aa+bb
cc = tuple(cc)
cc.count(5)
