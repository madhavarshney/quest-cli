from sys import stdout
from itertools import cycle
from threading import Thread
from time import sleep
from contextlib import contextmanager


@contextmanager
def spinner(text='', finished=''):
    done = False
    finished = finished or text

    def spin():
        for c in cycle('|/-\\'):
            if done:
                break
            stdout.write(f'\r{text} {c}')
            stdout.flush()
            sleep(0.1)
        stdout.write(f'\r{finished}{" " * (len(text) - len(finished))}  \n')

    thread = Thread(target=spin)
    thread.start()

    try:
        yield
    finally:
        done = True
        thread.join()


def colorize(color, text):
    return f'\001\033[{color}\002{text}\001\033[0m\002'
