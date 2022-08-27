# Use memoization to save and use answer for repeating problems
def memo_wrapper(**kwargs):  # Pass key_list=[list of arguments to be used in key]
    """Attributes:
    key_list: list of input args number to be used as memoizer"""

    def memoizer(func):
        memo = {}
        key_list = kwargs.get('key_list')

        def wrapper(*args, **kwargs):
            key_memo = tuple(args[i] if type(i) is int else kwargs.get(i) for i in key_list)
            if args not in memo:
                memo[args] = func(*args, **kwargs)
            return memo[args]

        return wrapper

    return memoizer
