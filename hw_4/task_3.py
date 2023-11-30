import multiprocessing
import time
from multiprocessing import Pipe, Queue
import logging
import codecs

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%dT%I:%M:%S',
                    filename='artifacts/task_3.log',
                    encoding='utf-8',
                    level=logging.DEBUG
                    )


def process_a(input_queue, output_pipe):
    logging.info("Process A started")
    message = input_queue.get()
    while message != 'exit':
        logging.info(f"Process A receive: '{message}'")
        processed_message = message.lower()
        logging.info(f"Process A send response: '{message}'")
        output_pipe.send(processed_message)
        message = input_queue.get()
        time.sleep(5)
    output_pipe.send(message)
    logging.info("Process A finished")


def process_b(input_b_pipe, pipe_b_main):
    logging.info("Process B started")
    message = input_b_pipe.recv()
    while message != 'exit':
        logging.info(f"Process B receive: '{message}'")
        encoded_message = codecs.encode(message, 'rot-13')
        logging.info(f"Process B send response: '{encoded_message}'")
        pipe_b_main.send(encoded_message)
        message = input_b_pipe.recv()
    logging.info("Process B finished")


def main():
    input_a_queue = Queue(maxsize=32)
    pipe_a_b_pub, pipe_a_b_sub = Pipe()
    pipe_b_main_pub, pipe_b_main_sub = Pipe()

    process_a_instance = multiprocessing.Process(target=process_a, args=(input_a_queue, pipe_a_b_pub))
    process_b_instance = multiprocessing.Process(target=process_b, args=(pipe_a_b_sub, pipe_b_main_sub))

    process_a_instance.start()
    process_b_instance.start()

    try:
        user_input = input("Enter message (or 'exit' to quit): ")
        while user_input != 'exit':
            logging.info(f"Main process sends: '{user_input}'")

            input_a_queue.put(user_input)

            if pipe_b_main_pub.poll():
                encoded_message = pipe_b_main_pub.recv()
                logging.info(f"Main process receives: '{encoded_message}'")

            user_input = input("Enter message (or 'exit' to quit): ")

    except KeyboardInterrupt:
        pass

    finally:
        input_a_queue.put('exit')
        process_a_instance.join()
        while process_a_instance.is_alive():
            if pipe_b_main_pub.poll():
                encoded_message = pipe_b_main_pub.recv()
                logging.info(f"Main process receives: '{encoded_message}'")


if __name__ == "__main__":
    main()
