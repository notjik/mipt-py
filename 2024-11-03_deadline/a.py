import abc
import os
import sys
import contextlib


class AbstractStd:
    @staticmethod
    @abc.abstractmethod
    def get():
        pass


class ToStdout(AbstractStd):
    @staticmethod
    def get():
        return sys.stdout


class ToStderr(AbstractStd):
    @staticmethod
    def get():
        return sys.stderr


class ToDevnull(AbstractStd):
    @staticmethod
    def get():
        return open(os.devnull, 'w')


@contextlib.contextmanager
def stream_switcher(stdout=AbstractStd, stderr=AbstractStd):
    sys.stdout, sys.stderr = stdout.get(), stderr.get()

    try:
        yield
    finally:
        sys.stdout, sys.stderr  = sys.__stdout__, sys.__stderr__


if __name__ == '__main__':
    with stream_switcher(stdout=ToStderr, stderr=ToStdout) as switcher:
        print('hi', file=sys.stdout)
