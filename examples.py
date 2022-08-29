from pprint import pprint
from time import perf_counter, perf_counter_ns

from memoizer import memo_wrapper  # import based on your directories


# @memo_wrapper without arguments will also work
@memo_wrapper(key_list=[0])  # fib(arg0=n)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)  # Problems are repeated on both sides to add to a time complexity of O(n^2)


# n = arg0, m = arg1
# @memo_wrapper(key_list=[0,1]) # This acheives the same result
@memo_wrapper
def grid_traveler(n, m):  # Without memo, time complexity = O(2^(m+n)), Space Complexity = O(m+n)
    if n == 0 or m == 0:  #
        return 0
    # below case, neither is 0, but either is 1
    elif n == 1 or m == 1:  # Only one way to travel in this case
        return 1

    return grid_traveler(n - 1, m) + grid_traveler(n, m - 1)  # n-1 for down move, m-1 for right move


# Without memoization, it will be 2^200 problems, with memoization it's only 200 problems


# @memo_wrapper(key_list=[0,2]) # both work
@memo_wrapper
def canSum(target, ls: list, idx):
    # print(target)
    if target == 0:
        return True
    elif idx == len(ls):
        return False

    # elif ls[idx] > target: # Skip if current can't be added
    #     return canSum2(target, ls, idx+1)
    # else:
    return canSum(target - ls[idx], ls, idx + 1) or canSum(target, ls, idx + 1)  # either skip or add,


# print(canSum(213421, [10, 5, 6, -1, -5, 23, 54, 123, 654, 765, 12, 43, -23, 43, -4, -54, -6, -7, -4, -3, 3, -4, -67, 2, -43, 4, 43, 32], 0))
# returns the 1st found combo
@memo_wrapper
def howSum(targetSum, numbers, idx) -> []:  # outputs a list containing A combination that adds upto target sum
    if targetSum == 0:
        return []
    elif idx == len(numbers):
        return None

    # if numbers[idx] > targetSum: # Skip if current can't be added
    #     return howSum(targetSum, numbers, idx+1)
    # else:
    # priority for skipping vs adding can be selected based on the placement of r1 call compared to r2 call
    r2 = howSum(targetSum, numbers, idx + 1)  # skip
    if r2 is not None:  # r2 reached upto goal
        return r2

    r1 = howSum(targetSum - numbers[idx], numbers, idx + 1)
    if r1 is not None:  # returned item instead of None:
        l = [{idx: numbers[idx]}]
        l.extend(r1)
        return l

    return None


# print(howSum(213421, [10, 5, 6, -1, -5, 23, 54, 123, 654, 765, 12, 43, -23, 43, -4, -54, -6, -7, -4, -3, 3, -4, -67, 2, -43, 4, 43, 32], 0))
#
# print(howSum(105, [7, 2, 6, 7, 8, 3, 7, 4, 5, 6, 7, -2, -5, -8, 10, 5, 6, -3, -5, 21, -65, -2, 9, 3, 4], 0))


@memo_wrapper
def bestSum(targetSum, numbers, idx) -> []:  # outputs a list containing A combination that adds upto target sum
    if targetSum == 0:
        return []
    elif idx == len(numbers):
        return None

    # if numbers[idx] > targetSum: # Skip if current can't be added
    #     return howSum(targetSum, numbers, idx+1)
    # else:
    # priority for skipping vs adding can be selected based on the placement of r1 call compared to r2 call
    r2 = bestSum(targetSum, numbers, idx + 1)  # skip

    # if r2 is not None:  # r2 reached upto goal
    #     return r2

    r1 = bestSum(targetSum - numbers[idx], numbers, idx + 1)
    if r1 is not None:  # returned item instead of None:
        l = [{idx: numbers[idx]}]
        l.extend(r1)
        # return l

    if r1 is not None and r2 is not None:
        return l if len(r1) < len(
            r2) else r2  # the shorter length upto this point will be the shorter length afterwards as well
    elif r1 is not None:
        return l
    elif r2 is not None:
        return r2
    else:
        return None


# print(bestSum(105, [7, 2, 6, 7, 8, 3, 7, 4, 5, 6, 7, -2, -5, -8, 10, 5, 6, -3, -5, 21, -65, -2, 9, 3, 4], 0))


# t = perf_counter()
# print(fib(200)) #280571172992510140037611932413038677189525
# print("Execution Time : ",perf_counter()-t," ms") #Execution Time :  0.0011546999448910356  ms

# 25477612258980856902730428600


# Without memoization, it will be 2^(80+80-4) problems, with memoization it's only 160 problems

# t = perf_counter()
# print(grid_traveler(80,80))
# print("Execution Time : ",perf_counter()-t," ms")
# 280571172992510140037611932413038677189525

target = 'mynameismichealjonescalmerismystyle'
word_bank = ['myname','ameis', 'micheal', 'ismicheal', 'ljones', 'jones', 'calmer', 'calm', 'er', 'ismystyle']
# Time : .startswith: O(n), loop: O(len(word_set=m)), calls: O(len(target)=n)
# at worst, each problem can break down into m more problems and that can happen upto n times.
# ALso, within each iter out of m^n iterations of for loop, at worst, slicing can require n iterations itself.
# --> Time: O(m^n *n)
# max depth is n, so max n call stack, Also, at each depth, new str of O(n) added
# Space O(n*n) --> O(n^2)
@memo_wrapper(key_list=[0])
def can_construct_new(target: str, word_bank) -> bool: # Below solution of can_construct solves a different problem
    if target == '':
        return True
    r = [] # Will store trues and falses
    for item_set in word_bank:
        if target.startswith(item_set, 0, len(item_set)):
            if(can_construct_new(target[len(item_set):], word_bank)):
                return True # To skip useless iterations from the below line
            # r.append(can_construct_new(target[len(item_set):], word_bank))

    return False # not using r array, This is for early optimized stoppage
    # return any(r)
@memo_wrapper
def count_construct(target: str, word_bank) -> int: # Below solution of can_construct solves a different problem
    if target == '':
        return 1
    total_count = 0
    for item_set in word_bank:
        if target.startswith(item_set, 0, len(item_set)):
            total_count+= count_construct(target[len(item_set):], word_bank)

    return total_count


# print(count_construct(target, word_bank))
# print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
#     'e',
#     'ee',
#     'eee',
#     'eeee',
#     'eeeee',
#     'eeeeee',
#     'eeeeee',
#     'ef',
#     'f',
#     'eef',
#     'eeef',
#     'eeeef'
# ]))
from array import array as ar
@memo_wrapper(key_list=[0])
def all_construct(target: str, word_bank): # Below solution of can_construct solves a different problem
    if target == '':
        return [[]] # Just to make it not None
    r_list = []
    for item_set in word_bank:
        if target.startswith(item_set, 0, len(item_set)):
            next_r = all_construct(target[len(item_set):], word_bank)
            l = list(map(lambda way: [item_set, *way], next_r))
            r_list.extend(l)

    return r_list
print(all_construct(target, word_bank))
print(all_construct('skateboard', ['scoobi','ska','board']))
# print(all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
#     'e',
#     'ee',
#     'eee',
#     'eeee',
#     'eeeee',
#     'eeeeee',
#     'eeeeee',
#     'ef',
#     'f',
#     'eef',
#     'eeef',
#     'eeeef'
# ]))
# print(can_construct_new(target, word_bank))
print(can_construct_new('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee',
    'eeeeee'
]))
# print('hockeyplayer'.startswith('hockep',0,len('hockep')))
# print('kep' in 'hockeyplayer')
# print('key' in 'hockeyplayer')

# Word Bank elements are reuseable
# Worst case is that target[idx] gets matched by the last item in word_bank for each match
# Time: O(n*m): n = len(target), m = len(word_bank)
# Nothing to memoize since no  repetition
def can_construct(target: str, idx,
                  word_bank: set) -> bool:  # returns a boolean indicating whether target can be constructed from wordbank.
    if idx == len(target):  # All elements matched
        return True
    for item in word_bank:
        #Below if also filters out the unncessecary tree.
        if item == target[idx]:  # Match the remaining 1st element of target string
            # Using idx instead of slicing target since that is O(1) instead of being O(target*target)
            return can_construct(target, idx+1, word_bank)

    return False # If not matched, then return false
# print(can_construct('pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp', 0, {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'}))
# def slice_next(st):
#     if st == "":
#         return
#
#     slice_next(st[1:])
#
#
# def pass_next(st, idx):
#     if idx == len(st):
#         return
#
#     pass_next(st[idx], idx + 1)
#
# # Below demonstrates the use of slicing remaining string compared to passing the next index value
# # tl = 'jakie Chan ki band baj gai'
# # tl = 'jakie Chan ki band baj gaijakie Chan ki band baj gai'
# tl = 'jakie Chan ki band baj gaijakie Chan ki band baj gaijakie Chan ki band baj gaijakie Chan ki band baj gai'
# # tl = 'jakie Chan ki band baj gai. Let\'s add as many more indexes as we can to see the performane difference of slicing vs passing'
#
# t = perf_counter_ns()
# slice_next(tl)
# ns_t1 = perf_counter_ns() - t
# print(f"time slice remaining: {ns_t1} ns")
#
# t = perf_counter_ns()
# pass_next(tl, 0)
# ns_t2 = perf_counter_ns() - t
# print(f"time pass next index: {ns_t2} ns")
#
# print(f'order of diff = {ns_t1/ns_t2}')
