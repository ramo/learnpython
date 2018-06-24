def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a // b


def echo_operation(op, x, y):
    print("Doing operation = {0} on {1} and {2}".format(op, x, y))

    def fun():
        print(op(x, y))

    # Returning function as return value
    return fun


def hello(h):
    def world(w):
        print(h, w)
    return world


def main():
    # Hello world
    world = hello('Hello')
    world('World')
    hello('Hello')('World')

    # Using functions as list elements
    operations = [add, subtract, multiply, divide]
    x, y = 10, 5
    # Iterating functions in a list
    for op in operations:
        # Passing function to another function
        fun = echo_operation(op, x, y)
        fun()


if __name__ == '__main__':
    main()
