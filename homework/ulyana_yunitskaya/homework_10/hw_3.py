def main_operation(func):

    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first < 0 or second < 0:
            operation = '*'
        elif first > second:
            operation = '-'
        else:
            operation = '/'
        return func(first, second, operation)

    return wrapper


@main_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


a = int(input('Write first number'))
b = int(input('Write second number'))

result = calc(a, b)
print("Result:", result)
