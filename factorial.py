def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


#fib
def fib(index):
    if index==0:
        return 0
    elif index==1:
        return 1
    else:
        return fib(index-1)+fib(index-2)
print(factorial(int(input())))

print(fib(int(input())))

