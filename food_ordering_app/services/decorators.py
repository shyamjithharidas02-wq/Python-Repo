from functools import wraps
import time


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n📌 Executing: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"\n📌 Finished: {func.__name__}")
        return result

    return wrapper


def login_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.current_user is None:
            print("❌ Please login first")
            return

        return func(self, *args, **kwargs)

    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏰ Execution time: {end-start:4f} sec")
        return result

    return wrapper
