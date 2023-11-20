def my_func():
    print("Hello from my function")
    return 0

def my_rec(x):
    print(x)
    #base case or stopping point
    if x == 0:
        return 0
    else:
        my_rec(x - 1)


#recursive factorial
def my_fac(n):
    if n == 1:
        return_value = 1
    else:
        return_value = n * my_fac(n-1)
    
    return return_value

#same problem with visual of the return chain
def fac(n):
    print(f"fac() called with n ={n}")
    rv = 1 if n <= 1 else n * fac(n-1)
    print(f"-> fac({n}) returns {rv}")
    return rv

#fibonacci sequence
def fib(n):
    #base cases
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(6))

    #recursive call

