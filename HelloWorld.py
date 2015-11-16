__author__ = 'Esmidth'


def ask_ok(prompt, retries=4, complaint="Yes or no,please!"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True;
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)


i = 5


def f(arg=i):
    print(arg)


def ff(a, l=None):
    if l is None:
        l = []
    l.append(a)
    return l


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


class MyClass:
    """A simple example class"""

    def __init__(self):
        self.data = []

    i = 12345

    def f(self):
        return 'HelloWord'


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update


class MappingSubClass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)


class Employee:
    pass


if __name__ == "__main__":
    john = Employee()
    john.name = "John Doe"
    john.dept = 'computer lab'
    john.salary = 1000
