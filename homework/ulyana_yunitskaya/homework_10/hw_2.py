def repeat_me(func):

    def wrapper(anything, count):
        for _ in range(count):
            func(anything)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('look at me', count=6)
