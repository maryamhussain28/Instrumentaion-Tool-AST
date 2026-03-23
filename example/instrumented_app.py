from instrumentation.decorators import trace_function
@trace_function
def compute(x):
    total = 0
    for i in range(x):
        total += i
    return total

@trace_function
def process():
    compute(10000)
    compute(20000)
process()