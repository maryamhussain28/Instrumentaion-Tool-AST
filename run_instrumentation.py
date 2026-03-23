import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from instrumentation.ast_instrument import instrument_code
from instrumentation.bytecode_hook import enable_bytecode_tracing

with open("example/sample_app.py") as f:
    code = f.read()

instrumented = instrument_code(code)

with open("example/instrumented_app.py", "w") as f:
    f.write("from instrumentation.decorators import trace_function\n")
    f.write(instrumented)

enable_bytecode_tracing()

exec(open("example/instrumented_app.py").read())