import time

def timeit(**kwargs):
    if 'loops' in kwargs:
        loops = kwargs['loops']
    else:
        loops = 1000
    def timeit_(func, **kwargs):
        def wrapper(*args, **kwargs):
            start = time.time()
            for i in range(loops):
                ans = func(*args, **kwargs)
            print(f'{func.__name__} took: {time.time() - start} for {loops} loops')
            return ans
        return wrapper
    return timeit_
