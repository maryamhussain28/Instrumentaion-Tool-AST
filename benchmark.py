import time
import subprocess

def run(cmd):
    start = time.time()
    subprocess.run(cmd, shell=True)
    end = time.time()

    return end - start


print("Running without instrumentation...")
baseline = run("python example/sample_app.py")

print("Running with instrumentation...")
instrumented = run("python run_instrumentation.py")

print("\nRESULTS")
print("Baseline:", baseline)
print("Instrumented:", instrumented)
print("Overhead:", instrumented - baseline)