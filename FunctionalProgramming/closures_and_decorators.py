def counter_closure():
    x = 0

    def count():
        nonlocal x
        x += 1
        return x
    return count


def empty_check(func):
    def check(*args, **kwargs):
        res = func(*args, **kwargs)
        if res:
            print('Success: Non empty result')
            return res
        else:
            raise BaseException('Failed: Empty is not acceptable')
    return check


# Added extra functionality to existing process_string method using decorators
@empty_check
def process_string(s):
    if s == 'ramo':
        return s
    else:
        return ''


def main():
    # Creating a closure to keep track of the count
    print('#'*20, 'Closures Example', '#'*20)
    cc = counter_closure()
    for _ in range(3):
        print(cc())

    # Decorators example
    print('#' * 20, 'Decorators Example', '#' * 20)
    print(process_string('ramo'))
    print(process_string('test'))


if __name__ == '__main__':
    main()
