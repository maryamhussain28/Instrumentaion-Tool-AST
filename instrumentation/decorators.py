import time
from functools import wraps
from .logger import log_event

def trace_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        log_event({
            "event": "function_start",
            "function": func.__name__,
            "args": str(args),
            "kwargs": str(kwargs)
        })

        result = func(*args, **kwargs)

        end = time.time()

        log_event({
            "event": "function_end",
            "function": func.__name__,
            "latency_ms": (end - start) * 1000
        })

        return result

    return wrapper