import threading
import multiprocessing
import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def run_fibonacci_sync(n, result_file):
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    execution_time = end_time - start_time
    with open(result_file, 'a') as f:
        f.write(f"Sync: Fib({n}) = {result}, Execution Time: {execution_time:.5f} seconds\n")


def run(start_time, tasks, task_type, result_file):
    for task in tasks:
        task.start()

    for task in tasks:
        task.join()

    end_time = time.time()
    execution_time = end_time - start_time
    with open(result_file, 'a') as f:
        f.write(f"{task_type}: Fib({n}) = {fibonacci(n)}, Execution Time: {execution_time:.5f} seconds\n")


def run_fibonacci_threading(n, result_file):
    start_time = time.time()
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)

    run(start_time, threads, 'Threading', result_file)


def run_fibonacci_multiprocessing(n, result_file):
    start_time = time.time()
    processes = []
    for _ in range(10):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(process)

    run(start_time, processes, 'Multiprocessing', result_file)


if __name__ == "__main__":
    n = 40
    result_file = "artifacts/fibonacci_results.txt"

    run_fibonacci_sync(n, result_file)

    run_fibonacci_threading(n, result_file)

    run_fibonacci_multiprocessing(n, result_file)
