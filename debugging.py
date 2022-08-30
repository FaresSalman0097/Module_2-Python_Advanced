import pdb

def addition(a,b):
    answer=a+b
    return answer

pdb.set_trace()
x=int(input("Enter the 1st number : "))
y=int(input("Enter the 2nd number : "))
sum = addition(x,y)
print(sum)