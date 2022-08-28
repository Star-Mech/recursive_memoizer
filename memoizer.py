# Use memoization to save and use answer for repeating problems
def memo_wrapper(*ar, **kw):  # Pass key_list=[list of arguments to be used in key]
    """ Function wraps recursive function and adds memoization.

    Takes as argument, the argument numbers as well as kwargs to pinpoint the
    decorated function arguments to be used for naming dict.

    Attributes:
    :key key_list (kwarg): A list containing arg numbers and kwarg name to be used as memoizer dict key.
    if key not specified, then a key containing all args and kwargs is used for memo
    """

    def memoizer(func):
        memo = {}
        key_list = kw.get('key_list')

        def wrapper(*args, **kwargs):
            if key_list:
                key_memo = tuple(args[i] if type(i) is int else kwargs.get(i) for i in key_list)
            else:
                key_memo = tuple(item for item in args if type(item) is not list)
            if key_memo not in memo:
                memo[key_memo] = func(*args, **kwargs)
            return memo[key_memo]

        return wrapper

    if kw:
        return memoizer
    else:
        return memoizer(*ar)
