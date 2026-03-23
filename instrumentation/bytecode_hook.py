import sys

def trace_calls(frame, event, arg):
    if event == "call":
        code = frame.f_code
        func_name = code.co_name
        print(f"[BYTECODE TRACE] calling {func_name}")
    return trace_calls


def enable_bytecode_tracing():
    sys.settrace(trace_calls)