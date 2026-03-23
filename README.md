# Experimental Code Instrumentation Pipeline (AST + Bytecode)

This project implements a lightweight experimental code instrumentation pipeline in Python using Abstract Syntax Tree (AST) transformation, decorator-based probes, and bytecode-level tracing. The system automatically injects monitoring logic into Python functions, captures execution events, and evaluates runtime overhead to study observability trade-offs.

## Overview

The goal of this project is to demonstrate how observability instrumentation can be implemented without modifying application logic manually. The pipeline parses source code, injects tracing decorators at function boundaries, enables runtime bytecode tracing, and logs execution metrics such as latency and call events.

The framework is designed as a minimal prototype for runtime observability, performance profiling, and instrumentation research.

## Features

- Automatic AST-based function instrumentation  
- Decorator-based function tracing  
- Bytecode-level execution tracing using sys.settrace  
- Function entry and exit logging  
- Execution latency measurement  
- Structured JSON logging  
- Lightweight instrumentation overhead  
- Performance benchmarking support  

## Architecture

Source Code  
↓  
AST Parser  
↓  
Instrumentation Injection  
↓  
Decorators + Bytecode Hooks  
↓  
Execution  
↓  
Logs and Latency Metrics  

## Project Structure

```
Instrumentation-Tool-AST/
│
├── instrumentation/
│   ├── ast_instrument.py
│   ├── decorators.py
│   ├── bytecode_hook.py
│   ├── logger.py
│   └── __init__.py
│
├── example/
│   ├── sample_app.py
│   └── instrumented_app.py
│
├── run_instrumentation.py
├── benchmark.py
└── README.md
```

## How It Works

### AST Instrumentation

The pipeline parses Python source code and automatically injects tracing decorators into each function definition. This allows monitoring without modifying the original code manually.

### Decorator-Based Probes

Injected decorators capture:

- function start events  
- function end events  
- function arguments  
- execution latency  
- timestamps  

### Bytecode Tracing

Runtime tracing is enabled using Python's sys.settrace() to capture function call events at the interpreter level.

### Logging

All instrumentation events are written as structured JSON logs for analysis.

## Running the Instrumentation

Run the instrumentation pipeline:

```
py run_instrumentation.py
```

Example output:

```
[BYTECODE TRACE] calling process
[BYTECODE TRACE] calling compute

{'event': 'function_start', 'function': 'process'}
{'event': 'function_start', 'function': 'compute'}
{'event': 'function_end', 'function': 'compute', 'latency_ms': 5.8}
{'event': 'function_end', 'function': 'process', 'latency_ms': 25.2}
```

## Performance Benchmark

To measure instrumentation overhead:

```
py benchmark.py
```

Example output:

```
Baseline: 0.02s
Instrumented: 0.08s
Overhead: 0.06s
```

This evaluates the runtime cost introduced by instrumentation probes.

## Observability Signals Captured

- Function call tracing  
- Execution latency  
- Call hierarchy  
- Runtime events  
- Structured logs  
- Instrumentation overhead  

## Example

Original function:

```python
def compute(x):
    total = 0
    for i in range(x):
        total += i
    return total
```

Instrumented automatically:

```python
@trace_function
def compute(x):
    total = 0
    for i in range(x):
        total += i
    return total
```

## Use Cases

- Runtime observability research  
- Performance profiling  
- Debug instrumentation  
- Automatic tracing  
- Lightweight APM prototype  
- Monitoring experiments  

## Technologies

- Python  
- AST module  
- sys.settrace  
- Decorators  
- JSON logging  

## Future Extensions

- OpenTelemetry integration  
- Distributed tracing support  
- Metrics aggregation  
- Visualization dashboard  
- Dynamic runtime instrumentation  
- Overhead optimization  

## Author

Maryam Hussain
