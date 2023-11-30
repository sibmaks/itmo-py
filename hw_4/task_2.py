import math
import concurrent.futures
import logging
import multiprocessing
import time

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%dT%I:%M:%S',
                    filename='artifacts/task_2.log',
                    encoding='utf-8',
                    level=logging.DEBUG
                    )
logger = logging.getLogger(__name__)


def integrate_worker(f, a, start, end, step):
    acc = 0
    for i in range(start, end):
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=1000000):
    step = (b - a) / n_iter
    chunk_size = n_iter // n_jobs

    def execute_with_executor(executor):
        futures = []
        with executor as pool:
            for i in range(n_jobs):
                start = i * chunk_size
                end = (i + 1) * chunk_size if i < n_jobs - 1 else n_iter
                futures.append(pool.submit(integrate_worker, f, a, start, end, step))
                logger.info(f'Task {i + 1}/{n_jobs} submitted to executor.')

            acc = sum(future.result() for future in concurrent.futures.as_completed(futures))
        return acc

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
        result_thread = execute_with_executor(executor)

    thread_executor_time = time.time() - start_time

    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
        result_process = execute_with_executor(executor)

    process_executor_time = time.time() - start_time

    return result_thread, result_process, thread_executor_time, process_executor_time


if __name__ == "__main__":
    cpu_num = multiprocessing.cpu_count()
    for n_jobs in range(1, cpu_num * 2 + 1):
        result_thread, result_process, thread_executor_time, process_executor_time = integrate(math.cos, 0, math.pi / 2,
                                                                                               n_jobs=n_jobs)

        logger.info(f'Jobs count: {n_jobs}')
        logger.info(f'Thread Executor Time: {(thread_executor_time * 1000):.2f} millis')
        logger.info(f'Process Executor Time: {(process_executor_time * 1000):.2f} millis')
        logger.info(f'Result (Thread): {result_thread}')
        logger.info(f'Result (Process): {result_process}')
