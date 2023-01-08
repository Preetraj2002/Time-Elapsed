import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper():
        start=time.time()
        function()
        end=time.time()
        diff=end-start
        print(f"{function.__name__} run speed: {diff}")
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10_000_000):
        i * i

@speed_calc_decorator       
def slow_function():
    for i in range(100_000_000):
        i * i

fast_function()
slow_function()