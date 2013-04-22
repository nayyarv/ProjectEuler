__author__ = 'Varun Nayyar'
__date__ = "22/04/13 6:40 PM"

import collections
import functools


class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    Taken from the internet - official python Wiki
    '''

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)


def main():
    #Remove the memoized decorator to see the difference
    print Fibonacci(100)


@memoized
def Fibonacci(n):
    if n > 2:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
    else:
        return 1


if __name__ == "__main__":
    main()
