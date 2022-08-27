import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        for i in range(1000):
            func(*args, **kwargs)
        print(f'{func.__name__} took: {time.time() - start}')
    return wrapper
