# parameters are the variables used when the function is defined
# arguments are the values passed for the variables while calling the function

# function without parameters
'''def withoutParameters():
    x=5
    y=10
    sum=x+y
    return sum
z = withoutParameters()
print(z)'''

# function with single parameter
'''def singleParameter(text):
    print(text)
name = "salmeera"
singleParameter(name)'''

# positional arguments
'''def positinalArgs(a,b,c):
    sum = a+b+c     # this sum is a local variable and can be called within the function
    return sum
# the variables defined as parameters are used within the function
sum = positinalArgs(6,9,12)   # this sum is a global variable
print(sum)'''

# keyword arguments
'''def keywordArgs(x,y,z):
    result = x*y+z  
    return result
result = keywordArgs(y=6,z=9,x=12)   # this sum is a global variable
print(result)'''
# for keyword arguments the order is not important, but the variables must be same

# we can also call the function by the combination of keyword and arguments
'''def keyPosArgs(x,y,z):
    result = x*y+z
    return result
result = keyPosArgs(6,z=9,y=12)
print(result)'''
# while calling this function the 1st position must be position argument
# When the keyword argument is used the next position also must be keyword args and not positional args

# default argument
'''def defaultArg(a,b,c="Nellai"):
    print(a," is a beautiful city")
    print(b," is also a beautiful city")
    print("but ",c," is not just a city, its an emotion")
defaultArg("Trichy","Chennai")'''
# the default argument is executed even when it's not called
# the default args must be at the end of the parameters
# the default argument value can also be changed
#defaultArg("Trichy","Chennai","Ariyalur")

# aribitrary and keyword arbitrary arguments
# *args - can pass any number of args
# **kwargs - can pass any number of keyword args
def arbArguments(a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])
arbArguments(1,2,3,4,5,one=1,two=2)

# after * only keyword args is passed and not any other arguments



