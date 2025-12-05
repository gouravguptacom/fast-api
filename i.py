import time

def slow(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                time.sleep(1)
                func(*args, **kwargs)
        return wrapper
    return decorator

@slow(3)
def greet() -> None:
    print("Hello World")

@slow(10)
def hello() -> None:
    print("Wow")

hello()