from time import perf_counter

from memoizer import memo_wrapper # import based on your directories



# @memo_wrapper without arguments will also work
@memo_wrapper(key_list=[0]) # fib(arg0=n)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)  # Problems are repeated on both sides to add to a time complexity of O(n^2)




# n = arg0, m = arg1
# @memo_wrapper(key_list=[0,1]) # This acheives the same result
@memo_wrapper
def grid_traveler(n, m):# Without memo, time complexity = O(2^(m+n)), Space Complexity = O(m+n)
    if n == 0 or m == 0:  #
        return 0
    # below case, neither is 0, but either is 1
    elif n == 1 or m == 1:  # Only one way to travel in this case
        return 1

    return grid_traveler(n-1,m) + grid_traveler(n, m-1) # n-1 for down move, m-1 for right move

# Without memoization, it will be 2^200 problems, with memoization it's only 200 problems
t = perf_counter()
print(fib(200)) #280571172992510140037611932413038677189525
print("Execution Time : ",perf_counter()-t," ms") #Execution Time :  0.0011546999448910356  ms

#25477612258980856902730428600


# Without memoization, it will be 2^(80+80-4) problems, with memoization it's only 160 problems

t = perf_counter()
print(grid_traveler(80,80))
print("Execution Time : ",perf_counter()-t," ms")
#280571172992510140037611932413038677189525
