# Scope



def foo():
    #x = x + 1 -- creates an Error!
    #x = 2
    global x
    x = 2
    print(f'in foo x = {x}')
    def moo():
        print("I am goo!")
    return x

#goo ( foo() )

foo()
#moo()
print(f'global x is {x}')

def myAdd(l1):
    l1.append(1)

def addDict(d1): # d1 = #50
    d1[1] =12
    d1 = { } # this does nothing for global scope
    # d1 = #100

def addNumber(x):
    x = x + 1
    print(f'in function x = {x}')
l2 = [1,2,3]
myAdd(l2)
print(l2)

d1 = {8:1}
addDict(d1)
print(d1)
x = 9
addNumber(x)
print(x)


