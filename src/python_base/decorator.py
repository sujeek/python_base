# -*- encoding=utf-8 -*-
import time


def timer(func):
    def deco(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        print(stop-start)
    return deco


def print_log(func):
    def wrappy(x):
        func(x)
        print "logging---%s" % func.__name__
    return wrappy


def timer2(parameter):

    def outer_wrapper(func):

        def wrapper(*args, **kwargs):
            if parameter == 'task1':
                start = time.time()
                func(*args, **kwargs)
                stop = time.time()
                print("the task1 run time is :", stop - start)
            elif parameter == 'task2':
                start = time.time()
                func(*args, **kwargs)
                stop = time.time()
                print("the task2 run time is :", stop - start)

        return wrapper

    return outer_wrapper


@timer2(parameter='task1')
def task1():
    time.sleep(2)
    print("in the task1")


@timer2(parameter='task2')
def task2():
    time.sleep(2)
    print("in the task2")


@print_log
def get(x):
    print x
    print "decorator hello world"


@timer
def test(parameter):
    time.sleep(2)
    print("test is running!")
    print "===%s" % parameter

if __name__ == '__main__':
    get(2)
    # test('22222')
    #task1()
    #task2()