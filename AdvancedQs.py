###LINK: https://python.g-node.org/python-summerschool-2011/_media/materials/advanced_python/exercises.pdf ###

#first
def logged(func):
    """
    Print out the arguments before function call and
    after the call print out the returned value
    """
    def wrapper(*args, **kwargs):
        print(’you called {.__name__}({}{}{})’.format(
            func,
            str(list(args))[1:-1], 
            ’, ’ if kwargs else ’’,
            ’, ’.join(’{}={}’.format(*pair) for pair in kwargs.items()),
            ))
        val = func(*args, **kwargs)
        print(’it returned’, val)
        return val
    return wrapper