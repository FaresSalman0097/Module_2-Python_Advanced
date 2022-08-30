# x=[x for x in range(20)]
# y=[i for i in x if i%2==0]
# z=[0 if i%2==0 else 1 for i in x]
# print(y)
# print(z)
fruits = ["Maambazham","Annachi","Pazha","Vaazhai"]
'''newList = []
for x in fruits:
    newList.append(x)
print(newList)'''

# list comprehension format
newList1=[x for x in fruits]
print(newList1)

newList2=[x for x in fruits if "i" in x]
print(newList2)

newList3 = [x if x!="Annachi" else "Mathulai" for x in fruits]
print(newList3)

newList4 = [x for x in range(10)]
print(newList4)

newList5 = [x for x in range(10) if x>5]
print(newList5)

newList6 = ["Hello" for x in fruits]
print(newList6)

newList7=[x.upper() for x in fruits]
print(newList7)

x = [x for x in range(21)]

y = [i for i in x if i%2==0]
print(y)

z = [0 if i%2==0 else 1 for i in x]
print(z)



