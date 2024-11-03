import functools


def logger_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        f_args = args
        if args and hasattr(args[0], '__dict__'):
            p_args = args[1:]
            if func.__code__.co_varnames[0] not in ["self", "cls"]:
                f_args = args[1:]
        else:
            p_args = args
        print(f"Function name: {func.__name__}")
        print(f"Arguments: {p_args} {kwargs}")

        return_value = func(*f_args, **kwargs)

        print(f"Return value: {return_value}")
        return return_value

    return wrapper


class MyClass(object):
    @logger_decorator
    def __init__(self):
        self.clss = self.my_class_class()

    @logger_decorator
    def my_func(self, a: int, b: int, c: int):
        self.d = a
        return b - a + c

    @logger_decorator
    def my_func_without_self(a: int, b: int, c: int):
        return b - a + c

    class my_class_class:
        @logger_decorator
        def my_func(self, a: int, b: int, c: int):
            self.d = a
            return b - a + c


@logger_decorator
def my_func(a: int, b: int, c: int):
    return b - a + c


my_func(5, 4, c=3)
mine = MyClass()
mine.my_func(5, 4, c=3)
mine.my_func_without_self(5, 4, c=3)
mine.clss.my_func(5, 4, c=3)