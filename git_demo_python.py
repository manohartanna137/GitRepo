from functools import reduce
list1=[10,20,30,40]
addition=reduce(lambda x,y : x+y,list1)
print(addition)